#FLIGHT, CAR, BICYCLE, WALKING, BUS, INTERCITY_BUS, FERRY, RAIL

#METERS
import numpy as np

co2Data = {'CAR':8.91/1609.34,
'BICYCLING':0,
'WALKING':0,
'BUS': 0.061/1609.34,
'INTERCITY_BUS':0.055/1609.34,
'FERRY':0.475/1609.34,
'RAIL':0.187/1609.34,
'TRAM':0.042/1000,
'SUBWAY':0.065/1000,
'OTHER':0}

def  calculateEmissions(seg):
    #print(seg)
    RES = None
    if seg['vehicle']=='FLIGHT':
        planeDist = (seg['time'])*14750
        multiplier = (0.1*np.exp(-0.0000004*planeDist)+0.144)/1609.34
        CO2 = multiplier*planeDist
        RES = CO2*seg['passengers']
    else:
        CO2 = co2Data[seg['vehicle']]*seg['distance']
        if seg['vehicle']=='CAR':
            RES = CO2*np.floor(1+seg['passengers']/5)
        else:
            RES = CO2*seg['passengers']
    seg['emissions'] = RES
    return seg
