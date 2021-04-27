with open("~/Downloads/BGL.log") as f:
    count = 0
    for line in f:
        # key = [w for w in line.split() if 'instance: ' in w]
        if 'b4b6cba0-4f87-4656-8e4d-f7e5c428ccf9' in line:
            with open('normal_1.log', 'a+') as file:
                file.write(line)
            count += 1
    print(count)
