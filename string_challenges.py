# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
format_word = word.lower()
print(format_word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = ['у','е','а','о','э','ё','я','и','ю']
format_word = word.lower()
s = 0
for simbol in format_word:
	if simbol in vowel:
		s += 1
print(s)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*[i[0] for i in sentence.split()], sep = '\n')


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
s = 0
for i in sentence.split():
	s = s + len(i)
print(s / len(sentence.split()))
