from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from resources.joke import Joke
from resources.math import Math

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
api = Api(app)
db = MongoEngine(app)

api.add_resource(Joke, '/joke', '/joke/<string:joke_type>')
api.add_resource(Math, '/math')
