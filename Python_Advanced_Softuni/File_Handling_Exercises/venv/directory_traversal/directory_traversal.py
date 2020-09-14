import os

path = input()
extensions_dict = {}

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) > 1:
        continue
    for file in files:
        extension = file.split('.')[1]
        if extension not in extensions_dict:
            extensions_dict[extension] = []
        extensions_dict[extension].append(file)

result_string = ''
for key, value in sorted(extensions_dict.items()):
    result_string += f'.{key}\n'
    for file in sorted(value):
        result_string += f'- - - {file}\n'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_location = desktop + os.path.sep + 'report.txt'

with open(final_location, "w") as file:
    file.write(result_string)


