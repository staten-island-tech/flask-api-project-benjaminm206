from flask import Flask
import requests
import random

app = Flask(__name__)

verse_refs = [
    "john 3:16",
    "philippians 4:13",
    "psalm 23:1",
    "romans 8:28",
    "isaiah 41:10",
    "1 corinthians 13:4-7",
    "joshua 1:9",
    "proverbs 3:5-6",
    "matthew 11:28",
    "galatians 6:9"
]

@app.route("/")
def index():
    response = requests.get("https://https://bible-api.com/BOOK+CHAPTER:VERSE")
    deta = response.json()
    verse_list = data['results']

verses = []

for verse in verse_list:
    url = verse['url']
    parts = url.strip("/").split("/")
    id = parts[-1]

    verse.append({
        'text': verse['name'].capitalize(),
        'id': id,
    })

"""   return render_template("index.html, verses=verses") """

if __name__ == '__main__':
    app.run(debug=True)