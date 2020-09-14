# file = open('write.txt' , 'w') #a - append(doesn't delete content) ,
# w - write(deletes file contant and rewrites again)

with open('write.txt', 'w') as file:
    file.write("AsdAsdASDasdAsd")
    file.writelines(["123123\n", '654\n'])
# print("asd" , file=file)

