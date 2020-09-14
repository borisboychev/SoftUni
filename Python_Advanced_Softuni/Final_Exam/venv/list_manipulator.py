def list_manipulator(*args):
    num_list = list(args[0])
    command = args[1]

    if command == 'add':
        sub_command = args[2]
        nums_to_add = list(args[3:])
        nums_to_add.sort()

        for i in range(len(nums_to_add)):
            if sub_command == 'end':
                num_list.append(nums_to_add[i])
            elif sub_command == 'beginning':
                num_list.insert(i , nums_to_add[i])

    elif command == 'remove':
        sub_command = args[2]
        if len(args) > 3:
            nums_to_remove = args[3]
            if sub_command == 'end':
                for i in range(int(nums_to_remove)):
                    num_list.pop()
            else:
                del num_list[:nums_to_remove]

        else:
            if sub_command == 'end':
                del num_list[-1]
            else:
                del num_list[0]

    return num_list




print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))




print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))