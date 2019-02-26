school_scores = [{'school_class':'4a', 'scores':[3,4,4,5,2]},
				 {'school_class':'5a', 'scores':[4,5,5,2,4]},
				 {'school_class':'6b', 'scores':[2,3,5,5,5]},
				 {'school_class':'8e', 'scores':[4,5,5,4,2]},
				 {'school_class':'9v', 'scores':[2,2,3,5,5]}]
average_value = 0
average_value_school = 0
for i in range(len(school_scores)):
	sum_class = 0
	for score in school_scores[i]['scores']:
		sum_class += score
	average_value = sum_class/len(school_scores[i]['scores'])
	class_number = school_scores[i]['school_class']
	print(f'средний балл в классе {class_number}: {average_value}')
	average_value_school += average_value
print(f'средний балл по школе: {average_value_school/len(school_scores)}') 
