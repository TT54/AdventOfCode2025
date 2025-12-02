import re

def invalid_id(id: int) -> bool:
    value = str(id)
    return value[:len(value) // 2] == value[len(value) // 2:]

def invalid_id2(id: int) -> bool:
    value = str(id)
    return len(re.findall("^([0-9]+)\\1+$", value)) > 0

with open('day2/data1.data') as f:
    input = f.readline()
    products = input.split(',')
    ids = [[i for i in range(int(product.split('-')[0]), int(product.split('-')[1]) + 1)] for product in products]
    result1 = sum([int(id) for l in ids for id in l if invalid_id(id)])
    result2 = sum([int(id) for l in ids for id in l if invalid_id2(id)])
    print(f"Result 1 : {result1}")
    print(f"Result 2 : {result2}")