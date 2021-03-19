import json

d = {}
with open("/Users/sushantahuja/Downloads/HDFS_1/HDFS.log") as f:
    count = 0
    for line in f:
        count += 1
        key = [w for w in line.split() if 'blk_' in w][0]
        if key in d.keys():
            d[key].append(line)
        else:
            d[key] = [line]

blk_seq = {key: value for key, value in d.items()}
print(blk_seq.keys())

for k in blk_seq.keys():
    if k == 'blk_-7780445815029719593' or k == 'blk_2426127018694625226' or k == 'blk_3164659653171489025':
        with open('normal_blk_seq.txt', 'a+') as file:
            file.write(k + ' Normal Sequence')
            for v in blk_seq[k]:
                file.write('\n')
                file.write(json.dumps(v))
            file.write('\n----------------------------------------------------------------------------------------\n')
    elif k == 'blk_8995709096442880345' or k == 'blk_9012228938744967057':
        with open('anomaly_blk_seq.txt', 'a+') as file:
            file.write(k + ' Anomaly Sequence')
            for v in blk_seq[k]:
                file.write('\n')
                file.write(json.dumps(v))
            file.write('\n----------------------------------------------------------------------------------------\n')