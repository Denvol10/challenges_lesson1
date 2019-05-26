# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
word_lower = word.lower()
print(word_lower.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
word_lower = word.lower()
vovwel_letters = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
count = 0
for letters in vovwel_letters:
    count += word_lower.count(letters)
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
print(len(list_sentence))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for words in list_sentence:
    print(words[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
count_len = 0
for words in list_sentence:
    count_len += len(words)
print(count_len / len(list_sentence))