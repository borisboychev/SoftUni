countries = input().split(', ')
cities = input().split(', ')

capitals = {x[0]:x[1] for x in zip(countries , cities)}

[print(f'{key} -> {value}') for key,value in capitals.items()]