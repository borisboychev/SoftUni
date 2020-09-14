class ValueCannotBeNegative(Exception):
    def __init__(self, value):
        msg = f'{value} is negative'
        super(ValueCannotBeNegative, self).__init__(msg)

for _ in range(5):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegative(x)
