#submit only function
def get_repeating_DNA(test):
    repeating = []
    for i in range(len(test)):
        if test[i:i+10] in test[i+1:]:
            if len(test[i:i+10]) == 10 and test[i:i+10] not in repeating:
                repeating.append(test[i:i+10])

    return repeating


#tests
test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)