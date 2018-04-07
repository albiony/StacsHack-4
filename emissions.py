#FLIGHT, CAR, BICYCLE, WALKING, BUS, INTERCITY_BUS, FERRY, RAIL

#METERS
import numpy as np

co2Data = {'CAR':8.91/1609.34,
'BICYCLE':0,
'WALKING':8.91/1609.34,
'BUS': 0.061/1609.34,
'INTERCITY_BUS':0.055/1609.34,
'FERRY':0.475/1609.34,
'RAIL':0.187/1609.34,
'TRAM':0.042/1000,
'SUBWAY':0.065/1000,
'OTHER':0}

#underground/metro: 0.065
#electric tram/trolley bus: 0.042

def  calculateEmissions(seg):
    if seg['vehicle']=='FLIGHT':
        planeDist = seg['time']*14750
        multiplier = (0.1*np.exp(-0.0000004*planeDist)+0.144)/1609.34
        #return multiplier
        CO2 = multiplier*planeDist
        return CO2*seg['passengers']
    else:
        CO2 = co2Data[seg['vehicle']]*seg['distance']
        if seg['vehicle']=='CAR':
            return CO2*floor(1+seg['passengers']/5)
        else:
            return CO2*seg['passengers']

#example
print calculateEmissions({'distance':1100000,'passengers':3,'time':None, 'vehicle':'FERRY'})
print calculateEmissions({'distance':None,'passengers':3,'time':60, 'vehicle':'FLIGHT'})
print calculateEmissions({'distance':250000,'passengers':1,'time':3, 'vehicle':'TRAM'})
