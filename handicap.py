import re
f = open('HandicapCoordinates.txt', 'r')
f_line = f.readlines()

positions = []

for x in f_line:
    long = re.search('long_wgs84: (-\d\d\.\d*)', x)
    positions.append(long.group(1))

    lat = re.search('lat_wgs84: (\d\d\.\d*)', x)
    positions.append(lat.group(1))

print(positions)
#print(len(dictionaryList))







f.close()