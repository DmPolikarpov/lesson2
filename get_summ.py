num_one = input('введите первое целое число: ')
num_two = input('введите второе целое число: ')

def get_summ(num_one, num_two):
	try:
		num_one = int(num_one)
		num_two = int(num_two)
	except ValueError:
		return 'введенные данные не являются целыми числами'
	return f'Сумма данных чисел равна: {num_one + num_two}'
summ = get_summ(num_one, num_two)
print(summ) 