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
    return [quote for quote in quotes if qid == quote['id']]


def _quote_exists(existing_quote):
    """Recommended helper"""
    return [ quote for quote in quotes if quote['quote'] == existing_quote ]


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify({"quotes": quotes})


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    quote = _get_quote(qid)
    if not quote:
        abort(404)

    return jsonify({'quotes':quote})


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    if not request.json:
        abort(400)
    quote = request.json.get('quote')
    movie = request.json.get('movie')
    if not quote or not movie:
        abort(400)
    if _quote_exists(quote):
        abort(400)
    for i in range(len(quotes)):
        if quotes[i]['quote'] == quote and quotes[i]['movie'] == movie:
            abort(400)
    new_id = quotes[-1].get("id") + 1
    new_quote = {"id":new_id,"quote":quote,"movie":movie}
    quotes.append(new_quote)
    return jsonify({"quote":new_quote}), 201


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    if not request.json:
            abort(400)
    
    if len(_get_quote(qid)) != 1:
        abort(404)
        
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


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    if len(_get_quote(qid)) == 1:
        for i in range(len(quotes)):
            if quotes[i]['id'] == qid:
                del quotes[i]
                return '',204
    abort(404)
