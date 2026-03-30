Currency Converter — Use an exchange rate API to convert between currencies.

Project structure:
Currency_converter/
├── app.py
├── requirements.txt
└── templates/
    └── index.html

Steps to run:
# 1. Install Flask
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open in browser
http://127.0.0.1:5000


What it does:

1.Enter any amount and pick a From / To currency
2.Shows the converted result with the live exchange rate
3.Displays a table of the same amount converted to 10 common currencies (USD, EUR, GBP, JPY, INR, etc.)
Uses the free ExchangeRate-API — no API key needed!

How to get a free key:

1.Go to exchangerate-api.com
2.Sign up — no credit card needed
3.Copy your API key from the dashboard

Then update one line in app.py:

To run:

1.Open the file in any text editor
2.Replace YOUR_API_KEY_HERE with your free key
3.Double-click the file to open in browser — done! 

How they talk to each other:
User clicks Convert
      ↓
index.html  →  sends amount, from, to  →  app.py (/convert)
                                               ↓
                                         Python calculates
                                               ↓
index.html  ←  gets result, rate, table  ←  app.py
      ↓
Shows result instantly ⚡

You need to add your real API key! Here's exactly what to do:
Get your free API key:

1.Go to 👉 app.exchangerate-api.com/sign-up
2.Enter your email and sign up (free, no credit card)
3.You'll see your API key on the dashboard — looks like this:

Done! Here's the full picture:
How it works:
Browser (HTML)
    ↓  clicks Convert
Flask (app.py)
    ↓  calls live API
ExchangeRate-API
    ↓  returns rates
Flask (app.py)

Finally the output will be caluculated and display 

    ↓  calculates & sends back
Browser (HTML)
    ↓  shows result + table
