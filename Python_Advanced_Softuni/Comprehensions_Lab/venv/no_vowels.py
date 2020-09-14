vowels = ['a' , 'o' , 'u' , 'e' , 'i' , 'A' , 'O' , 'U' , 'E' , 'I']

string = input()

result = [s for s in string if s not in vowels]
print(''.join(result))