from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form.get("city")
        lat = request.form.get("lat")
        lon = request.form.get("lon")

        if city:
            # Get location from city name
            formatted_city = city.replace(" ", "+")
            geocoding_url = f"https://nominatim.openstreetmap.org/search?q={formatted_city}&format=json"
            response = requests.get(geocoding_url, headers={"User-Agent": "weather-app"})
            location_data = response.json()[0]
            lat = location_data["lat"]
            lon = location_data["lon"]

        if lat and lon:
            # Get weather from coordinates
            point_url = f"https://api.weather.gov/points/{lat},{lon}"
            forecast_url = requests.get(point_url).json()["properties"]["forecast"]
            forecast = requests.get(forecast_url).json()
            return render_template("weather.html", forecast=forecast)

    return render_template("weather.html", forecast=None, city=city)


    try:
        response = requests.get(url)
        response.raise_for_status()
        forecast = response.json()
        return render_template("weather.html", forecast=forecast)
    except Exception as e:
        print("Error:", e)
        return render_template("weather.html", forecast=None)

if __name__ == '__main__':
    app.run(debug=True)




