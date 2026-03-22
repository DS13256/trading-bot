from flask import Flask, request, jsonify
import time
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
        
        
