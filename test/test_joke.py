import unittest
from app import app
from models import JokeModel
from mongoengine.connection import _get_db


class JokeTest(unittest.TestCase):

    def setUp(self):
        # Setting up the test client
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()
        with app.app_context():
            joke_test = JokeModel(text='Knock Knock! Test Joke')
            joke_test.save()

    def test_random_joke(self):
        response = self.client.get('/joke')

        self.assertEqual(200, response.status_code)
        self.assertIn('random_joke', response.data.decode('utf-8'),
                      msg='[X] No "random_joke" key in response.')

    def test_chuck_joke(self):
        response = self.client.get('/joke/Chuck')
        self.assertEqual(200, response.status_code)
        self.assertIn('chuck_joke', response.data.decode('utf-8'),
                      msg='[X] No "chuck_joke" key in response.')

    def test_dad_joke(self):
        response = self.client.get('/joke/Dad')

        self.assertEqual(200, response.status_code)
        self.assertIn('dad_joke', response.data.decode('utf-8'),
                      msg='[X] No "dad_joke" key in response.')

    def test_post_joke(self):
        response = self.client.post(
            '/joke', data={'joke': 'Knock Knock! It\'s a joke!'})

        self.assertEqual(201, response.status_code,
                         msg='[X] No joke created.')

    def test_put_joke(self):
        response = self.client.put(
            '/joke', data={'number': 2,
                           'joke': 'Knock Knock! It\'s a joke moddified!'})

        self.assertEqual(200, response.status_code,
                         msg='[X] No joke modified.')

    def test_delete_joke(self):
        response = self.client.delete(
            '/joke', data={'number': 1})

        self.assertEqual(200, response.status_code,
                         msg='[X] No joke deleted.')

    def tearDown(self):
        # Drop the test database
        db = _get_db()
        db.drop_collection('joke_model')
        db.drop_collection('mongoengine.counters')


if __name__ == "__main__":
    unittest.main()
