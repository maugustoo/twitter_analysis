import json

tweets_data_path = 'final_user.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r", encoding='utf8')

a = {'text': 'RT @sugasayajins: jaden fez um álbum de rap sem soltar palavrão nem depreciar mulheres, tem uma empresa que estimula cuidado com meio ambie…', 'is_racism': 0, 'is_against': 0}
#print(a)
#print(a['text'])


for line in tweets_file:
    line_str = json.dumps(line)
    json_acceptable_string = line_str.replace("'", "\\\"")
    json_acceptable_string = json_acceptable_string.replace("\\n", "")
    print(json_acceptable_string)

    line_json = json.loads(json_acceptable_string)
    print(line_json)
    break

for line in tweets_file:
    try:
        json.dumps(line)
        #print(line)
        #print(line['text'])
        if tweet['is_racism']:
            print (tweet)
    except:
        continue
