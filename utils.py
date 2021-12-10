import os

# Download data from orc
def downloadData():
    os.system('git clone https://github.com/jieter/orc-data data/orc-data')


#{
# 'sailnumber': 'NED/NED8337', 'country': 'NED', 'name': 'Sweeny', 'owner': '-', 
# 'rating': {'gph': 574.8, 'osn': 559.1, 'triple_offshore': [0.9216, 1.1736, 1.3129], 
#   'triple_inshore': [0.7147, 0.9551, 1.0802]}, 
# 'boat': {
# 'builder': 'J-Boats ', 'type': 'J-111', 'designer': 'Johnson', 'year': 2011, 
# 'sizes': {'loa': 11.1, 'beam': 3.29, 'draft': 2.2, 'displacement': 4502.0, 
# 'genoa': 32.98, 'main': 39.21, 'spinnaker': 0.0, 'spinnaker_asym': 129.08, 'crew': 709.0, 
# 'wetted_surface': 26.18}}, 'vpp': {'angles': (52, 60, 75, 90, 110, 120, 135, 150), 
# 'speeds': (6, 8, 10, 12, 14, 16, 20), 52: [5.67, 6.77, 7.34, 7.55, 7.64, 7.68, 7.83], 
# 60: [6.0, 7.04, 7.51, 7.75, 7.86, 7.93, 8.09], 75: [6.28, 7.22, 7.66, 7.99, 8.26, 8.42, 8.56], 
# 90: [6.22, 7.33, 7.67, 8.03, 8.43, 8.81, 9.28], 110: [6.36, 7.47, 8.02, 8.41, 8.73, 9.07, 9.77], 
# 120: [6.22, 7.4, 7.98, 8.59, 9.12, 9.54, 10.42], 135: [5.55, 6.92, 7.66, 8.21, 8.89, 9.69, 11.57], 
# 150: [4.68, 5.87, 6.93, 7.6, 8.0, 8.44, 10.06], 'beat_angle': [42.8, 41.2, 39.4, 37.5, 37.1, 36.8, 36.8], 
# 'beat_vmg': [3.72, 4.54, 5.15, 5.39, 5.5, 5.57, 5.68], 
# 'run_angle': [143.5, 146, 149, 151.5, 149.8, 176, 142.4], 
# 'run_vmg': [4.05, 5.08, 6.0, 6.59, 6.93, 7.42, 8.72]}}


def loadData(fileName="data/orc-data/ALL2021.json"):
    with open(fileName) as f:
        data = eval(f.read())
    return data

def dataToList(data):
    boats = []
    for boat in data:
        boats.append(boat)
    return boats