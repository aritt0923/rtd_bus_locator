import requests
import urllib.request
import blackboxprotobuf
import base64

alerts_url = "https://www.rtd-denver.com/files/gtfs-rt/Alerts.pb"

vp_url = "https://www.rtd-denver.com/files/gtfs-rt/VehiclePosition.pb"

tu_url = "https://www.rtd-denver.com/files/gtfs-rt/TripUpdate.pb"

 
def get_vp(vp_url): #downloads raw .pb vehicle position data, returns JSON 
    vp_bytes = requests.get(vp_url).content 
    message,typedef = blackboxprotobuf.protobuf_to_json(vp_bytes)
    vp_blackbox = open("vp_bb.txt", "w")
    return vp_blackbox.write(message)
    


print(get_vp(vp_url))