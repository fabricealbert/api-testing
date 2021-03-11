#ref https://www.dataquest.io/blog/python-api-tutorial/

import requests
import json

parameters = {
    "lat": 36.9,
    "lon": -121.9
}



response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.status_code)
print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())



pass_times = response.json()['response']
print ("Pass times")
jprint(pass_times)


risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print("Risetimes")
print(risetimes)


from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
