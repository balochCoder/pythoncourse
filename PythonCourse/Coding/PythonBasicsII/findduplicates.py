some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate_list =[]
for x in some_list:
    if some_list.count(x) > 1:
        if x not in duplicate_list:
           duplicate_list.append(x)
print(duplicate_list)