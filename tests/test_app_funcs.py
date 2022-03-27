import unittest
import pandas as pd
from func_app import finding_results, check_card_number, read
import os


class TestAppFunc(unittest.TestCase):

    def setUp(self):
        self.data_lists = [['45719942416578578', 'VISA', 'DEBIT', 'JCB CO.', 'USA', 53.034]]
        self.data = pd.DataFrame(self.data_lists, columns=["bin", "brand", "type", "issuer", "country", "latitude"])

        dir = os.path.dirname(__file__)[:-6]
        self.file = os.path.join(dir, "binlist-data.csv")

    def test_correct_finding_results(self):
        bin_card = '457199'
        result = finding_results(bin_card, self.data)
        expect_result = f"BIN: 45719942416578578, Brand: VISA, Type: DEBIT, " \
                      f"Issuer: JCB CO., Country: USA, Latitude: {53.034}\n"
        self.assertEqual(expect_result, result)

    def test_incorrect_finding_results(self):
        bin_card = '452599'
        result = finding_results(bin_card, self.data)
        expect_result = f""
        self.assertEqual(expect_result, result)

    def test_correct_check_number(self):
        number = "45719942416578578"
        expect_res = True
        self.assertEqual(expect_res, check_card_number(number))

    def test_incorrect_check_number(self):
        number = "45719942erqe8"
        expect_res = False
        self.assertEqual(expect_res, check_card_number(number))

    def test_error_read_file(self):
        with self.assertRaises(FileNotFoundError):
            read("wekfewpfkow;rw,3po;fkw.csv")

    def test_correct_read_file(self):
        expect = type(pd.DataFrame())
        res_type = type(read(self.file))
        self.assertEqual(expect, res_type)
