import json
import matplotlib.pylab as plt
import csv

d = {'Normal': 0, 'Anomaly': 0}
with open("data/anomaly_label.csv") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['Label'] == 'Anomaly':
            d['Anomaly'] += 1
        else:
            d['Normal'] += 1
print(d)

with open('length_csv.txt', 'w') as file:
    file.write(json.dumps(d))


