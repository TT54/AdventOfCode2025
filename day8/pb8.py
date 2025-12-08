import numpy as np
import time

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

def connect(i, j, array: np.array, elements_group: dict, groups: dict[int: set]):
    array[i][j] = 1e20
    array[j][i] = 1e20
    if i in elements_group.keys() and j in elements_group.keys():
        if elements_group[i] == elements_group[j]: return
        old_value = elements_group[j]
        groups[elements_group[i]] = groups[elements_group[i]]  + groups[old_value]
        for key in groups[old_value]:
            if elements_group[key] == old_value: 
                elements_group[key] = elements_group[i]
        groups.pop(old_value)
    elif i in elements_group.keys():
        elements_group[j] = elements_group[i]
        groups[elements_group[i]].append(j)
    elif j in elements_group.keys():
        elements_group[i] = elements_group[j]
        groups[elements_group[j]].append(i)
    else:
        elements_group[i] = len(elements_group)
        elements_group[j] = elements_group[i]
        groups[elements_group[i]] = [i, j]

with open('day8/data1.data') as f:
    begin = time.time()
    boxes = []
    for line in f.readlines():
        boxes.append((int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])))
    array = np.array(calculate_distances(boxes))
    groups = {}
    elements_group = {}
    for _ in range(NUMBER_OF_PAIRS):
        argmax = np.argmin(array)
        (i, j) = (argmax // len(array), argmax % len(array))
        connect(i, j, array, elements_group, groups)

    results = [len(s) for s in groups.values()]
    results.sort()

    result1 = results[-1] * results[-2] * results[-3]

    result2 = 0
    while(len(list(groups.values())[0]) != len(boxes)):
        argmax = np.argmin(array)
        (i, j) = (argmax // len(array), argmax % len(array))
        connect(i, j, array, elements_group, groups)
        result2 = boxes[i][0] * boxes[j][0]

    print(f"Result 1 : {result1}")
    print(f"Result 2 : {result2}")
    print(time.time() - begin)