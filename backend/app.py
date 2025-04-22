from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/count_sort_dates', methods=['POST'])
def count_sort_dates():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_names', methods=['POST'])
def count_sort_names():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_id', methods=['POST'])
def count_sort_id():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_tweet', methods=['POST'])
def count_sort_tweet():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_replies', methods=['POST'])
def count_sort_replies():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_retweets', methods=['POST'])
def count_sort_retweets():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_likes', methods=['POST'])
def count_sort_likes():
    x = 2
    return jsonify({"result": x})

@app.route('/count_sort_quotes', methods=['POST'])
def count_sort_quotes():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_dates', methods=['POST'])
def heap_sort_dates():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_names', methods=['POST'])
def heap_sort_names():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_id', methods=['POST'])
def heap_sort_id():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_tweet', methods=['POST'])
def heap_sort_tweet():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_replies', methods=['POST'])
def heap_sort_replies():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_retweets', methods=['POST'])
def heap_sort_retweets():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_likes', methods=['POST'])
def heap_sort_likes():
    x = 2
    return jsonify({"result": x})

@app.route('/heap_sort_quotes', methods=['POST'])
def heap_sort_quotes():
    x = 2
    return jsonify({"result": x})

if __name__ == '__main__':
    app.run(debug=True)
