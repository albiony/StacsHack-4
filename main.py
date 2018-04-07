from gmaps import *
from emissions import *
from airports import findNearbyAirports

def findFlights(origin, dest, passengers):
    if origin == "St Andrews":
        return []
    return [[{'time': 60, 'distance': None, 'passengers': passengers, 'vehicle': 'FLIGHT'}]]

#Get these from the user:
origin = "Edinburgh"
dest = "London"
passengers = 1

flights = findFlights(origin, dest, passengers)
#if not flights:
    #One of the inputs didn't have an airport
    #originAps = findNearbyAirports(origin)
    #destAps = findNearbyAirports(dest)

    #For now, try the first ones:
    #findFlights(originAps[0], destAps[0], passengers)



others = findRoutes(origin, dest, passengers)

routes = flights + others

#If findflights is an empty list (or None?), use input to get nearest airport codes

for route in routes:
    for leg in route:
        leg = calculateEmissions(leg)

print (routes)