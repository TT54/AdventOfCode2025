def invalid_id(id: int) -> bool:
    value = str(id)
    return value[:len(value) // 2] == value[len(value) // 2:]

with open('day2/data1.data') as f:
    input = f.readline()
    products = input.split(',')
    ids = [[i for i in range(int(product.split('-')[0]), int(product.split('-')[1]) + 1)] for product in products]
    result = sum([int(id) for l in ids for id in l if invalid_id(id)])
    print(f"Result 1 : {result}")