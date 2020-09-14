from collections import deque

def solve():
    food_quantity = int(input())
    integer_sequence = input().split(' ')

    #find biggest order in the queue
    print(max([int(i) for i in integer_sequence]))

    integer_sequence = deque(integer_sequence)

    for _ in range(len(integer_sequence)):
        if food_quantity - int(integer_sequence[0]) >= 0:
            food_quantity -= int(integer_sequence[0])
            integer_sequence.popleft()

    if len(integer_sequence) >= 1:
        print(f"Orders left: {' '.join([str(i) for i in integer_sequence])}")
    else:
        print("Orders complete")

solve()