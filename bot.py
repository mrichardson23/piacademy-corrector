from twython import Twython
from twython import TwythonStreamer
from random import choice

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )


messages = [
	" Hello there! The correct hashtag is #Picademy.",
	" What a great tweet! Please use the hashtag #Picademy instead.",
	" I want to make sure your fellow educators see your tweets, so be sure to use the hashtag #Picademy instead.",
	" I love your enthusiasm. Join the conversation with the hashtag #Picademy (note the spelling).",
	" You've used the wrong hashtag... and that is OK. But please use #Picademy going forward.  Thanks.",
	" It seems you've got an extra 'a' in your tweet.  The correct hashtag is #Picademy"
]

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
         if 'text' in data:
             print("Received a tweet: " + data['text'])
             twitter.update_status(status="@" + data['user']['screen_name'] + choice(messages), in_reply_to_status_id=data['id'])
             
         
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
    )

stream.statuses.filter(track='#piacademy')
         
