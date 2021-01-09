from flask import Flask
from user_tweets import get_user_tweets
from get_user import convert_username_to_id

app = Flask(__name__)

@app.route('/')
def index():
    # pick the person
    twitter_user_name = "chamath" #'3291691'
    # convert the username to a user id
    twitter_user_id = convert_username_to_id(twitter_user_name)
    # call a function from a different file
    returned_tweets = get_user_tweets(twitter_user_id)
    #print the tweets on the page
    return returned_tweets

if __name__ == "__main__":
    app.run(debug=True)
