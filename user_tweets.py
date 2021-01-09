'''
This is a function to get twitter data from the api and return it to a flask app
'''
import requests

def get_user_tweets(func_input):
    # main function to be called in the app.py file
    user_id = func_input
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACcvKQEAAAAAeh2CeFCS9U8JFAOLqW4kI3icfrg%3Dl7dxrNDY0MdfUOIAQhFmS6jEPgcIsZ5BJyEGVtWzDfs3niaqMC'
    pagination_token = ''
    json_response = build_full_api_call(user_id, BEARER_TOKEN, pagination_token)
    return json_response


def build_full_api_call(user_id, BEARER_TOKEN, pagination_token):
    # everything required to call the api once
    url = create_url(user_id, pagination_token)
    headers = create_headers(BEARER_TOKEN)
    params = get_params()
    return connect_to_endpoint(url, headers, params)


def create_url(user_id, pagination_token):
    # all the pieces to create the api url
    max_results = 5
    # when replies excluded, api only returns 800. when retweets are excluded, 3200 returned
    exclude = 'replies'
    if pagination_token == '':
        return "https://api.twitter.com/2/users/{}/tweets?max_results={}&exclude={}".format(user_id, max_results,exclude)
    else:
        return "https://api.twitter.com/2/users/{}/tweets?max_results={}&pagination_token={}&exclude={}".format(user_id, max_results, pagination_token, exclude)


def create_headers(BEARER_TOKEN):
    # requirements to authorize the api call
    headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}
    return headers


def get_params():
    # defined the parameters that will be requested from the api
    # https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets
    return {"tweet.fields": "created_at"}


def connect_to_endpoint(url, headers, params):
    # requesting the data with the other function data
    response = requests.request("GET", url, headers=headers, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()