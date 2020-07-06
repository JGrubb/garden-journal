import requests
import json

data = requests.get("http://wttr.in/07860", params = {"format": "j1"})

weather = data.json()
r = requests.post('http://raspberrypi.local:5000/new', 
    json={"key": "weather", 
        "value": json.dumps(weather['current_condition'][0])
        }
    )

print(r.status_code)