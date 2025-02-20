from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/api/predictions', methods=['GET'])
def get_predictions():
    predictions = [
        {"timestamp": time.time(), "cpu_usage": round(random.uniform(0.2, 0.9), 2)}
        for _ in range(10)
    ]
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)