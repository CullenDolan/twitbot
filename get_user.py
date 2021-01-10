'''
This function is to convert the username to the user id that is used to search for tweets
'''
import requests
import json
import os

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
def auth():
    return os.environ.get("BEARER_TOKEN")


def convert_username_to_id(user_name):
    url = create_url(user_name)
    bearer_token = auth()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    twit_username = twit_dict_to_str(json_response)
    return twit_username
    

def twit_dict_to_str(nested_dict):
    #convert the nested dict to the string
    new_dict = nested_dict.get('data')
    twit_list = [i["id"] for i in new_dict]
    twit_username = ""  
    for ele in twit_list:  
        twit_username += ele   
    return twit_username


def create_url(user_name):
    usernames = "usernames="+user_name
    user_fields = "user.fields=description,created_at"
    url = "https://api.twitter.com/2/users/by?{}".format(usernames)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
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