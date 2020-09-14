def vowel_filter(function):
    def wrapper():
        func = function()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return [x for x in func if x in vowels]

    return wrapper


""""Test Code"""


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

# def not_vowel(function):
#     def wrapper():
#         vowels = ['a', 'u', 'e', 'i', 'o']
#         result = []
#         func = function()
#         for el in func:
#             if el not in vowels:
#                 result.append(el)
#         return result
#
#     return wrapper

# @not_vowel
# def get_letters_2():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters_2())
