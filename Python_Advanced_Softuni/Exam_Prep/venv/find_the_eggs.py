def find_strongest_eggs(*args):
    eggs = args[0]
    sub_list_count = args[1]
    sub_lists = []
    best_eggs = []

    for _ in range(sub_list_count):
        sub_lists.append([])

    for i in range(len(sub_lists)):
        sub_lists[i] = [eggs[index] for index in range(i , len(eggs) , sub_list_count)]

    for sub_list in sub_lists:
        mid_el = sub_list[len(sub_list) // 2]
        left_el = sub_list[len(sub_list) // 2 - 1]
        right_el = sub_list[len(sub_list) // 2 + 1]

        if left_el < mid_el > right_el > left_el:
            best_eggs.append(mid_el)

    return best_eggs




test = ([-1,7,3,15,2,12] , 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))