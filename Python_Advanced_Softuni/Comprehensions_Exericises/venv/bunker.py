categories = {product:{} for product in input().split(', ')}
n = int(input())

for _ in range(n):
    token = input().split(' - ')
    category = token[0]
    item = token[1]
    quantity = token[2].split(";")[0].split(':')[1]
    quality = token[2].split(";")[1].split(':')[1]

    categories[category][item] = (quantity , quality)

items_count = sum([sum([int(x[0]) for x in list(categories[category].values())])
          for category in categories])
average_quality = sum([sum([int(x[1]) for x in list(categories[category].values())])
          for category in categories]) / len(categories)

print(f"Count of items: {items_count}")
print(f"Average quality: {average_quality:.2f}")
[print(f"{k} -> {', '.join(v)}") for k,v in categories.items()]