import json
import csv
import random
import sys

# 第1引数に取得するデータのファイル名を指定する
# ここではsushi3a.5000.10.orderを利用することを前提とする
#
# アイテムの種類は以下の10種類
# 0:えび      1:穴子      2:まぐろ    3:いか      4:うに
# 5:いくら    6:玉子      7:とろ      8:鉄火巻    9:かっぱ巻  
# 
# eventの種別は"View"と"Purchase"
# 各ユーザのランキングの上位2アイテムについて"Purchase"
# 3~5位のアイテムについて"View"イベントが発生したものとして学習用データを生成する
event_types = ['View', 'Purchase']
#
# タイムスタンプについてはランダムなタイムスタンプでデータを作成することとする
# 2021/04/01 ~ 2022/3/31まで→ Epoch秒で1617202800 ~ 1648652400
start = 1617202800
end   = 1648652400
# 
# 以下、https://www.kamishima.net/sushi/ より
# ◆◇◆ sushi3a.5000.10.order / sushi3b.5000.10.order ◆◇◆
# 
# それぞれ，アイテム集合A と B に対する嗜好を利用者に順位法で質問した結果
# 
# - 先頭のヘッダ行
#  <アイテムの総数 |X*|><sp>1<nl>
# 
# |X*| は，sushi3a.5000.10.order では10，sushi3b.5000.10.order では100
# 
# - 本体以降
# 各行が sushi3.udata の各行の利用者に対応
#  0<sp><順序長 |Xi|><sp><1番目のアイテムID>....<|Xi|番目のアイテムID><nl>
# 
# アイテムは最も好きなものから順に整列
# 
# <sp>:空白(0x20)
# <nl>:改行(0x0a)
# 
filename = sys.argv[1]

# ファイル全体を文字列として読み込み
with open(filename) as f:
    data = f.read()

# 読み込んだデータを行ごとに配列に格納
lines = data.split('\n')
# header行を削除
lines.pop(0)

# 学習用データに書き込むためのデータ
csv_data = []

# データを生成
for i in range(len(lines) - 1):
    # USER_IDは行数
    user_id = i + 1
    # space区切りの3~4番目の要素がランキングの1~2位, 5~7番目の要素が3~5位
    line = lines[i].split(' ')
    # 1~2位
    csv_data.append([
        str(user_id),
        str(line[2]),
        event_types[1],
        random.randint(start, end)
        ])
    csv_data.append([
        str(user_id),
        str(line[3]),
        event_types[1],
        random.randint(start, end)
        ])
    # 3~5位
    csv_data.append([
        str(user_id),
        str(line[4]),
        event_types[0],
        random.randint(start, end)
        ])
    csv_data.append([
        str(user_id),
        str(line[5]),
        event_types[0],
        random.randint(start, end)
        ])
    csv_data.append([
        str(user_id),
        str(line[6]),
        event_types[0],
        random.randint(start, end)
        ])

# schemaを読み込み
schema = open('schema.json', 'r')
loaded = json.load(schema)

# schemaからHeaderとなる部分を取得
header = ''
for value in loaded['fields']:
    header += value['name']
    header += ' '

# generated_sushi_interaction_data.csvとして出力
with open('./generated_sushi_interaction_data.csv', 'w+') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header.split())
    for i in range(len(csv_data)):
        writer.writerow(csv_data[i])

