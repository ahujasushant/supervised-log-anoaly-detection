from pathlib import Path
import os

entries = Path('../../../Downloads/Hadoop/')
dir_names = []
for dir in entries.iterdir():
    if dir.is_file():
        continue
    dir_names.append(dir)
    print(dir.name)
print(dir_names[0])
for dir in dir_names:
    if '1445175094696_0005' == str(dir).split('application_')[1]:
        with open('container_1445175094696_0005_01_000001.log') as entries:
            with open('merged-normal.log', 'a+') as file:
                for log_file in entries:
                    print(log_file)
                    with open(log_file) as f:
                        for line in f:
                            file.write(line)

