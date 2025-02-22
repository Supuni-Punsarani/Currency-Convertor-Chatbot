from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

# Currency API Key 
API_KEY = "f4d90778c554f7bf0ebdd5aa"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"


@app.route("/", methods=["POST"])
def index():
    """Handles Dialogflow webhook requests"""
    data = request.get_json()

    # Extract parameters from Dialogflow
    source_currency = data["queryResult"]["parameters"]["unit-currency"]["currency"]
    amount = data["queryResult"]["parameters"]["unit-currency"]["amount"]
    target_currency = data["queryResult"]["parameters"]["currency-name"]
    print(source_currency, amount, target_currency)

    # Fetch exchange rate
    conversion_factor = fetch_conversion_factor(source_currency, target_currency)

    if conversion_factor is None:
        return jsonify({"fulfillmentText": "Sorry, I couldn't fetch the conversion rate."})

    final_amount = amount * conversion_factor
    response = {
        "fulfillmentText": f"{amount} {source_currency} is {final_amount:.2f} {target_currency}."
    }

    return jsonify(response)


def fetch_conversion_factor(source, target):
    """Fetch currency conversion factor"""
    url = f"{BASE_URL}/{source}/{target}"
    response = requests.get(url)

    if response.status_code != 200:
        return None  # Handle API errors

    data = response.json()

    if "conversion_rate" in data:
        return data["conversion_rate"]
    return None


if __name__ == "__main__":
    app.run(debug=True, port=5000)
