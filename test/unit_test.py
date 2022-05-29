from email import header
from pathlib import Path
from wsgiref import headers
import pytest
from app.app import init_app

@pytest.fixture()
def app():
    app = init_app(True)
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# def test_request_example(client):
#     response = client.get("/api/customers/")
#     assert response.status_code == 200
    # assert b"<h2>Hello, World!</h2>" in response.data
# resources = Path(__file__).parent.parent / 'app/api/resources'

def test_add_customer(client):
    correct_customer = client.post("/api/customers/",  json=({
        "name": "giuliana",
        "surname": "silva"
    }))
    wrong_name = client.post("/api/customers/",  json=({
        "name": 2,
        "surname": "silva"
    }))
    wrong_surname = client.post("/api/customers/",  json=({
        "name": "giuliana",
    }))

    assert correct_customer.status_code == 200
    assert wrong_name.status_code == 400
    assert wrong_surname.status_code == 400


def test_get_customer(client):
    response = client.get("/api/customers/1")
    assert response.status_code == 200
    assert response.json["name"] == "giuliana"
    assert response.json["surname"] == "silva"
    assert response.json["accounts"] == []


def test_create_account(client):
    correct_account = client.post("/api/accounts/",  json=({
        "customer_id": "1",
        "initialCredit": 2
    }))
    correct_account2 = client.post("/api/accounts/",  json=({
        "customer_id": "1",
        "initialCredit": 1
    }))

    client.post("/api/customers/",  json=({
        "name": "giuliana2",
        "surname": "silva"
    }))
    
    correct_account_with_zero_credit = client.post("/api/accounts/",  json=({
        "customer_id": "2",
        "initialCredit": 0
    }))

    wrong_customer_id = client.post("/api/accounts/",  json=({
        "customer_id": "3",
        "initialCredit": 2
    }))
    
    assert correct_account.status_code == 200
    assert correct_account.json['transaction_id'] == "1"

    assert correct_account_with_zero_credit.status_code == 200
    assert correct_account_with_zero_credit.json['transaction_id'] == None
    
    assert wrong_customer_id.status_code == 400
    

def test_get_all_info(client):
    get_info = client.get("/api/customers/1")
    get_info2 = client.get("/api/customers/2")

    print('DEBUG >>',get_info.json)
    assert get_info.json['total_balance'] == get_info.json['accounts'][0]['balance'] + get_info.json['accounts'][1]['balance']
    assert get_info2.json['accounts'][0]['transactions'] == []




    