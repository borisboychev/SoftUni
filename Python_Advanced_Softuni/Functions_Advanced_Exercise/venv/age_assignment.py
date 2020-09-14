def age_assignment(*args , **kwargs):
    result = {}
    for arg in args:
        result[arg] = kwargs[arg[0]]

    return result

print(age_assignment("Amy", "Bill", "Willy",  W=36, A=22, B=61))
