import re
f = open('HandicapCoordinates.txt', 'r')
f_line = f.readlines()

dictionaryList = []

for x in f_line:
    long = re.search('long_wgs84: (-\d\d\.\d*)', x)
    dictionaryList.append(long.group(1))

    lat = re.search('lat_wgs84: (\d\d\.\d*)', x)
    dictionaryList.append(lat.group(1))

#print(dictionaryList)
#print(len(dictionaryList))







f.close()