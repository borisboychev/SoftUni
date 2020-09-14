def count_values(values):
    count = {}

    for v in values:
        if v not in count:
            count[v] = 1
            continue
        count[v] += 1

    return count


def print_result(values_count):
    for (k,v) in values_count.items():
        print(f"{k} - {v} times")


result = count_values(map
                      (float,
                        (input().split(' '))))
print_result(result)


