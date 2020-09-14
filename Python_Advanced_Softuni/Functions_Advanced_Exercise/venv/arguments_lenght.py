def args_length(*args):
    args_list = []
    for i in args:
        args_list.append(i)

    return len(args_list)


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
