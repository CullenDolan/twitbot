from flask import Flask, render_template, request
from user_tweets import get_user_tweets
from get_user import convert_username_to_id

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"

    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)


@app.route('/')
def index():
    twitter_username = form_data.item()
    # pick the person, convert name to id, get the tweets
    #twitter_user_name = "chamath"
    twitter_user_id = convert_username_to_id(twitter_user_name)
    returned_tweets = get_user_tweets(twitter_user_id)
    return returned_tweets

if __name__ == "__main__":
    app.run(debug=True)
