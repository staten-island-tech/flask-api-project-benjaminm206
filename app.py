from flask import Flask, render_template
import html
import requests

app = Flask(__name__)

@app.route("/")
def index():
    with open("mobs.json") as f:
        mobs = json.load(f)
    return render_template(index.html, mobs = mobs)

if __name__ == '__main__':
    app.run(debug=True)


