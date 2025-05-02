from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get all BMW cars
    response = requests.get("https://carapi.app/api/models?make=BMW")
    if response.status_code == 200:
        cars = response.json().get("data", [])
    else:
        cars = []
    return render_template("index.html", cars=cars)

@app.route("/car/<int:id>")
def car_detail(id):
    # Get details for a specific model
    response = requests.get("https://carapi.app/api/models?make=BMW")  # Just an example URL
    if response.status_code == 200:
        car = response.json()
    else:
        car = {}

    # Dummy stats, since the API doesn't provide stats like Pokémon
    stat_names = ["Horsepower", "Weight"]
    stat_values = [
        car.get("horsepower", 0),
        car.get("weight", 0)
    ]

    return render_template("car.html", car={
        'id': car.get("id", id),
        'model': car.get("model_name", "Unknown"),
        'make': car.get("make_display", "Unknown"),
        'brand': car.get("make_display", "Unknown"),
        'year': car.get("year", "Unknown"),
        'engine': car.get("engine_type", "Unknown"),
        'horsepower': car.get("horsepower", 0),
        'weight': car.get("weight", 0),
        'image': f"https://raw.githubusercontent.com/arthurkao/car-images/main/{id}.png",
        'stat_names': stat_names,
        'stat_values': stat_values
    })

if __name__ == '__main__':
    app.run(debug=True)
