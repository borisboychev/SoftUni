#old code

#number_list = input().split(', ')
#result = 0
#for i in range(len(number_list)):
    #number = number_list[i+1]
    #if number < 5:
        #result *= number
    #elif number > 5 and number > 10:
        #result /= number

#print(result)

#new code
number_list = [int(x) for x in input().split(', ')]
result = 1
for number in number_list:
    if number <= 5:
        result *= number
    elif number < 5 and number <= 10:
        result /= number

print(result)
