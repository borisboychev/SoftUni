def create_sequence(n):
    if n == 0:
        print(0)
    seq = [0 , 1]
    for i in range(2 , n + 1):
        seq.append(seq[i - 2] + seq[i - 1])

    print(' '.join(str(x) for x in seq))
def locate(number):
    x, y = 0, 1
    while x < number:
        x , y = y , x + y

    if x == number:
        print('Number found')
    else:
        print('Number not found')
