import re

with open('day6/data1.data') as f:
    problems = []
    lines = []
    for line in f.readlines():
        problems.append([s for s in re.split("\\s+", line.replace('\n', '')) if len(s) > 0])
        lines.append(line.replace('\n', ''))
    
    result1 = 0
    for i in range(len(problems[0])):
        score = int(problems[0][i])
        for j in range(1, len(problems) - 1):
            exec("score " + problems[-1][i] + "= " + problems[j][i])
        result1 += score
    
    result2 = 0
    cursor = len(lines[0])
    numbers = []
    while cursor > 0:
        cursor -= 1
        number = ''
        for i in range(len(lines) - 1):
            number = number + lines[i][cursor] if lines[i][cursor] != ' ' else number
        
        if number == '':
            continue

        numbers.append(number)

        if lines[-1][cursor] != ' ':
            score = int(numbers[0])
            for i in range(1, len(numbers)):
                exec("score " + lines[-1][cursor] + '= ' + numbers[i])
            result2 += score
            numbers.clear()

    
    print(f"Result 1 : {result1}")
    print(f"Result 2 : {result2}")