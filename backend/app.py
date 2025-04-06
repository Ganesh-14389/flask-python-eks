from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api")
def hello():
    return jsonify(message="Hello from Flask backend!")

@app.route("/health")
def health():
    return "OK", 200

@app.route("/ready")
def ready():
    return "Ready", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
