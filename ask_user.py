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
		print(questions.get(user_question, 'не правильный вопрос, попробуй еще раз'))
		user_question = input('Пользователь: ').lower().strip()
	print('Пока!')

if __name__ == '__main__':
	ask_user()