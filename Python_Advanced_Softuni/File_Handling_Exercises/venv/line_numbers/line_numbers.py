result_txt = ''
with open('text.txt' , 'r') as file:
    for (i,l) in enumerate(file):
        length = len([el for el in l if el.isalpha()])
        count = 0

        for el in l:
            if el in "',.?!\":-":
                count += 1

        result_txt += f'Line {i + 1}: {l[:-2]} ({length})({count})\n'

with open('output.txt' , 'w') as outputfile:
    outputfile.write(result_txt)
