import json
import pandas as pd
#import matplotlib.pyplot as plt

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        used_data = {}
        used_data['tweet_id'] = tweet['id']
        if tweet['truncated']:
            used_data['text'] = tweet['extended_tweet']['full_text']
        else:
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
