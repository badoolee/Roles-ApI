# API Documentation

This document provides documentation for a Roles REST API, which allows CRUD (Create, Read, Update, Delete) operations to assign roles to users.

## Setup
1. Clone this repository to your local machine:

   **git clone** [repository-url]

2. Create a virtual environment and activate it:
    First ensure that python is installed in your computer then create a virtual environment by pressing control+shift+p on your keyboard and select python environment. create the virtual environment with the lastest version of python on your PC e.g python version 3.11.0.

3. Before you proceed, make sure you have the following packages are installed:

    - django
    - djangorestframework
    - requests

    Install the above packages by:

    **pip install -r requirements.txt**

4. Initialize the database and create the necessary tables:

    python manage.py makemigrations
    python mange.py migrate

## Running The Application
To run the application, open your terminal and run **python manage.py runserver**






## Standand Format and Usage of Api

1. Creating an admin user:
    To create a admin user, open terminal and run **python manage.py createsuperuser**, then input your email and passsword to register as an admin. 


2. Registering new user:
    To register new user, open postman and input the user email and password.

    Example:
    POST [http://127.0.0.1:8000/user/register/]

    REQUEST:
    ```
    {
	"email": "email@gmail.com",
    "password: "password"
    }
    ```

    RESPONSE:
     ```
    {
        "status": 200,
        "message": "Registration successful, please check your email to confirm",
        "data": User's info,
        }
    ```
    And if the email already exist, it returns:

    RESPONSE:
     ```
    {
    "Message":  "The email already exists"
    }
     ```

    Then verify the user using the following format

    Example:
    POST [http://127.0.0.1:8000/user/verify/]

    REQUEST:
    ```
    {
	"email": "email@gmail.com",
    "otp: otp code
    }
    ```

    RESPONSE:
     ```
    {
        "status": 200,
        "message": "account verified",
        "data": {},
        }
     ```





3. Creating a new role:
    A role is created using the following format

    Example:
    POST [http://127.0.0.1:8000/role/list/]

    REQUEST:
    ```
    {
    "name": "Taiwo",
    "description: "Data analyst"
    }

    RESPONSE:
     ```
    {
    "name": "Taiwo",
    "description: "Data analyst"
    }
    ```


4. Getting the list of all the roles:
    The list of the roles using the following format

    Example:
    GET [http://127.0.0.1:8000/role/list/]


3. Deleting a role:
    A role is deleted using the following format

    Example:
    DELETE [http://127.0.0.1:8000/role/1/]


4. Inputting a new role into an existing one:
    A role is deleted using the following format

    Example:
    PUT [http://127.0.0.1:8000/role/1/]

    REQUEST:
     ```
    {
    "name": "Femi",
    "description: "Backend Developer"
    }
    ``` 

## 