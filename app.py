from flask import Flask, request, jsonify
import hashlib
import hmac
import time
import requests
import json
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://api.coindcx.com"

def place_order(side, symbol, amount):
    body = {
        "side": side,
        "order_type": "market_order",
        "market": symbol,
        "total_quantity": amount,
        "timestamp": int(time.time() * 1000)
    }

    json_body = json.dumps(body, separators=(',', ':'))

    signature = hmac.new(
        bytes(API_SECRET, 'utf-8'),
        bytes(json_body, 'utf-8'),
        hashlib.sha256
    ).hexdigest()

    headers = {
        'X-AUTH-APIKEY': API_KEY,
        'X-AUTH-SIGNATURE': signature,
        'Content-Type': 'application/json'
    }

    response = requests.post(
        BASE_URL + "/exchange/v1/orders/create",
        data=json_body,
        headers=headers
    )

    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    result = place_order(
        data["action"],
        data["symbol"],
        data["amount"]
    )

    return jsonify(result)

@app.route('/')
def home():
    return "Bot is running 🚀"
