# Google Cloud Functions Course
## Starting a project
To start a new project in Google Cloud, we can go the [Firebase Console](https://console.firebase.google.com/) or create it from [Google Cloud Platform Console](https://console.cloud.google.com)
## Create a virtual environmet
First we have to install python3.venv with the following command:
```
sudo apt install python3.venv
```
Then, we execute the following command:
```
python3 -m venv venv
```
After activate Virtual Enviroment:
```
source venv/bin/activate
```
In order to add new packages to our new virtual enviroment we create a file called `requirements.txt` and execute the following command:
```
pip install -r requirements.txt
```
We need config on congiguration on pycharm de projeto-interpreter with the virtual enviroment
