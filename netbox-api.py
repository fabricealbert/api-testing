#ref https://www.dataquest.io/blog/python-api-tutorial/

import requests
import json
import pynetbox

session = requests.Session()
session.headers = {"mycustomheader": "FA testing"}
session.verify = False




def print_json(obj):
    # create a formatted string of the Python JSON object
    text = json.dump(obj, f , indent=4)
    print(text)



nb = pynetbox.api(url="https://netbox.global.ftlprod.net/", token= "367f020ffd228e148bd3b225d4f0be4adabc2365")
nb.http_session = session

sites = nb.dcim.devices.all()
regions = nb.dcim.regions.all()
print(sites)
