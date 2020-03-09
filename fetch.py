import requests
import json
import time

url = "https://coronavirus-tracker-api.herokuapp.com/all"
id = 87 # country ID

response = requests.get(url)
data = response.text

parsed = json.loads(data)

confirmed_w = repr(parsed.get("latest").get("confirmed"))
deaths_w = repr(parsed.get("latest").get("deaths"))
recovered_w = repr (parsed.get("latest").get("recovered"))


confirmed_ch = repr(parsed.get("confirmed").get("locations")[id].get("latest"))
deaths_ch = repr(parsed.get("deaths").get("locations")[id].get("latest"))
recovered_ch = repr(parsed.get("recovered").get("locations")[id].get("latest"))

print ("Confirmed Worldwide " + confirmed_w)
time.sleep (1)
print ("Deaths Worldwide " + deaths_w)
time.sleep (1)
print ("Recovered Worldwide " + recovered_w)
print ("Swiss Deaths " + deaths_ch)