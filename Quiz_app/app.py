# app.py
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "quiz_secret"

QUESTIONS = [
    {"question": "What is the capital of France?",
     "choices": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 2},

    {"question": "Which planet is closest to the Sun?",
     "choices": ["Venus", "Earth", "Mars", "Mercury"], "answer": 3},

    {"question": "How many sides does a hexagon have?",
     "choices": ["5", "6", "7", "8"], "answer": 1},

    {"question": "What does HTML stand for?",
     "choices": ["HyperText Markup Language", "HighText Machine Language",
                 "HyperTool Markup Logic", "HyperText Modeling Language"], "answer": 0},

    {"question": "What is 12 x 12?",
     "choices": ["132", "140", "144", "148"], "answer": 2},
]


@app.route("/")
def index():
    session["current"] = 0
    session["score"] = 0
    session["feedback"] = None
    return redirect(url_for("question"))


@app.route("/question")
def question():
    current = session.get("current", 0)
    if current >= len(QUESTIONS):
        return redirect(url_for("result"))

    q = QUESTIONS[current]
    feedback = session.pop("feedback", None)

    return render_template("index.html",
        question=q["question"],
        choices=q["choices"],
        current=current + 1,
        total=len(QUESTIONS),
        score=session.get("score", 0),
        feedback=feedback,
        percent=int((current / len(QUESTIONS)) * 100)
    )


@app.route("/answer", methods=["POST"])
def answer():
    current = session.get("current", 0)
    q = QUESTIONS[current]
    user_answer = int(request.form.get("choice"))
    correct_text = q["choices"][q["answer"]]

    if user_answer == q["answer"]:
        session["score"] = session.get("score", 0) + 1
        session["feedback"] = {"correct": True,
                                "message": "Correct! Well done.",
                                "correct_answer": correct_text}
    else:
        session["feedback"] = {"correct": False,
                                "message": "Wrong!",
                                "correct_answer": "Correct answer: " + correct_text}

    session["current"] = current + 1
    return redirect(url_for("question"))


@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(QUESTIONS)
    percent = int((score / total) * 100)

    if percent == 100:
        message = "Perfect score! You nailed it!"
    elif percent >= 60:
        message = "Good job! Keep practicing."
    else:
        message = "Keep going — you will get there!"

    return render_template("result.html", score=score, total=total, message=message)


if __name__ == "__main__":
    app.run(debug=True)