with open('text.txt', 'r') as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            for el in line:
                if el in '-,.!?':
                    line = line.replace(el, '@')
            words = reversed(line.split())
            print(' '.join(words))
