def count_paper_around(diagram, i, j):
    count = 0
    for (k, l) in [(u, v) for u in range(-1, 2) for v in range(-1, 2) if (u, v) != (0, 0)]:
        if i + k >= 0 and j + l >= 0 and i + k < len(diagram) and j + l < len(diagram[i + k]) and diagram[i + k][j + l] == '@':
            count += 1
    return count

with open('day4/data1.data') as f:
    diagram = [[c for c in line] for line in f.readlines()]
    result1 = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == '@' and count_paper_around(diagram, i, j) < 4:
                result1 += 1

    print(f"Result 1 : {result1}")