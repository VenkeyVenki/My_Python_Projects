from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
data = {
    "message": [
        "Win money now",
        "Limited time offer",
        "Congratulations you won a prize",
        "Hello friend",
        "Let's meet tomorrow",
        "Claim your free reward"
    ],
    "label": [
        "spam", "spam", "spam",
        "ham", "ham", "spam"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

model = MultinomialNB()
model.fit(X, y)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = vectorizer.transform([message])
    prediction = model.predict(data)[0]
    return render_template('index.html', prediction=prediction, message=message)

if __name__ == '__main__':
    app.run(debug=True)