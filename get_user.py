import requests
import json

def convert_username_to_id(user_name):
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACcvKQEAAAAAeh2CeFCS9U8JFAOLqW4kI3icfrg%3Dl7dxrNDY0MdfUOIAQhFmS6jEPgcIsZ5BJyEGVtWzDfs3niaqMC'
    url = create_url(user_name)
    headers = create_headers(BEARER_TOKEN)
    json_response = connect_to_endpoint(url, headers)
    #json_response = json.dumps(json_response['data']['id'])
    print(json_response['data']['id'])


def create_url(user_name):
    usernames = "usernames="+user_name
    user_fields = "user.fields=description,created_at"
    url = "https://api.twitter.com/2/users/by?{}".format(usernames)#, user_fields) #&{}
    return url

def create_headers(BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers) 
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()