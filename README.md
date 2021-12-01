# SampleWebService
Sample web service to track a user's points by point provider.

## Installation

### Requirements
In order to run this web service you will need to:
* Be using Python 3.8
* Install CherryPy
This can be done by using the package manager [pip](https://pip.pypa.io/en/stable/).
```bash
pip3 install cherrypy
```
You can also install CherryPy by following [this](https://docs.cherrypy.dev/en/latest/install.html) page.

### Setup
To run this project, clone to a desired directory:
```
$ ../git clone https://github.com/AdrianMartinezCodes/SampleWebService.git
$ cd SampleWebService
$ python3 webService.py
```
Default port is 8080.
## Usage
This webService accepts requests to the following endpoints:
```bash
localhost:xxxx/inputTransaction

localhost:xxxx/spendPoints

localhost:xxxx/checkBalance

shutdown:xxxx/shutdown
```
### /inputTransacation
Input: expects a JSON string in the form 
```javascript
{"payer":name,"points":num,"timestamp":time}
```
The input will be processed and updates the running total of the user

#### Example
By using curl, the following JSON string: 
```javascript
{ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
```
can be passed in:
```bash
$ curl http://localhost:xxxx/inputTransaction -H "Content-Type: application/json" -d \
'{ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }'
```
Calling **/checkBalance** outputs:
```javascript
{"DANNON":1000}
```



### /spendPoints
Assumptions: A populated user
Cannot spend points > myUser.runningTotal
Input: expects a JSON string in the form
```javascript
{"points":num}
```
The input is processed and the points are subtracted from the users account by oldest transaction first
Return: JSON string of form: 
```javascript
[{payer:payer1, points: -num1},{payer:payer1, points: -num2,...}
```

#### Example
Assume the user has populated with 
```javascript
{ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
```
Then calling
```bash
$ curl http://localhost:xxxx/spendPoints -H "Content-Type: application/json" -d '{"points":100}'
```
returns
```javascript
[{"DANNON":-100}]
```

### /checkBalance
Outputs the totals of the providers
Returns: JSON string of form 
```javascript
{"payer1": runningTotal1, "payer2": runningTotal2,...}
```

#### Example
See usage in **/inputTransaction**

### /shutdown
Stops the server


## Running Tests(Optional)
Running the tests requires installing [requests](https://docs.python-requests.org/en/master/) and [pytest](https://docs.pytest.org/en/6.2.x/) libraries.
To run:
```bash
$ installedDir/pytest
```
