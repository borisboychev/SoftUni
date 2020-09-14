def get_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(' ')


def get_count_words(file_path, words):
    words_count = {word: 0 for word in words}
    with open(file_path, 'r') as file:
        for line in file:
            words_count = count_words_in_line(line, words, words_count)
    return words_count


def count_words_in_line(line, words, words_count):
    for key_word in words:
        if key_word.lower() in line.lower():
            words_count[key_word] += 1

    return words_count

words_file_path = 'words.txt'
text_file_path = 'text.txt'

words_count = get_count_words(text_file_path , get_words(words_file_path))

for k,v in words_count.items():
    print(f'{k} : {v}')