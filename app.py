from flask import Flask, render_template
import html
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get all trivia questions
    response = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
    data = response.json()

trivia_questions = []
for item in data["results"]:
    question = {
        "question": html.unescape(item["question"]),
        "question": html.unescape(item["correct_answer"]),
        "incorrect_answers": [html.unescape(ans) for ans in item["incorrect_answer)"]],
        "category": item["category"],
        "difficulty": item["difficulty"]
    }
    trivia_questions.append(question)
if __name__ == '__main__':
    app.run(debug=True)
