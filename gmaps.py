import requests

#origin, dest: strings, city or town names
#passengers: int, number of passengers

#returns: a list of routes, where each route is a list of steps, 
#where each step is a dictionary containing the following: 
#distance: int, distance in meters
#passengers: int, number of passengers
#time, None 
#vehicle: string, the vehicle used.
def findRoutes(origin, dest, passengers):
    payload = {'alternatives': 'true', 'origin': origin, 'destination': dest, 
        'key': 'AIzaSyA6S6OY74W3tymVCzD2jJfxGY7qdpZYx7Q', 'mode': 'transit'}    #parameters
    urlString = 'https://maps.googleapis.com/maps/api/directions/json'
    r = requests.get(urlString, params=payload)
    response= r.json()

    #Building the return list, little by little
    routes = []
    routesJson = response['routes']

    for rou in routesJson:
        route = []
        stepsJson = rou['legs'][0]['steps']
        for st in stepsJson:
            step = {}
            step['distance'] = st['distance']['value']
            step['passengers'] = passengers
            step['time'] = None
            mode = st['travel_mode']

            if mode == 'WALKING':
                step['vehicle'] = mode
            elif mode == 'BICYCLING':
                step['vehicle'] = 'BICYCLE'
            elif mode == 'DRIVING':
                step['vehicle'] = 'CAR'
            else:
                vehicle = st['transit_details']['line']['vehicle']['type']

                if (vehicle == 'HEAVY_RAIL' or vehicle == 'COMMUTER_TRAIN' or vehicle == 'RAIL' 
                    or vehicle == 'METRO_RAIL' or vehicle == 'HIGH_SPEED_TRAIN'):
                    step['vehicle'] = 'RAIL'
                elif (vehicle == 'TRAM' or vehicle == 'TROLLEYBUS'):
                    step['vehicle'] = 'TRAM'
                elif (vehicle == 'SUBWAY' or vehicle == 'BUS' or vehicle == 'FERRY' or vehicle == 'INTERCITY_BUS'):
                    step['vehicle'] = vehicle
                else:
                    step['vehicle'] = 'OTHER'

            route.append(step)
        routes.append(route)
    return routes

#Returns a single route, e.g. a list of steps
def findSingleRoute(origin, dest, passengers):
    payload = {'alternatives': 'false', 'origin': origin, 'destination': dest, 
        'key': 'AIzaSyA6S6OY74W3tymVCzD2jJfxGY7qdpZYx7Q', 'mode': 'transit'}    #parameters
    urlString = 'https://maps.googleapis.com/maps/api/directions/json'
    r = requests.get(urlString, params=payload)
    response= r.json()

    steps = []
    stepsJson = response['routes'][0]['legs'][0]['steps']
    for st in stepsJson:
            step = {}
            step['distance'] = st['distance']['value']
            step['passengers'] = passengers
            step['time'] = None
            mode = st['travel_mode']

            if mode == 'WALKING':
                step['vehicle'] = mode
            elif mode == 'BICYCLING':
                step['vehicle'] = 'BICYCLE'
            elif mode == 'DRIVING':
                step['vehicle'] = 'CAR'
            else:
                vehicle = st['transit_details']['line']['vehicle']['type']

                if (vehicle == 'HEAVY_RAIL' or vehicle == 'COMMUTER_TRAIN' or vehicle == 'RAIL' 
                    or vehicle == 'METRO_RAIL' or vehicle == 'HIGH_SPEED_TRAIN'):
                    step['vehicle'] = 'RAIL'
                elif (vehicle == 'TRAM' or vehicle == 'TROLLEYBUS'):
                    step['vehicle'] = 'TRAM'
                elif (vehicle == 'SUBWAY' or vehicle == 'BUS' or vehicle == 'FERRY' or vehicle == 'INTERCITY_BUS'):
                    step['vehicle'] = vehicle
                else:
                    step['vehicle'] = 'OTHER'

            steps.append(step)
    #print(steps)
    return steps

