from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

# ✅ Webhook endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()

        print("Webhook Received:", data)

        # optional: basic validation
        if not data:
            return jsonify({"error": "No data received"}), 400

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
