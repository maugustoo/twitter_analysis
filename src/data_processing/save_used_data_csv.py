# Saves only the data that will be used in training the model
import csv
import json
import re

def replace_with_byte(match):
    return chr(int(match.group(0)[1:], 8))


def repair(brokenjson):
    invalid_escape = re.compile(r'\\[0-7]{1,3}')  # up to 3 digits for byte values up to FF
    return invalid_escape.sub(replace_with_byte, brokenjson)


tweets_data_path = '././final_racism/final_all1_json.txt'

with open(tweets_data_path, "r", encoding='utf8') as tweets_file, \
     open("test.csv", "w", newline='') as csv_file:

    f = csv.writer(csv_file)
    f.writerow(["text", "is_racism", "is_against"])

    for line in tweets_file:
        try:
            line_json = json.loads(repair(line))

            f.writerow([line_json['text'], line_json['is_racism'],
                       line_json['is_against']])
        except:
            print(line)
            continue
