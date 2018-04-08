import requests
import json

baseURL = "http://partners.api.skyscanner.net/apiservices"
apiKey = "ha728411429177864364580142296607"

def getLocation(town):
    while True:
        url = baseURL + "/autosuggest/v1.0/UK/GBP/en-GB"
        payload = { 'query': town, 'apiKey': apiKey}
        r = requests.get(url, params=payload)
        if r.status_code == 200:
             break;
    #print(r)
    locationJson = r.text
    myjson = json.loads(locationJson)
    #print(myjson['Places'][0]['PlaceId'])
    if not myjson['Places']:
        return None
    placeId = myjson['Places'][0]['PlaceId']
    return placeId

#Session creation
def createSession(origin, dest, passengerNum):
    #adults must be between 1 and 8
    while True:
        originLoc = getLocation(origin)
        destLoc = getLocation(dest)
        if originLoc is None or destLoc is None:
            return None
        url = baseURL + "/pricing/v1.0"
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        payload = {'locationSchema': 'iata', 'country': 'UK','currency': 'GBP', 'locale': 'en-GB', 'originplace': originLoc, 'destinationplace': destLoc, 'outbounddate' : '2018-04-08', 'adults': passengerNum , 'apikey': apiKey}
        r = requests.post(url, headers=headers, data=payload)
        #print(r)
        if r.status_code == 201:
             break;
    # print(r.headers.get('Location'))
    sessionList = r.headers.get('Location').split('/')
    sessionID = sessionList[-1]
    return sessionID

def retrieveDetails(sessionID, passengerNum):
    while True:
        url = baseURL + "/pricing/v1.0/" + sessionID
        payload = {'apiKey': apiKey}
        r = requests.get(url, params=payload)
        #print(r)
        if r.status_code == 200:
             break;
        # print(r.text)
    locationJson = r.text
    myjson = json.loads(locationJson)
    legsList = myjson['Legs']
    # print(legsList)
    routes = []
    for i in range(5):
        if len(legsList) < (i + 1):
            break;
        routes.append([{'distance': None, 'time': legsList[i]['Duration'], 'vehicle': 'FLIGHT', 'passengers': passengerNum}]) #'distance': None, 'time': legsList[i]['Duration'], 'vehicle': 'Flight', 'passengers': passengerNum
    #print(routes)
    return routes



#origin and dest are both strings of town names and passengerNum is an integer
#Called from main
def findFlights(origin, dest, passengerNum):
    sessionID = createSession(origin, dest, passengerNum)
    if sessionID is None:
        return None
    routes = retrieveDetails(sessionID, passengerNum)
    return routes

#if __name__ == "__main__":
    #findFlights("Berlin", "Madrid", 2)
