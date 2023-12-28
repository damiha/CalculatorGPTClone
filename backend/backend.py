from flask import Flask, request, jsonify
from flask_cors import CORS

from infix_parser import parse

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    infix_str = data.get('infix_str', '')

    precedence_order = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1
    }

    result = parse(infix_str, precedence_order)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
