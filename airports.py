import requests

#Takes an address and returns an airport code string
def findNearbyAirports(address):
    payload = {'address': address, 'key': 'AIzaSyCtPHcJxNLUbND4udbOtli5cra3CqhZ4xc'}    #parameters
    urlString = 'https://maps.googleapis.com/maps/api/geocode/json'
    r = requests.get(urlString, params=payload)
    response = r.json()
    loc = response['results'][0]['geometry']['location']
    return getAirportCode(loc['lat'], loc['lng'])

def getAirportCode(lon, lat):
    #Make a POST-requests
    postString = 'https://api.lufthansa.com/v1/oauth/token'
    postParams = {'client_id' : 'x4jvdk4hqnfgru4akpxfeemp', 'client_secret' : 'EY3gUyyq3M', 'grant_type': 'client_credentials'}
    r = requests.post(postString, data=postParams)
    response = r.json()
    token = response['access_token']
    
    urlString = 'https://api.lufthansa.com/v1/references/airports/nearest/' + str(lon) + "," + str(lat)
    authStr = 'Bearer ' + token
    headers = {'Authorization': authStr, 'Accept': 'application/json'}
    r = requests.get(urlString, headers=headers)
    response = r.json()

    airports = response['NearestAirportResource']['Airports']['Airport']
    #print(airports)
    #print()
    apnames = []
    for i, ap in enumerate(airports):
        names = airports[i]['Names']['Name']
        if type(names) is dict:
            #print(names)
            apnames.append(name['$'])
        else:
            for name in names:
                #print(name)                
                if name['@LanguageCode'] == 'en':
                    apnames.append(name['$'])
    return apnames

#print(findNearbyAirports('St Andrews'))