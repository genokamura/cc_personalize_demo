import json
import csv
import random

# schemaを読み込み
schema = open('schema.json', 'r')
loaded = json.load(schema)

# schemaからHeaderとなる部分を取得
header = ''
for value in loaded['fields']:
    header += value['name']
    header += ' '

# 1000人のユニークユーザ
user_size = 1000

# 1000種類のアイテム
item_size = 1000

# 10000件のインタラクションデータ
data_size = 10000

# eventの種別
event_types = ['View', 'Purchase']

# timestampは2021/04/01 ~ 2022/3/31までと仮定
# → 1617202800 ~ 1648652400
# ランダムなタイムスタンプでデータを作成する
start = 1617202800
end   = 1648652400

# generated_interaction_data.csvとして出力
with open('./generated_random_interaction_data.csv', 'w+') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header.split())
    for i in range(data_size):
        writer.writerow([
            str(random.randint(1, user_size)), 
            str(random.randint(1, item_size)),
            random.choice(event_types),
            random.randint(start, end)
            ])
