import numpy as np

with open("day3/data1.data") as f:
    result1 = 0
    for line in f.readlines():
        line = line.replace('\n', '')
        max_1 = np.argmax([int(c) for c in line[:len(line) - 1]])
        max_2 = max_1 + 1 + np.argmax([int(c) for c in line[max_1 + 1:]])
        result1 += int(str(line[max_1]) + str(line[max_2]))
    print(result1)
