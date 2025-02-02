from flask import Flask, request, jsonify, render_template
from main import spamDetection
from flask_cors import CORS
import os

app = Flask(__name__)

# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email')
    if not email:
        return jsonify({'Error': 'No email content provided'}), 400

    prediction = spamDetection(email)
    return jsonify({'result':prediction})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
