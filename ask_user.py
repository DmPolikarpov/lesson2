questions = {'как дела?':'хорошо!',
			 'что делаешь?':'программирую',
			 'какая погода?':'отличная',
			 'какой сегодня день недели?':'не знаю'}


def ask_user():
	user_answer = input('Как дела? ')
	while user_answer != 'хорошо':
		try:
			user_answer = input('Как дела?')
		except KeyboardInterrupt:
			print('Пока!')
			break
	print('Пожалуйста, задайте вопрос')
	user_ques = input('Пользователь: ')
	if user_ques in questions:
		print(f'Программа: {questions[user_ques]}') 
ask_user()