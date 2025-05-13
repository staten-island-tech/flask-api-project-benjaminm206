from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.weather.gov")
    weather_details = response.json()
    for weather in weather_details:
        print(weather)

""" weather = []

for weather in weather_list:
    url = weather['url']
    parts = url.strip("/").split("/")
    id = parts[-1]

    weather.append({
        'temp': weather['temp'],
        'wind-speed': weather['wind'],
        'precipitation': weather['precipitation'],
        'hourly-forcast': weather['hourly-forecast'],
        'visibility': weather['visibility'],
        'aqi': weather['air-quality-index'],
        'uv': weather['uv-index']
    })

if __name__ == '__main__':
    app.run(debug=True) """