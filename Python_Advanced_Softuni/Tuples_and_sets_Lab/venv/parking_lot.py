def solve(cars , n):
    for _ in range(n):
        (command , plate) = input().split(', ')
        if command == "IN":
            cars.add(plate)
        elif command == "OUT":
            if plate in cars:
                cars.remove(plate)

    return cars

def print_cars(cars_left):
    #if set is empty
    if len(cars_left) == 0:
        print("Parking Lot is Empty")
        return
    for i in cars_left:
        print(i)

n = int(input())
cars = set()

result = solve(cars , n)
print_cars(result)