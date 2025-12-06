import re

with open('day6/data1.data') as f:
    problems = []
    for line in f.readlines():
        problems.append([s for s in re.split("\\s+", line.replace('\n', '')) if len(s) > 0])
    
    result1 = 0
    for i in range(len(problems[0])):
        score = int(problems[0][i])
        for j in range(1, len(problems) - 1):
            exec("score " + problems[-1][i] + "= " + problems[j][i])
        result1 += score
    
    print(f"Result 1 : {result1}")