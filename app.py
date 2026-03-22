from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Root route
@app.route("/")
def home():
    return "Server Running"

# Webhook route (POST only)
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()

        print("Webhook Received:", data)

        if not data:
            return jsonify({"error": "No data received"}), 400

        # You can process BUY/SELL here
        signal = data.get("signal")

        return jsonify({
            "status": "success",
            "received_signal": signal
        }), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
