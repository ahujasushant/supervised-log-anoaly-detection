import csv
import json

d = {}
with open("data/HDFS.log") as f:
    count = 0
    for line in f:
        count += 1
        # if count > 100: break
        key = [w for w in line.split() if 'blk_' in w][0]
        if key in d.keys():
            d[key].append(line)
        else:
            d[key] = [line]

length_dict = {key: len(value) for key, value in d.items()}
a = {}
with open("data/anomaly_label.csv") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['Label'] == 'Anomaly' and row['BlockId'] in length_dict:
            a[row['Label'] + ' ' + row['BlockId']] = length_dict[row['BlockId']]

print(a)

n = {}
with open("data/anomaly_label.csv") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['Label'] == 'Normal' and row['BlockId'] in length_dict:
            n[row['Label'] + ' ' + row['BlockId']] = length_dict[row['BlockId']]

print(n)

with open('normal.txt', 'w') as file:
    file.write(json.dumps(n))

with open('anomaly.txt', 'w') as file:
    file.write(json.dumps(a))
