import myUser
import json

testUser = myUser.myUser()

def test_loadin():
    file = open("TextFiles/list.txt","r")
    for line in file:
        testUser.transaction(json.loads(line))
    file.close
    assert testUser.checkBalance() == open("TextFiles/tst.txt","r").read()

def test_spendPoints():    
    results = testUser.spendPoints(json.loads('{"points":"5000"}'))
    assert results == open("TextFiles/outputText.txt","r").read()

def test_checkBalance():
    data = testUser.checkBalance()
    load = open("TextFiles/balance.txt","r").read()
    assert data == load

def test_sameSamePoints():
    testUser.transaction(json.loads(
        '{ "payer": "Carmax", "points": 1000, "timestamp": "2020-10-02T14:00:00Z" }'))
    for i in range(3):
        results = testUser.spendPoints(json.loads('{"points":100}'))
    data = json.loads(testUser.checkBalance())
    assert data["Carmax"] == 700
