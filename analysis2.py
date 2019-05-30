import json
import pandas as pd
#import matplotlib.pyplot as plt

tweets_data_path = 'twitter_used_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r", encoding='utf8')
for line in tweets_file:
    try:
        tweet = json.loads(line)
        used_data = {}
        used_data['text'] = tweet['text']
        used_data['is_racism'] = 0
        print(used_data)
    except:
        continue
