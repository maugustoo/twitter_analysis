# Format the input text for utf8 making the text an acceptable string
import json
import re

def replace_with_byte(match):
    return chr(int(match.group(0)[1:], 8))


def repair(brokenjson):
    invalid_escape = re.compile(r'\\[0-7]{1,3}')  # up to 3 digits for byte values up to FF
    return invalid_escape.sub(replace_with_byte, brokenjson)


def repair_and_put_all(tweets_data_path):
    #tweets_data_path = '././final_racism/final_all1_json.txt'
    tweets_file = open(tweets_data_path, "r", encoding='utf8')
    for line in tweets_file:
        try:
            line_str = json.dumps(line)
            json_acceptable_string = line_str.replace("'", "\\\"")

            line_json = json.loads(repair(json_acceptable_string))
            print(line_json)

        except:
            continue


def repair_and_put_is_racism(tweets_data_path):
    #tweets_data_path = '././final_racism/final_10_json.txt'
    tweets_file = open(tweets_data_path, "r", encoding='utf8')

    for line in tweets_file:
        try:
            tweet = json.loads(repair(line))
            if tweet['is_racism']:
                print(tweet)
        except:
            continue
