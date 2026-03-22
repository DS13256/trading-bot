from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)

        print("Webhook Received:", data)

        if not data:
            return jsonify({"error": "No data"}), 400

        signal = data.get("signal")

        return jsonify({
            "status": "success",
            "signal": signal
        }), 200

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
