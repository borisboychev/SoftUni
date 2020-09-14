
numbers = [int(x) for x in input().split()]

negative_sum = sum(filter(lambda x: x < 0 , numbers))
positive_sum = sum(filter(lambda x: x > 0 , numbers))

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")