import unittest
from app import app
from mongoengine.connection import _get_db


class MathTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_numbers(self):
        response = self.client.get('/math', query_string={'numbers': 1,
                                                          'numbers': 2,
                                                          'numbers': 3})

        self.assertEqual(200, response.status_code)

    def test_number(self):
        response = self.client.get('/math', query_string={'number': 1})

        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Drop the test database
        db = _get_db()
        db.drop_collection('joke_model')
        db.drop_collection('mongoengine.counters')


if __name__ == "__main__":
    unittest.main()
