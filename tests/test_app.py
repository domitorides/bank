import unittest
from app import app
import pandas as pd
import app as app_test

data_lists = [['45719942416578578', 'VISA', 'DEBIT', 'JCB CO.', 'USA', 53.034]]
db = pd.DataFrame(data_lists, columns=["bin", "brand", "type", "issuer", "country", "latitude"])


class TestApp(unittest.TestCase):

    def setUp(self):
        app_test.db = db
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url_cards = '/cards/'

    def test_app_incorrect_card(self):
        response = self.app.get(self.base_url_cards + '2132132456awdaw9367')
        response_text = response.data.decode()
        self.assertEqual('500 Internal Server Error', response_text)
        assert response.status_code == 500

    def test_app_correct_card(self):

        response = self.app.get(self.base_url_cards + '45719942416578578')
        assert response.status_code == 200
