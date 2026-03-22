from flask import Flask, request
import hmac
import hashlib
import requests
import json

API_KEY = "58c46d3c4b7e893883933280ed6a17fbffafd42a7aa0d9d8"
SECRET_KEY = "a97c2a24dba565557d74f3972e1ff043374dd691c1c79a780afe5c204439e890"

BASE_URL = "https://api.coindcx.com"

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        raw = request.data.decode("utf-8")
        print("SIGNAL:", raw)

        if "buy" in raw.lower():
            print("BUY SIGNAL RECEIVED")
            place_order("buy", "BTCINR", 0.001)

        elif "sell" in raw.lower():
            print("SELL SIGNAL RECEIVED")
            place_order("sell", "BTCINR", 0.001)

        return {"status": "ok"}, 200

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}, 500


def place_order(side, market, quantity):
    try:
        endpoint = "/exchange/v1/orders/create"

        body = {
            "side": side,
            "order_type": "market_order",
            "market": market,
            "total_quantity": quantity
        }

        body_str = json.dumps(body, separators=(',', ':'))

        secret_bytes = bytes(SECRET_KEY, encoding='utf-8')
        signature = hmac.new(secret_bytes, body_str.encode(), hashlib.sha256).hexdigest()

        headers = {
            "Content-Type": "application/json",
            "X-AUTH-APIKEY": API_KEY,
            "X-AUTH-SIGNATURE": signature
        }

        response = requests.post(
            BASE_URL + endpoint,
            data=body_str,
            headers=headers
        )

        print("ORDER RESPONSE:", response.text)

        return response.json()

    except Exception as e:
        print("ORDER ERROR:", str(e))
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
