# StacsHack-4
Group project for StacsHack 4 hackathon

CO2 calculator:
calculateEmissions(trip)
  trip: a dictionary containing the following:
    distance: distance in miles, used with non-flights
    time: time in seconds, used with flights
    vehicle: a string of the vehicle used:
      FLIGHT, CAR, BICYCLE, WALKING, BUS, INTERCITY_BUS, FERRY, RAIL
  returns: the same dictionary, with a parameter emissions: X inserted, where X is in a sensible unit
