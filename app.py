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
    current_temp = None
    hourly = None
    
    if request.method == "POST": #sending data to API
        city = request.form.get("city") #gets the city via the form on the index
        formatted_city = city.replace(" ", "+") #removes spaces for URL
        geocoding_url = f"https://nominatim.openstreetmap.org/search?q={formatted_city}&format=json" #takes the city and converts it into latitude and longitude
        response = requests.get(geocoding_url, headers={"User-Agent": "weather-app"})
        location_data = response.json()[0] #Location data = the response the API returns back -> as a list (json)
        lat = location_data["lat"] #latitude
        lon = location_data["lon"] #longitude

        #Imputting lat and lon into weather API
        points_url = f"https://api.weather.gov/points/{lat},{lon}"
        #Getting response containing location of the URL's for the weather data 
        points_response = requests.get(points_url).json()["properties"]
        # Extracting the URL's for the forecast using the lat and lon
        forecast_url = points_response["forecast"]
        hourly_url = points_response["forecastHourly"]
        details_url = points_response["forecastGridData"]
        # Fetching the weather data from each URL
        forecast = requests.get(forecast_url).json()
        hourly = requests.get(hourly_url).json()
        details = requests.get(details_url).json()
        # Fetching data for the hourly forecast
        current_temp = hourly["properties"]["periods"][0]["temperature"]

    return render_template("weather.html", forecast=forecast, hourly=hourly, details=details, city=city, current_temp=current_temp)

if __name__ == '__main__':
    app.run(debug=True)