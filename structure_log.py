import json
import matplotlib.pylab as plt

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
    # print(d)

length_dict = {key: len(value) for key, value in d.items()}
# print(length_dict)

with open('length.txt', 'w') as file:
     file.write(json.dumps(length_dict))

flipped = {}

for key, value in length_dict.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)

flipped_length = { key: len(value) for key, value in flipped.items() }
print(flipped_length)
#
x = flipped_length.keys()
y = flipped_length.values()
plt.plot(x, y)
# plt.show()
plt.savefig('sample-plot-1.png')
# [print(value) for key, value in d.items()]
