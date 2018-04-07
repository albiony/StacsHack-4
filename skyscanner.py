import requests

baseURL = "http://partners.api.skyscanner.net/apiservices/"

#Session creation
def createSession(passengerNum, origin):
    payload = {'country': 'GB','currency': 'GBP', 'locale': 'en-GB', 'originPlace': origin, 'outboundDate' : '2017-04-07', 'adults': passengerNum , 'apiKey': 'ha728411429177864364580142296607'}

#sends request to Skyscanner API
def makeRequests:
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    r = requests.get(baseURL, headers = headers)

#origin and dest are both strings of town names and passengerNum is an integer
#Called from main
def findFlights(origin, dest, passengerNum):
    #TODO returns routes list
