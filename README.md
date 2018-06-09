# py-webservices
WebServices-project M1 I2L 2017-2018

This project aims to provide a social-network that surpasses both twitter and facebook by far.

Installation
============

On a debian-like system

```bash
sudo apt install python3 python3-pip
sudo pip3 install -r requirements.txt
```

Then, clone this repo as non-privileged user

```bash
git clone https://github.com/mmequignon/py-webservices
cd py-webservices
```


Configuration
=============

In webservices/settings.py, you should customize ALLOWED_HOSTS depending on your configuration.
For example:
```python
ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
]
```

Everything else should be well configured out of the box.


First run
=========

There is no database in this repo, you should first create one.

```bash
python3 manage.py makemigrations

```

Then, you will have to create a new super user.

```bash
python3 manage.py createsuperuser
```

You can now run the Django webserver
```bash
python3 manage.py runserver
```

Usage
=====

At superuser creation, an auth token has been created. We will firt get it.

```bash
curl -X POST http://py-webservices.lxc:8000/get_auth_token/ -H 'Accept: application/json; indent=4' -d 'username=admin&password=superadmin'
{
    "token": "03c1931bbb8885f3fa0f3410686d7ad78c4f9134"
}
```

You can now create a new Buddy instance:
```bash
curl -X POST http://py-webservices.lxc:8000/buddy/ -H 'Accept: application/json; indent=4' -d 'username=supertoto&password=supertoto' -H 'Authorization: Token 03c1931bbb8885f3fa0f3410686d7ad78c4f9134'
{
    "id": 2,
    "username": "supertoto",
    "email": ""
}
```

Here is a list of all of the available operations for each models

| Action         | Method | route       |
|----------------|--------|-------------|
| create         | POST   | model/      |
| list           | GET    | model/      |
| update         | PUT    | model/<pk>/ |
| partial update | PATCH  | model/<pk>/ |
| delete         | DELETE | model/<pk>/ |
