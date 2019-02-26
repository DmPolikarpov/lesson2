
your_age = input('Сколько тебе лет: ')

def work(your_age):
	your_work = ''
	try:
		your_age = int(your_age)		
	except ValueError:
		return 'ошибка ввода'
	if 2 <= your_age < 7:
		your_work = 'ты учишься в детском саду'
	elif 0 <= your_age < 2:
		your_work = 'ты - ребенок'
	elif 7 <= your_age < 17:
		your_work = 'ты учишься в школе'
	elif 17 <= your_age < 24:
		your_work = 'ты - студент'
	elif 24 <= your_age < 65:
		your_work = 'ты работаешь'
	else:
		your_work = 'ты - пенсионер'
	return your_work


a = work(your_age)
print(a)
