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
	print('Пожалуйста, задайте вопрос.\nДля завершения программы напишите "задолбал"')
	user_question = input('Пользователь: ')
	user_question = user_question.lower()
	user_question = user_question.strip()
	while user_question != 'задолбал':
		if user_question in questions:
			print(f'Программа: {questions[user_question]}')
			user_question = input('Пользователь: ')
			user_question = user_question.lower()
			user_question = user_question.strip()
		else:
			print('не правильный вопрос, попробуй еще раз')
			user_question = input('Пользователь: ')
			user_question = user_question.lower()
			user_question = user_question.strip()
	print('Пока!')
ask_user()