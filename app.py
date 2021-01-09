from flask import Flask
from user_tweets import get_user_tweets
import json

app = Flask(__name__)

@app.route('/')
def index():
    twitter_user_id = "3291691"
    # call a function from a different file
    returned_tweets = get_user_tweets(twitter_user_id)
    returned_tweets = json.dumps(returned_tweets, indent=4, sort_keys=True)
    return returned_tweets

if __name__ == "__main__":
    app.run(debug=True)
