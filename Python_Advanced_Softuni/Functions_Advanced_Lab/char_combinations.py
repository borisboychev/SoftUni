def permutations(txt, index):
    if index >= len(txt):
        print("".join(txt))
        return
    permutations(txt, index + 1)
    for i in range(index + 1, len(txt)):
        txt[index], txt[i] = txt[i], txt[index]
        permutations(txt, index + 1)
        txt[index], txt[i] = txt[i], txt[index]



txt = list(input())
permutations(txt, 0)