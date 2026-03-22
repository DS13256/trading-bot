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
        print("SIGNAL:", raw)

        if "buy" in raw.lower():
            print("BUY SIGNAL RECEIVED")

        elif "sell" in raw.lower():
            print("SELL SIGNAL RECEIVED")

        return {"status": "ok"}, 200

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}, 500
