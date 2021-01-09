from get_user import convert_username_to_id
import json

def main():
    twitter_user_name = "chamath"
    twitter_user_id = convert_username_to_id(twitter_user_name)
    twitter_user_id =twitter_user_id
    twitter_user_id_plain =twitter_user_id
    

    print(twitter_user_id_plain['data'])
    
    '''print(type(twitter_user_id_plain['data']))

    json_twit_dumps = json.dumps(twitter_user_id['data'])
    print(type(json_twit_dumps))
    
    print(json_twit_dumps)'''
    


if __name__ == "__main__":
    main()