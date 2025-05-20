from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    forecast = None #Initializing an empty value to soon be filled
    city = None
    condition = None
    if request.method == "POST": #sending data to API
        city = request.form.get("city") #gets the city via the form on the index
        formatted_city = city.replace(" ", "+") #removes spaces for URL
        geocoding_url = f"https://nominatim.openstreetmap.org/search?q={formatted_city}&format=json" #takes the city and converts it into latitude and longitude
        response = requests.get(geocoding_url, headers={"User-Agent": "weather-app"})
        location_data = response.json()[0]
        lat = location_data["lat"] #latitude
        lon = location_data["lon"] #longitude

    if lat and lon:
        points_url = f"https://api.weather.gov/points/{lat},{lon}"
        points_response = requests.get(points_url).json()["properties"]
    
        forecast_url = points_response["forecast"]
        hourly_url = points_response["forecastHourly"]

        forecast = requests.get(forecast_url).json()
        hourly = requests.get(hourly_url).json()

        current_temp = forecast["properties"]["periods"][0]["temperature"]

        condition = forecast['properties']['periods'][0]['shortForecast'].lower()

    return render_template("weather.html", forecast=forecast, hourly=hourly, city=city, current_temp=current_temp)



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




