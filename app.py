from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml")
    data = response.json()

weather = []

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

"""   return render_template("index.html, verses=verses") """

if __name__ == '__main__':
    app.run(debug=True)