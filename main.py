from gmaps import *
from emissions import *

#Get these from the user:
origin = "Edinburgh"
dest = "London"
passengers = 1

routes = findRoutes(origin, dest, passengers) #+ findFlights(origin, dest, passengers)

for route in routes:
    for leg in route:
        leg = calculateEmissions(leg)

print (routes)