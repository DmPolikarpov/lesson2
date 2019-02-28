
your_age = input('Сколько тебе лет: ')
your_work = ''

def variety_work(your_age):
	try:
		your_age = int(your_age)
	except ValueError:
		return 'ошибка ввода'
	if your_age < 0:
		return 'ошибка ввода'
	if your_age in range(0, 2):
		your_work = 'ты - ребенок'		
	elif your_age in range(2, 7):
		your_work = 'ты учишься в детском саду'
	elif your_age in range(7, 18):
		your_work = 'ты учишься в школе'
	elif your_age in range(18, 24):
		your_work = 'ты - студент'
	elif your_age in range(24, 65):
		your_work = 'ты работаешь'
	else:
		your_work = 'ты - пенсионер'
	return your_work

a = variety_work(your_age)
print(a)
