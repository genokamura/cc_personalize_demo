import boto3
import json
import sys

# 第1引数にユーザID、第2引数に取得するランキングの件数を指定する
# ex) ユーザID: 10, 10件取得
# $ python test_recommender.py 10 10
userId = sys.argv[1]
numResults = int(sys.argv[2])

client = boto3.client(
        'personalize-runtime',
        aws_access_key_id='YOUR_ACCESS_KEY_ID',
        aws_secret_access_key='YOUR_SECRET_ACCESS_KEY'
        )

response = client.get_recommendations(
        userId=userId,
        numResults=numResults,
        recommenderArn='RECOMENDATION_ARN'
        )

for item_list in response['itemList']:
    print(item_list)

