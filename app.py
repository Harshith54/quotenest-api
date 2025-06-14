from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)
@app.route("/")
def home()
    return "Quotenest API is running!"

with open('quotes.json', 'r') as f:
    quotes = json.load(f)

@app.route('/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes)

@app.route('/quotes/random', methods=['GET'])
def get_random_quote():
    return jsonify(random.choice(quotes))

@app.route('/quotes/<author>', methods=['GET'])
def get_quotes_by_author(author):
    filtered = [q for q in quotes if q['author'].lower() == author.lower()]
    return jsonify(filtered)

@app.route('/quotes', methods=['POST'])
def add_quote():
    new_quote = request.get_json()
    quotes.append(new_quote)
    with open('quotes.json', 'w') as f:
        json.dump(quotes, f, indent=4)
    return jsonify({'message': 'Quote added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
