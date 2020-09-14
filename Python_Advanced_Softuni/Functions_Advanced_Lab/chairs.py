def chair_combos(names, size , result = []):
    if len(result) == size:
        print(', '.join(result))
        return
    for i in range(len(names)):
        result.append(names[i])
        chair_combos(names[i+1:], size, result)
        result.pop()
    

people = input().split(', ')
chairs = int(input())

chair_combos(people, chairs)