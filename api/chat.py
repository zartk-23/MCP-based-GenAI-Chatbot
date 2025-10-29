from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '').lower()

        if 'hi' in message or 'hello' in message:
            return jsonify({'response': 'Hello! Ask me about weather or facts!'})
        elif 'weather' in message:
            return jsonify({'response': 'It\'s sunny in London! ☀️'})
        else:
            return jsonify({'response': 'I heard: ' + message})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
