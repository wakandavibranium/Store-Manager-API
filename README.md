[![Build Status](https://travis-ci.com/wakandavibranium/Store-Manager-API.svg?branch=ch-integrate-travis-%23161202921)](https://travis-ci.com/wakandavibranium/Store-Manager-API)   [![Coverage Status](https://coveralls.io/repos/github/wakandavibranium/Store-Manager-API/badge.svg?branch=ch-integrate-travis-%23161202921)](https://coveralls.io/github/wakandavibranium/Store-Manager-API?branch=ch-integrate-travis-%23161202921)   [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/625f37020e835b5e8fad)

# Store-Manager-API
This is an API for the Store Manager web application. Store Manager is a web application that helps store owners manage sales and product inventory records.


## Documentation

1. API documentation can be found [here](https://store-manager-api-adc2.herokuapp.com/api/v1)

2. PivotalTracker stories can be found [here](https://www.pivotaltracker.com/n/projects/2202783)


## Prerequisites

1. Download & install [Python 3+](https://www.python.org/downloads/)

2. Download & install [Git](https://git-scm.com/downloads) 

3. Download & install [Postman](https://www.getpostman.com/apps)


## Installation & Configurations

1. Create a directory and `cd` into it

2. ```git clone https://github.com/wakandavibranium/Store-Manager-API.git```

3. `cd` into the Store-Manager-API repo

4. ```git checkout ft-user-login-#161360421```

5. Create a [virtual environment](https://virtualenv.pypa.io/en/stable/) for this project and activate it.

6. Open the terminal and type ```pip install -r requirements.txt``` 
   This will install project dependancies.

### Configuring environment variables on windows, 
```
set FLASK_APP=run.py
set FLASK_ENV=development
set SECRET_KEY=thisisyoursecretkey
```

### Configuring environment variables on linux, 
```
export FLASK_APP=run.py
export FLASK_ENV=development
export SECRET_KEY=thisisyoursecretkey
```

## Running The App
On your terminal

```flask run```

## Consuming the API

* Open your web browser and enter ```http://127.0.0.1:5000/api/v1``` in the address bar

```or```

* Visit the API hosted on [Heroku](https://store-manager-api-adc2.herokuapp.com/api/v1)


## API Endpoints Implemented

| HTTP Method   |  EndPoint             | Description                             |
| --------------|:----------------------|:---------------------------------------:|                                                                 
| POST          | /products/            | Add a product                           | 
| GET           | /products/            | Get all products                        | 
| GET           | /products/{id}        | Get a product by id                     |
| POST          | /sales/               | Add a sale                              |
| GET           | /sales/               | Get all sales                           |
| GET           | /sales/{id}           | Get a sale by id                        |
| POST          | /auth/signup/         | Sign Up a user                          |
| GET           | /auth/signup/         | Get all users                           |
| POST          | /auth/login/          | Login a user                            |