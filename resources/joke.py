import random
import json
from data.api import get_joke
from models import JokeModel
from flask_restful import Resource, reqparse


# * URL's
URL_CHUCK = "https://api.chucknorris.io/jokes/random"
URL_DAD = 'https://icanhazdadjoke.com/'


class Joke(Resource):

    def __init__(self):
        self.urls = [URL_DAD, URL_CHUCK]
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'joke_type', type=str, help='Path must be "Chuck" or "Dad"', location='view_args', default=None)
        self.reqparse.add_argument(
            'joke', type=str, help='The joke text', location='form')
        self.reqparse.add_argument(
            'number', type=int, help='The joke number', location='form')

    def get(self, joke_type: str = None) -> json:
        """Get a ramdom joke from an API url

        Returns:
            json: Joke
        """
        args = self.reqparse.parse_args()
        joke_type = args['joke_type']

        if joke_type is None:
            data = get_joke(random.choice(self.urls))
            return {'random_joke': data.get('value', data.get('joke'))}, 200
        elif str(joke_type).capitalize() == "Dad":
            data = get_joke(URL_DAD)
            return {'dad_joke': data['joke']}, 200
        elif str(joke_type).capitalize() == "Chuck":
            data = get_joke(URL_CHUCK)
            return {'chuck_joke': data['value']}, 200
        else:
            return {'error': 'The valid paths parameters are \'Dad\' or \'Chuck\''}, 404

    def post(self):
        """Create a new joke

        Args:
            joke (str): Joke text content

        Returns:
            json: 
        """
        args = self.reqparse.parse_args()

        if args['joke']:
            new_joke = JokeModel(text=args['joke'])
            new_joke.save()
            return {"message": f"Joke {new_joke['number']} added succesfully."}, 201
        return {"error": "The joke text is required."}, 400

    def put(self):
        """Update a joke

        Args:
            number (int): Joke number to update
            joke (str): Joke text content to update

        """
        args = self.reqparse.parse_args()

        if args['joke'] and args['number']:
            try:
                number = int(args['number'])
                edit_joke = JokeModel.objects(number=number).first()
                edit_joke.text = args['joke']
                edit_joke.save()
            except Exception:
                return {"error": "Please, input a valid joke number."}, 404
            return {"message": f"Joke {edit_joke['number']} modified succesfully."}, 200
        return {"error": "The joke number and joke text is required."}, 400

    def delete(self):
        """Delete a joke

        Args:
            number (int): Joke number to delete
        """
        args = self.reqparse.parse_args()

        if args['number']:
            try:
                number = int(args['number'])
                delete_joke = JokeModel.objects(number=number).delete()
                delete_joke.save()
            except Exception:
                return {"error": "Please, input a valid joke number."}, 404
            return {"message": f"Joke {number} deleted succesfully."}, 200
        return {"error": "The joke number is required."}, 400
