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
        raw = request.data.decode("utf-8")
        print("RAW DATA:", raw)

        signal = raw.lower()

        if "buy" in signal:
            place_order("buy", "BTCINR", 0.001)

        elif "sell" in signal:
            place_order("sell", "BTCINR", 0.001)

        return {"status": "success"}, 200

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}, 500
        
