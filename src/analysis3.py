import json
import re

tweets_data_path = './final/final_7.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r", encoding='utf8')

invalid_escape = re.compile(r'\\[0-7]{1,3}')  # up to 3 digits for byte values up to FF

def replace_with_byte(match):
    return chr(int(match.group(0)[1:], 8))

def repair(brokenjson):
    return invalid_escape.sub(replace_with_byte, brokenjson)

for line in tweets_file:
    try:
        line_str = json.dumps(line)
        json_acceptable_string = line_str.replace("'", "\\\"")


        line_json = json.loads(repair(json_acceptable_string))
        print(line_json)

    except:
        continue


# tweets_data_path2 = './final_racism/final_7_json.txt'
# tweets_file = open(tweets_data_path2, "r", encoding='utf8')
#
# for line in tweets_file:
#     try:
#         tweet = json.loads(repair(line))
#         if tweet['is_racism']:
#             print(tweet)
#     except:
#         continue
