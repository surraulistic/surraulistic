# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".

def check_palindrome(number):
	number_reverse = number[::-1]
	if len(number) != 4:
		print("Мне нужно 4 цифры.")
		return False
	elif number == number_reverse:
		print("Это число-палиндром!")
		return True
	else:
		print("Не палиндром.")
		return False

check_palindrome(input("4-х значное число:"))