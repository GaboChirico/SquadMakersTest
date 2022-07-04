import mongoengine as me
import datetime

class JokeModel(me.Document):
    # TODO: Add Joke fields here.
    number = me.SequenceField()
    text = me.StringField(required=True)
    created_at = me.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return f'Joke {self.number}: {self.text}'