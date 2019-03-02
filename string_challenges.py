# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = ['у','е','а','о','э','ё','я','и','ю']
s = 1
for simbol in word:
	if simbol in vowel:
		s += 1
print(s)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(' ') + 1)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*[i[0] for i in sentence.split()], sep = '\n')


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
s = 0
for i in sentence.split():
	s = s + len(i)
print(s / len(sentence.split()))


