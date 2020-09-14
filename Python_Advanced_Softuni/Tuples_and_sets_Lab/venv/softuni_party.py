def get_not_arrived(guests , guests_arrived):
    return set(guests) - set(guests_arrived)

def print_result(result):
    print(len(result))
    result = sorted(result)
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]

n = int(input())
guests = {input() for _ in range(n)}
guests_arrived = set()

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        guests_arrived.add(guest)

result = get_not_arrived(guests , guests_arrived)
print_result(result)
