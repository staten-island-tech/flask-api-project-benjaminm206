from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    url = "https://api.weather.gov/gridpoints/MPX/107,71/forecast"
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

