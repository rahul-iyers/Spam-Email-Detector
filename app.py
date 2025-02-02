from flask import Flask, request, jsonify
from main import spamDetection
from flask_cors import CORS

app = Flask(__name__)

#CORS(app)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email')
    if not email:
        return jsonify({'Error': 'No email content provided'}), 400

    prediction = spamDetection(email)
    return jsonify({'result':prediction})

if __name__ == '__main__':
    app.run(debug=True)
