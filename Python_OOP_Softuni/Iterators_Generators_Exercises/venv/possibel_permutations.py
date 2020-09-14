def possible_permutations(numbers):

    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i != j and i != k and k != j:
                    yield [i,j,k]