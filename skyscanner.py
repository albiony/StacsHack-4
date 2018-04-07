import requests
import json

baseURL = "http://partners.api.skyscanner.net/apiservices"
apiKey = "ha728411429177864364580142296607"

def getLocation(town):
    #TODO search for location by name, retrieve id, country
    url = baseURL + "/autosuggest/v1.0/UK/GBP/en-GB"
    payload = { 'query': town, 'apiKey': apiKey}
    r = requests.get(url, params=payload)
    print(r)
    # print(r.text)
    locationJson = r.text
    myjson = json.loads(locationJson)
    # print(myjson['Places'][0]['PlaceId'])
    placeId = myjson['Places'][0]['PlaceId']
    return placeId

#Session creation
def createSession(origin, dest, passengerNum):
    #adults must be between 1 and 8
    originLoc = getLocation(origin)
    destLoc = getLocation(dest)
    url = baseURL + "/pricing/v1.0"
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    payload = {'locationSchema': 'iata', 'country': 'UK','currency': 'GBP', 'locale': 'en-GB', 'originplace': originLoc, 'destinationplace': destLoc, 'outbounddate' : '2018-09-07', 'adults': passengerNum , 'apikey': apiKey}
    r = requests.post(url, headers=headers, data=payload)
    print(r)
    print(r.headers.get('Location'))
    sessionList = r.headers.get('Location').split('/')
    sessionID = sessionList[-1]
    return sessionID

def retrieveDetails(sessionID):
    # TODO
    url = baseURL + "/pricing/v1.0/" + sessionID
    payload = {'apiKey': apiKey}
    r = requests.get(url, params=payload)
    print(r)
    print(r.text)



#origin and dest are both strings of town names and passengerNum is an integer
#Called from main
def findFlights(origin, dest, passengerNum):
    sessionID = createSession(passengerNum, origin, 2)
    retrieveDetails(sessionID)

#used for testing
def main():
    findFlights("Berlin", "Madrid", 2)

if __name__ == "__main__":
    main()
