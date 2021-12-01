import requests
import json

def test_input():
    """
    Testing inputs to system
    """
    inputurl = "http://localhost:8080/input"
    for line in open("TextFiles/list.txt","r"):
        json_data = json.loads(line)
        response = requests.post(url= inputurl,json = json_data)
        print(response.status_code, response.reason)
    geturl = "http://localhost:8080/checkBalance"
    output = requests.get(url=geturl)
    print(output.status_code, output.reason)
    data = output.json()
    assert data == json.loads(open("TextFiles/tst.txt","r").read())

def test_spend_points():
    """
    Testing spendPoints
    """
    spendurl = "http://localhost:8080/spendPoints"
    data = json.loads('{ "points": 5000 }')
    response = requests.post(url = spendurl, json = data)
    print(response.status_code, response.reason)
    data = response.json()
    testData = open("TextFiles/outputText.txt","r").read()
    assert data == testData

def test_balance():
    """
    Testing checkBalance
    """
    geturl = "http://localhost:8080/checkBalance"
    output = requests.get(url=geturl)
    print(output.status_code, output.reason)
    data = output.json()
    assert data == json.loads(open("TextFiles/balance.txt","r").read())
