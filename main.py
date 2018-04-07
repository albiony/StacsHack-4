from gmaps import *
from emissions import *
from airports import findNearbyAirports

def findFlights(origin, dest, passengers):
    if origin == "St Andrews":
        return []
    return [[{'time': 60, 'distance': None, 'passengers': passengers, 'vehicle': 'FLIGHT'}]]

#Get these from the user:
origin = "St Andrews"
dest = "London"
passengers = 1

flights = findFlights(origin, dest, passengers)
if not flights:
    #One of the inputs didn't have an airport
    originAps = findNearbyAirports(origin)
    destAps = findNearbyAirports(dest)

    #For now, try the first ones:
    flights = findFlights(originAps[0], destAps[0], passengers)

    if (originAps[0].split(' ')[-1] != 'Airport'):  #A horrible hack
        originAps[0] += ' Airport'
    if (destAps[0].split(' ')[-1] != 'Airport'):  #A horrible hack
        destAps[0] += ' Airport'
    legToAp = findSingleRoute(origin, originAps[0], passengers)
    legFromAp = findSingleRoute(destAps[0], dest, passengers)
    
    flights = [legToAp + flights[0] + legFromAp]

others = findRoutes(origin, dest, passengers)

routes = flights + others

#If findflights is an empty list (or None?), use input to get nearest airport codes

for route in routes:
    for leg in route:
        leg = calculateEmissions(leg)

print (routes)