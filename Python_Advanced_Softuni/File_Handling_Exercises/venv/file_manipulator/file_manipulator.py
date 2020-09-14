import os

while True:
    arg = input().split('-')
    if arg[0] == 'End':
        break

    if arg[0] == 'Create':
        file_name = arg[1]
        with open(file_name, 'w') as file:
            file.write('')

    elif arg[0] == 'Add':
        file_name = arg[1]
        with open(file_name , 'a') as file:
            content = arg[2]
            file.write(content+'\n')

    elif arg[0] == 'Replace':
        file_name = arg[1]
        if os.path.exists(file_name):
            file_text = ''

            with open(file_name , 'r') as file:
                file_text = file.read()

            with open(file_name , 'w') as file:
                old_str , new_str = arg[2] , arg[3]

                file_text = file_text.replace(old_str, new_str)
                file.write(file_text)
        else:
            print('An error occured')

    elif arg[0] == 'Delete':
        file_name = arg[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occured')
