import pandas as pd


def check_card_number(number: str):
    if 16 <= len(number) <= 20 and number.isdigit():
        return True
    return False


def finding_results(bin, data):
    result = ''
    for ind, row in data.iterrows():
        if row['bin'][:6] == bin:
            result += f"BIN: {row['bin']}, Brand: {row['brand']}, Type: {row['type']}, " \
                      f"Issuer: {row['issuer']}, Country: {row['country']}, Latitude: {row['latitude']}\n"
    return result


def read(file):
    db = pd.read_csv(file)
    db = db.drop(['category', 'alpha_2', 'alpha_3', 'longitude', 'bank_phone', 'bank_url'], axis=1)
    db['bin'] = db['bin'].astype(str)
    return db
