# Task 1 #

x = int(input())
if x > 0:
	print(x+1)
if x == 0:
	print(int(10))
if x < 0:
	print(x-2)

# Task 2 #


x = int(input())
def _summ(x):
	if 10 <= x <= 99:
		digit1 = x // 10
		digit2 = x % 10
		summ = digit1 + digit2
		return summ
	else:
		return "Need a value from 10 to 99"
def _prod(x):
	if 10 <= x <= 99:
		digit1 = x // 10
		digit2 = x % 10
		product = digit1 * digit2
		return product
	else:
		return "Need a value from 10 to 99"
result1 = _summ(x)
result2 = _prod(x)
print("Sum:", result1)
print("Product:", result2)

# Task 3 #

str = "Hello world"
str1 = str[0:5]
str2 = str[6:11]
print("Первая часть " + str1)
print("Вторая часть " + str2)


"""
Дан номер месяца (1 — январь, 2 — февраль, ...).
Вывести название соответствующего времени года
("зима", "весна" и т.д.).
"""
month = int(input())
match month:
    case 1 | 2 | 12:
        print("winter")
    case 3 | 4 | 5:
        print("spring")
    case 6 | 7 | 8:
        print("summer")
    case 9 | 10 | 11:
        print("fall")
    case _:
        print("There are only 12 months in a year")
        pass
