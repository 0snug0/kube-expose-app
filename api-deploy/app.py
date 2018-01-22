from flask import Flask, jsonify, abort
import random, logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

coins = [
	{
		'id': 1,
		'company': 'bitcoin',
		'symbol': 'BTC',
		'price': '18378.35',

	},
	{
		'id': 2,
		'company': 'Ethereum',
		'symbol': 'ETH',
		'price': '1984.42',

	},
	{
		'id': 3,
		'company': 'Ripple',
		'symbol': 'XRP',
		'price': '4.34',
	}
]

@app.route('/', methods=['GET'])
def get_coins():
	return jsonify({'coins': coins})

@app.route('/<int:coin_id>', methods=['GET'])
def get_coin(coin_id):
	coin = [coin for coin in coins if coin['id'] == coin_id]
	if len(coin) == 0:
		abort(404)
	return jsonify({'coin': coin[0]})


if __name__ == "__main__":
    app.run(host="0.0.0.0")