file = open('text.txt' , 'r')

index = 0
for line in file:
    print(f"{index} : {line.strip()}")
    index+=1
    