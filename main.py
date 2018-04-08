from gmaps import *
from emissions import *
from airports import findNearbyAirports
from skyscanner import *

import sys

#Get these from the user:
origin = "St Andrews"
dest = "London"
passengers = 1

flights = findFlights(origin, dest, passengers)
if flights is None:
    #One of the inputs didn't have an airport
    originAps = findNearbyAirports(origin)
    destAps = findNearbyAirports(dest)

    #For now, try the first ones:
    i = -1
    while flights is None:
        i += 1
        flights = findFlights(originAps[i], destAps[i], passengers)

    if (originAps[i].split(' ')[-1] != 'Airport'):  #A horrible hack
        originAps[i] += ' Airport'
    if (destAps[i].split(' ')[-1] != 'Airport'):  #A horrible hack
        destAps[i] += ' Airport'
    legToAp = findSingleRoute(origin, originAps[i], passengers)
    legFromAp = findSingleRoute(destAps[i], dest, passengers)
    
    flights = [legToAp + flights[0] + legFromAp]

others = findRoutes(origin, dest, passengers)

routes = flights + others

#If findflights is an empty list (or None?), use input to get nearest airport codes

for route in routes:
    for leg in route:
        leg = calculateEmissions(leg)

print (routes)
sys.stdout.flush()