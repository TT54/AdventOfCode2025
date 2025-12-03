import numpy as np

with open("day3/data1.data") as f:
    result1 = 0
    for line in f.readlines():
        line = line.replace('\n', '')
        max_1 = np.argmax([int(c) for c in line[:len(line) - 1]])
        max_2 = max_1 + 1 + np.argmax([int(c) for c in line[max_1 + 1:]])
        result1 += int(str(line[max_1]) + str(line[max_2]))

    f.seek(0)
    result2 = 0
    for line in f.readlines():
        line = line.replace('\n', '')
        number_str = ''
        last_max = -1
        for i in reversed(range(12)):
            last_max = last_max + 1 + np.argmax([int(c) for c in line[last_max + 1 : len(line) - i]])
            number_str += str(line[last_max])
        result2 += int(number_str)

    print(result1)
    print(result2)
