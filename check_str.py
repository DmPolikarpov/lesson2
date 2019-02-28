first = input()
second = input()

def check_str(first, second):
	if isinstance(first, str) and isinstance(second, str):
		if first == second:
			return 1
		elif first != second and len(first) > len(second):
			return 2
		elif first != second and second == 'learn':
			return 3
	else:
		return 0
a = check_str(first, second)
print(a)