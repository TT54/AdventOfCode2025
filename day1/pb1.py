with open('day1/data1.data') as f:
    rotations: list[int] = []
    for line in f.readlines():
        rotations.append((1 if line.startswith('R') else -1) * int(line[1::]))
    
    pos = 50
    zeros = 0
    for rot in rotations:
        pos = (pos + rot) % 100
        if pos == 0: zeros += 1
    
    print("Zeros : " + str(zeros))