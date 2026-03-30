# ================================
#  app.py  —  Flask Backend
#  Uses live rates from ExchangeRate-API
#  Run: python app.py
#  Open: http://127.0.0.1:5000
# ================================


from flask import Flask, render_template, request, jsonify
import requests   # used to call the exchange rate API
#Create the Flask app
app = Flask(__name__)
#Paste your free API key here
# Get one free at: https://app.exchangerate-api.com/sign-up
API_KEY = "YOUR_API_KEY"
# List of currencies shown in the dropdown
CURRENCIES = ["USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF", "CNY", "SGD"]
#──Show the homepage ───────────────────────────────
@app.route("/")
def home():
    return render_template("index.html", currencies=CURRENCIES)
# ──Convert when user clicks the button ────────────
@app.route("/convert", methods=["POST"])
def convert():
    #Read values sent from the HTML page
    data     = request.get_json()
    amount   = float(data["amount"])
    from_cur = data["from"]
    to_cur   = data["to"]
    #Validate the amount
    if amount <= 0:
        return jsonify({"error": "Amount must be greater than 0"})
    #Call the live API to get exchange rates
    url      = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_cur}"
    response = requests.get(url)        # send request to API
    api_data = response.json()          # convert response to Python dict
    #Check if the API gave a good response
    if api_data.get("result") != "success":
        return jsonify({"error": "Could not fetch rates. Check your API key."})
    #Get rates from the API response
    rates = api_data["conversion_rates"]
    #Calculate the conversion
    rate   = rates[to_cur]
    result = round(amount * rate, 2)
    #Build a table for all currencies
    table = []
    for cur in CURRENCIES:
        if cur in rates:
            table.append({
                "currency": cur,
                "rate":     round(rates[cur], 4),
                "value":    round(amount * rates[cur], 2)
            })
    #Send result back to the HTML page
    return jsonify({
        "result": result,
        "rate":   round(rate, 4),
        "from":   from_cur,
        "to":     to_cur,
        "amount": amount,
        "table":  table
    })
if __name__ == "__main__":
    app.run(debug=True)