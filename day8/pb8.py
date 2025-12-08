import numpy as np

NUMBER_OF_PAIRS = 1000

def distance(box1, box2):
    return (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2

def calculate_distances(boxes):
    distances = [[1e20 for _ in range(len(boxes))] for _ in range(len(boxes))]
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if i == j: continue
            distances[i][j] = distance(boxes[i], boxes[j])
            distances[j][i] = distances[i][j]
    return distances

with open('day8/data1.data') as f:
    boxes = []
    for line in f.readlines():
        boxes.append((int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])))
    array = np.array(calculate_distances(boxes))
    groups = {}
    for _ in range(NUMBER_OF_PAIRS):
        argmax = np.argmin(array)
        (i, j) = (argmax // len(array), argmax % len(array))
        array[i][j] = 1e20
        array[j][i] = 1e20
        if i in groups.keys() and j in groups.keys():
            if groups[i] == groups[j]: continue
            old_value = groups[j]
            for key in groups.keys():
                if groups[key] == old_value: 
                    groups[key] = groups[i]
        elif i in groups.keys():
            groups[j] = groups[i]
        elif j in groups.keys():
            groups[i] = groups[j]
        else:
            groups[i] = len(groups)
            groups[j] = groups[i]

    results = {}
    for key in groups.keys():
        if groups[key] in results: results[groups[key]] += 1
        else: results[groups[key]] = 1

    results = list(results.values())
    results.sort()
    
    result1 = results[-1] * results[-2] * results[-3]

    print(f"Result 1 : {result1}")