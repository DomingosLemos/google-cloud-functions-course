from flask import abort

def get_bearer_token(request):
    bearer_token = request.headers.get('Authorization', None)
    if not bearer_token:
        abort(401)
    parts = bearer_token.split()
    if parts[0].lower()!= "bearer":
        # autorization header must start wit 'Bearer'
        abort(401)
    elif len(parts) == 1:
        # token was not found
        abort(401)
    elif len(parts) > 2:
        # autorization header must be os the form 'Bearer token'
        abort(401)
    bearer_token = parts[1]
    return bearer_token


def hello_world(request):
    import os

    #apenas permitir metodo POST
    if request.method != 'POST':
        abort(405)

    #garantir que o header trás o token
    bearer_token = get_bearer_token(request)
    secret_key = os.environ.get('ACCESS_TOKEN')
    if bearer_token != secret_key:
        abort(401)

    request_args = request.args
    request_json = request.get_json(silent=True) #silent para colocar null na variável caso não passe parametros
    #if request_args and 'name' in request_args and 'lastname' in request_args:
    parameters = ('name', 'lastname')
    if request_args and all(k in request_args for k in parameters):
        name = request_args['name']
        lastname = request_args['lastname']
    #elif request_json and 'name' in request_json and 'lastname' in request_json:
    elif request_json and all(k in request_json for k in parameters):
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        abort(400)
        name = 'World'
        lastname = ''
    return f'Hello {name} {lastname}'
