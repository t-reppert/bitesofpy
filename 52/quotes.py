from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    for quote in quotes:
        if qid == quote['id']:
            return [quote]


def _quote_exists(existing_quote):
    """Recommended helper"""
    for i in range(len(quotes)):
        if existing_quote == quotes[i]['id']:
            return True
    return False


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify({"quotes": quotes, "status_code": 200})


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    if _quote_exists(qid):
        quote = _get_quote(qid)
        return jsonify({'quotes':quote,'status_code':200})
    abort(404)


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    if not request.json:
        abort(400)
    if not request.get_json().get('quote') or not request.get_json().get('movie'):
        abort(400)
    req = request.json
    quote = req['quote']
    movie = req['movie']
    for i in range(len(quotes)):
        if quotes[i]['quote'] == quote and quotes[i]['movie'] == movie:
            abort(400)
    new_id = len(quotes) + 1
    new_quote = {"id":new_id,"quote":quote,"movie":movie}
    quotes.append(new_quote)
    return jsonify({"quote":new_quote}), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    if not request.json:
            abort(400)
    if _quote_exists(qid):
        req = request.json
        quote = req['quote']
        movie = req['movie']
        for i in range(len(quotes)):
            if qid == quotes[i]['id']:
                if quotes[i]['quote'] == quote and quotes[i]['movie'] == movie:
                    return jsonify({'quote':quotes[i]}),200
                quotes[i]['quote'] = quote
                quotes[i]['movie'] = movie
                return jsonify({'quote':quotes[i]}),200
    abort(404)


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    if _quote_exists(qid):
        for i in range(len(quotes)):
            if quotes[i]['id'] == qid:
                del quotes[i]
                return '',204
    abort(404)
