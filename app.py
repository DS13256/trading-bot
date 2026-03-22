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
        data = request.get_json(force=True)
        print("Webhook Received:", data)

        signal = data.get("signal")

        # BUY
        if signal == "buy":
            place_order("buy", "BTCUSDT", 0.001)

        # SELL
        elif signal == "sell":
            place_order("sell", "BTCUSDT", 0.001)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
