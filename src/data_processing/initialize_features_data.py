# Routine to initiate the features to be labeled
import json
import pandas as pd

tweets_data_path = '././used_data/used_data_users2.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r", encoding='utf8')
for line in tweets_file:
    try:
        tweet = json.loads(line)
        used_data = {}
        used_data['text'] = tweet['text']
        used_data['is_racism'] = 0
        used_data['is_against'] = 0
        print(used_data)
    except:
        continue
