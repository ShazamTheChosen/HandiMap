import re
f = open('HandicapCoordinates.txt', 'r')
a = open("latcoord.txt", 'w')
b = open("longcoord.txt", 'w')
f_line = f.readlines()

for x in f_line:
    long = re.search('long_wgs84: (-\d\d\.\d*)', x)
    b.write(long.group(1)+"\n")

    lat = re.search('lat_wgs84: (\d\d\.\d*)', x)
    a.write(lat.group(1)+"\n")

#mMap.addMarker(new MarkerOptions().position(new LatLng(42.36,-71))
#for marker in zip(latitudes,longitudes):
 #   print("mMap.addMarker(new MarkerOptions().position(new LatLng("+str(marker[0])+','+ str(marker[1])+').title("Marker in Sydney")));')

f.close()
a.close()
b.close()