with open("day5/data1.data") as f:
    fresh = []
    result1 = 0
    fresh_part = True
    for line in f.readlines():
        if line == '\n':
            fresh_part = False
            continue
        if fresh_part:
            begin, end = line.replace('\n', '').split('-')
            fresh.append((int(begin), int(end)))
        else:
            value = int(line.replace('\n', ''))
            for begin, end in fresh:
                if begin <= value <= end:
                    result1 += 1
                    break
    
    print(f'Result1 : {result1}')