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

        print("Webhook Received:", data)

        if not data:
            return jsonify({"status": "no json received"}), 200

        signal = data.get("signal")

        return jsonify({
            "status": "success",
            "signal": signal
        }), 200

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
