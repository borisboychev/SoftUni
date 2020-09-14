file_path = 'text.txt'
try:
    file = open(file_path, 'r')
    print("File found")
    while True:
        line = file.readline(14)
        if not line:
            break
except:
    print("File not found")
