with open('day1/data1.data') as f:
    rotations: list[int] = []
    for line in f.readlines():
        rotations.append((1 if line.startswith('R') else -1) * int(line[1::]))
    
    pos = 50
    zeros = 0
    zeros2 = 0
    for rot in rotations:
        sign = 1 if rot > 0 else -1
        for i in range(abs(rot)):
            pos = (pos + sign) % 100
            if pos == 0:
                zeros2 += 1
        if pos == 0:
            zeros += 1
    
    print("Result 1 : " + str(zeros))
    print("Result 2 : " + str(zeros2))