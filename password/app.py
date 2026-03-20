from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

def check_strength(password):
    score = 0
    if len(password) >= 8:   score += 1
    if len(password) >= 12:  score += 1
    if any(c.islower() for c in password):  score += 1
    if any(c.isupper() for c in password):  score += 1
    if any(c.isdigit() for c in password):  score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2:   return "Weak"
    elif score <= 4: return "Medium"
    else:            return "Strong"


@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()

    length       = int(data.get("length", 12))
    use_upper    = data.get("uppercase", True)
    use_lower    = data.get("lowercase", True)
    use_digits   = data.get("digits", True)
    use_symbols  = data.get("symbols", False)
    count        = int(data.get("count", 1))

    # Validate
    if length < 4 or length > 64:
        return jsonify({"error": "Length must be between 4 and 64."}), 400
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        return jsonify({"error": "Select at least one character type."}), 400
    if count < 1 or count > 10:
        return jsonify({"error": "Count must be between 1 and 10."}), 400

    # Build character pool
    pool = ""
    required = []
    if use_lower:   pool += string.ascii_lowercase;  required.append(random.choice(string.ascii_lowercase))
    if use_upper:   pool += string.ascii_uppercase;  required.append(random.choice(string.ascii_uppercase))
    if use_digits:  pool += string.digits;           required.append(random.choice(string.digits))
    if use_symbols: pool += string.punctuation;      required.append(random.choice(string.punctuation))

    passwords = []
    for _ in range(count):
        # Fill rest randomly
        rest = [random.choice(pool) for _ in range(length - len(required))]
        pwd_list = required + rest
        random.shuffle(pwd_list)
        password = "".join(pwd_list)
        passwords.append({
            "password": password,
            "strength": check_strength(password)
        })

    return jsonify({"passwords": passwords})


if __name__ == "__main__":
    app.run(debug=True, port=5001)