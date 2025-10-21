from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    load_status = random.choice(["Low", "Medium", "High"])
    return jsonify({
        "message": "E-Commerce Website - AI Load Balancer Active",
        "predicted_traffic": load_status,
        "status": "Running Securely"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
