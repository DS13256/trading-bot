from flask import Flask, request, jsonify
import time
import hmac
import hashlib
import requests
import json

API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

BASE_URL = "https://api.coindcx.com"
app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(silent=True)

        print("RAW DATA:", request.data)
        print("JSON DATA:", data)

        if data is None:
            return {"status": "no json received"}, 200

        signal = data.get("signal")

        if signal == "buy":
            place_order("buy", "BTCUSDT", 0.001)

        elif signal == "sell":
            place_order("sell", "BTCUSDT", 0.001)

        return {"status": "success"}, 200

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}, 500
