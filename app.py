from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    
    # We tell Flask to show the 'index.html' page
    return render_template("index.html")

# Route for the Pokémon details page
@app.route("/car/<int:id>")
def car_detail(id):
    # We get detailed info for a specific Pokémon using its id.
    response = requests.get(f"https://www.carqueryapi.com/api/0.3/?cmd=getModel&model={id}")
    
    data = response.json()
    
    if data and 'models' in data:
        car = data['models'][0]
    # We extract extra details like types, height, weight, and stats.
        model = data.get('model')
        make = data.get('make')
        brand = data.get('brand').capitalize()
        year = data.get('year')
        engine = data.get('engine')
        horsepower = data.get('horsepower')
        weight = data.get('weight')
        image_url = f"https://raw.githubusercontent.com/arthurkao/car-images/main/{id}.png"
    
    # Get the Pokémon’s base stats (like hp, attack, defense, etc.)
    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]
    
    # We tell Flask to show the 'pokemon.html' page with all these details.
    return render_template("car.html", car={
        'id': id,
        'model': model,
        'make': make,
        'brand': brand,
        'year': year,
        'engine': engine,
        'horsepower': horsepower,
        'weight': weight,
        'image': image_url
    })

if __name__ == '__main__':
    app.run(debug=True)