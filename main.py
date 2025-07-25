import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "e3d4a88f2a195b0ee0e066d27cfbc79a"

account_sid = "AC46a16533590e82a4e08a1f9bea096c65"
auth_token = "dc8af91864dde23ed3f5549e0ac01a76"

weather_params = {
    "lat" : "19.190518",
    "lon" : "73.022186",
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWN_Endpoint, params= weather_params)
response.raise_for_status()
weather_data =response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "It's going to rain today. Remember to bring an ☂",
        from_ = "+13163755753" ,
        to = "+919324496003"
    )
print(message.status)






