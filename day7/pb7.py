def forward(room):
    for depth in range(len(room) - 1):
        for j in range(len(room[depth])):
            if room[depth][j] < 0:
                if room[depth + 1][j] != 1:
                    room[depth + 1][j] += room[depth][j]
                else:
                    room[depth + 1][j + 1] += room[depth][j]
                    room[depth + 1][j - 1] += room[depth][j]
    return -sum([i for i in room[-1]])

with open("day7/data1.data") as f:
    room = []
    for line in f.readlines():
        l = [(0 if c == '.' else (1 if c == '^' else -1)) for c in line.replace('\n', '')]
        room.append(l)
    
    result2 = forward(room)

    result1 = 0
    for i in range(len(room) - 1):
        for j in range(len(room[i])):
            if room[i][j] == -1:
                if room[i + 1][j] == 0: room[i + 1][j] = -1
                elif room[i + 1][j] == 1:
                    room[i + 1][j + 1] = -1
                    room[i + 1][j - 1] = -1
                    result1 += 1
    
    print(f'Result 1 : {result1}')
    print(f'Result 2 : {result2}')