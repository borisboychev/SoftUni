contacts = {}

text_input = input().split('-')

while len(text_input) != 1:
    name = text_input[0]
    number = text_input[1]
    contacts[name] = number
    text_input = input().split('-')

n = int(text_input[0])

for _ in range(n):
    contact_name = input()
    if contact_name in contacts:
        print(f'{contact_name} -> {contacts[contact_name]}')
    else:
        print(f'Contact {contact_name} does not exist.')
