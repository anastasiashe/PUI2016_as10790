# Imports
from __future__ import print_function
import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
##################

# Arguments
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info.py mta_key busline busline.csv")
    sys.exit()

mta_key = sys.argv[1]
busline = sys.argv[2]
buslinecsv = sys.argv[3]
##################

# Parameters
# mta_key = "11b6806c-c9bc-404b-9b10-468d9765fb46"
# busline = "B38"
# buslinecsv = "B38.csv"
##################

# Functions
def get_jsonparsed_data(url):
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)
##################


mta_url = "http://bustime.mta.info/api/siri/vehicle-monitoring." \
          "json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" % (mta_key, busline)
jsonData = get_jsonparsed_data(mta_url)

vehicleactivitieslist = jsonData["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

# counter = 0
# vehicleactivity = vehicleactivitieslist[counter]

buslinefile = open(buslinecsv, "w")
buslinefile.write("Latitude, Longitude, Stop Name, Stop Status\n")

for counter, vehicleactivity in enumerate(vehicleactivitieslist):
    vehiclelocation = vehicleactivity["MonitoredVehicleJourney"]["VehicleLocation"]
    onwcall = vehicleactivity["MonitoredVehicleJourney"]["OnwardCalls"]
    if len(onwcall) == 0:
        buslinefile.write("%f, %f, %s, %s\n" % (vehiclelocation["Latitude"], vehiclelocation["Longitude"], "N/A", "N/A"))
    else:
        nextstop = onwcall["OnwardCall"][0]
        distance = nextstop["Extensions"]["Distances"]
        buslinefile.write("%f, %f, %s, %s\n" % (vehiclelocation["Latitude"], vehiclelocation["Longitude"], nextstop["StopPointName"], distance["PresentableDistance"]))

buslinefile.close()