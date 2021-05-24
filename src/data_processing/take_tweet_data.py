# Routine to get the necessary data from each of the tweets and save it in a file
import json
import pandas as pd

tweets_data_path = '././to_analysi/data_users2.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        used_data = {}
        used_data['tweet_id'] = tweet['id']
        if 'retweeted_status' in tweet:
            if 'extended_tweet' in tweet['retweeted_status']:
                if 'full_text' in tweet['retweeted_status']['extended_tweet']:
                    used_data['text'] = tweet['retweeted_status']['extended_tweet']['full_text']
                else:
                    pass # i need to figure out what is possible here
        if 'quoted_status' in tweet:
            if 'extended_tweet' in tweet['quoted_status']:
                if 'full_text' in tweet['quoted_status']['extended_tweet']:
                    used_data['text'] = tweet['quoted_status']['extended_tweet']['full_text']
                else:
                    pass # i need to figure out what is possible here

        if 'extended_tweet' in tweet:
            if 'full_text' in tweet['extended_tweet']:
                used_data['text'] = tweet['extended_tweet']['full_text']
            else:
                pass # i need to figure out what is possible here

        if 'text' in tweet:
            used_data['text'] = tweet['text']

        used_data['created_at'] = tweet['created_at']
        used_data['user'] = tweet['user']['screen_name']
        already_used = False
        for data in tweets_data:
            data_json = json.loads(data)
            if data_json['text'] == used_data['text']:
                already_used = True
                break

        if not already_used:
            tweets_data.append(json.dumps(used_data))
            print(json.dumps(used_data))
    except:
        continue
