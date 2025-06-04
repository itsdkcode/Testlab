import os
from flask import Flask, request, jsonify
from get_price import get_price

app = Flask(__name__)

@app.route('/price')
def price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'symbol parameter is required'}), 400
    try:
        price = get_price(symbol)
    except Exception as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify({'symbol': symbol, 'price': price})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
