from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/", methods=["GET", "POST"])
def index():

    if "number" not in session:
        session["number"] = random.randint(1, 100)

    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        number = session["number"]

        if guess > number:
            message = "Too High"
        elif guess < number:
            message = "Too Low"
        else:
            message = "Correct!"
            session.pop("number")

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)