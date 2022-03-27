from flask import Flask
from func_app import check_card_number, finding_results, read

app = Flask(__name__)

PORT = 8080
HOST = "0.0.0.0"
db = None


@app.route('/cards/<string:number_card>', methods=["GET"])
def bank_cards(number_card):
    if check_card_number(number_card):

        bin_number_card = number_card[:6]
        result = finding_results(bin_number_card, db)

        if result:
            return f"{result}", 200
        return f"No data for this BIN", 500

    return f"500 Internal Server Error", 500


if __name__ == '__main__':
    print('Считывание базы данных')
    db = read("binlist-data.csv")
    app.run(host=HOST, port=PORT)
