# Imports
import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
##################

# Arguments
mta_key = sys.argv[1]
busline = sys.argv[2]
##################

# Parameters
# mta_key = "11b6806c-c9bc-404b-9b10-468d9765fb46"
# busline = "B38"
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

print "Bus Line: " + busline
print "Number of Active Buses: %d" % (len(vehicleactivitieslist))

for counter, vehicleactivity in enumerate(vehicleactivitieslist):
    vehiclelocation = vehicleactivity["MonitoredVehicleJourney"]["VehicleLocation"]
    print "Bus %d is at latitude %f and longitude %f" % (
    counter, vehiclelocation["Latitude"], vehiclelocation["Longitude"])