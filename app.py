from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "local-development-only"
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Healthcare Connect"
    }), 200


@app.route("/appointment", methods=["POST"])
def appointment():
    service = request.form.get("service", "").strip()

    if not service:
        return jsonify({
            "message": "Please select a healthcare service"
        }), 400

    return jsonify({
        "message": "Demo appointment request received",
        "service": service
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("APP_PORT", 5000))
    )
