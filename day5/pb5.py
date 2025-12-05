def union(begin, end, l:list) -> list:
    new_list = []
    begin_inserted = False
    end_inserted = False
    for i in range(len(l)):
        element, is_begin = l[i]
        if element < begin:                             # Cas < begin
            new_list.append((element, is_begin))
        elif element == begin:                          # Cas = begin
            begin_inserted = True
            if is_begin: new_list.append((begin, True))
        else:                                           # Cas > begin
            if not begin_inserted:
                begin_inserted = True
                if is_begin: new_list.append((begin, True))
            
            if element < end:                           # Cas < end
                # On ne fait rien
                ...
            elif element == end:                        # Cas = end
                end_inserted = True
                if not is_begin: new_list.append((end, False))
            else:                                       # Cas > end
                if not end_inserted:
                    end_inserted = True
                    if is_begin: new_list.append((end, False))
                
                new_list.append((element, is_begin))

    if not begin_inserted:
        new_list.append((begin, True))
    
    if not end_inserted:
        new_list.append((end, False))

    return new_list
    

with open("day5/data1.data") as f:
    fresh = []
    result1 = 0
    fresh_part = True
    for line in f.readlines():
        if line == '\n':
            fresh_part = False
            continue
        if fresh_part:
            begin, end = line.replace('\n', '').split('-')
            fresh.append((int(begin), int(end)))
        else:
            value = int(line.replace('\n', ''))
            for begin, end in fresh:
                if begin <= value <= end:
                    result1 += 1
                    break

    fresh_list = []
    for begin, end in fresh:
        fresh_list = union(begin, end, fresh_list)

    result2 = 0
    for i in range(0, len(fresh_list), 2):
        result2 += fresh_list[i + 1][0] - fresh_list[i][0] + 1
                
    print(f'Result1 : {result1}')
    print(f'Result2 : {result2}')