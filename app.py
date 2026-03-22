from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

# ✅ Webhook endpoint (POST only)
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("Webhook Received:", data)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

# ❗ Optional: handle wrong method (GET etc.)
@app.route("/webhook", methods=["GET"])
def webhook_get():
    return "Method Not Allowed", 405

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
