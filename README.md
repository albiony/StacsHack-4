# StacsHack-4
Group project for StacsHack 4 hackathon

CO2 calculator:
module name = emissions.py
calculateEmissions(trip)
  trip: dictionary, containing the following:
    distance: float, distance in miles, used with non-flights
    passengers: int, number of passengers
    time: int, time in minutes, used with flights
    vehicle: string, the vehicle used:
      FLIGHT, CAR, BICYCLE, WALKING, BUS, INTERCITY_BUS, FERRY, RAIL
  returns: dictionary, containing the old dictionary and a parameter emissions: X inserted, where X is in a sensible unit
  
API callers:

module name = skyscanner.py
findFlights(origin, dest, passengers)
  origin, dest: strings, city or town names
  passengers: int, number of passengers
  returns: a list of routes, where each route is a list of steps, where each step is a dictionary containing the following:
    distance: None
    passengers: int, number of passengers
    time, int, time in minutes
    vehicle: string, "FLIGHT"

module name = gmaps.py
findRoutes(origin, dest, passengers)
  origin, dest: strings, city or town names
  passengers: int, number of passengers
  returns: a list of routes, where each route is a list of steps, where each step is a dictionary containing the following:
    distance: float, distance in miles
    passengers: int, number of passengers
    time, None
    vehicle: string, the vehicle used.
