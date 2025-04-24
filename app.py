from flask import Flask, render_template

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
    response = requests.get(f"https://github.com/arthurkao/car-data{id}")
    data = response.json()
    
    # We extract extra details like types, height, weight, and stats.
    types = [t['type']['name'] for t in data['types']]
    model = data.get('model')
    make = data.get('make')
    brand = data.get('brand').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
    
    # Get the Pokémon’s base stats (like hp, attack, defense, etc.)
    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]
    
    # We tell Flask to show the 'pokemon.html' page with all these details.
    return render_template("pokemon.html", pokemon={
        'name': name,
        'id': id,
        'image': image_url,
        'types': types,
        'height': height,
        'weight': weight,
        'stat_names': stat_names,
        'stat_values': stat_values
    })

if __name__ == '__main__':
    app.run(debug=True)