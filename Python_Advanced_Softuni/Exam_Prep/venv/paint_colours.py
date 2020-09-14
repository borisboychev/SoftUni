line_input = input().split(' ')

main_colours = ['red', 'yellow', 'blue']
secondary_colours = {'purple' : ['red , blue'],
                     'orange' : ['red' , 'yellow'],
                     'green' : ['blue' , 'yellow']}

colours_found = []

while line_input:

    firs_el = line_input.pop()
    second_el = ''
    if line_input:
        second_el = line_input.pop(0)

    first_comb = firs_el + second_el
    second_comb = second_el + firs_el

    if first_comb in main_colours or first_comb in secondary_colours:
        colours_found.append(first_comb)

    elif second_comb in main_colours or second_comb in secondary_colours:
        colours_found.append(second_comb)
    else:
        if len(firs_el) > 1:
            line_input.insert(len(line_input) // 2 , firs_el[:-1])
        if len(second_el) > 1:
            line_input.insert(len(line_input) // 2 , second_el[:-1])

for i in range(len(colours_found) - 1 , -1, -1):
    current = colours_found[i]
    if current in secondary_colours and  any(x not in colours_found for x in secondary_colours[current]):
        del colours_found[i]

print(colours_found)


