# tekever-a2

## Introduction

The assessment consists of an API to open a new &quot;current account of already existing customers. 

- The API will expose an endpoint that accepts the user information (customerID, initialCredit). 
- Once the endpoint is called, a new account will be opened and connected to the user whose ID is customerID. 
- Also, if initialCredit is not 0, a transaction will be sent to the new account. 
- Another Endpoint will output the user information showing Name, Surname, balance, and transactions of the accounts. 

### Requirements

Add .env in the directory root:

        ENV=development
        SECRET_KEY=SECRET_KEY
        PORT=5000


## Run with Docker

### Install
- Docker https://docs.docker.com/get-docker/
- Docker Compose https://docs.docker.com/compose/install/

### Execution
    docker build --tag a2 .
    docker run -d -p 5000:5000 a2
    
Go to http://localhost:5000/api
  
## Run without Docker

### Install
- Python 3.10.4 https://www.python.org/downloads/windows/

### Execution
#### Linux:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python index.py
  
#### Windows:
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python index.py

Go to http://localhost:5000/api

### Testing:
    pytest
