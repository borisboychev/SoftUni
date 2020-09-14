def get_repeating_DNA(sequence):
    repeating_dna = []
    for i in range(len(sequence)):
        if sequence[i:i+10] in sequence[i+1:]:
            if len(sequence[i:i+10]) == 10 and sequence[i:i+10] not in repeating_dna:
                repeating_dna.append(sequence[i:i+10])

    return repeating_dna


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)


test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)


test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)