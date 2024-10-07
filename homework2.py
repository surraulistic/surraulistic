#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

a = int(input("1st number:"))
b = int(input("2nd number:"))

summ = a + b
diff = a - b
prod = a * b
div = a / b
div_int = a // b
div_rem = a % b
exponent = a ** b

print(f"Sum:{summ}\nDifference:{diff}\nProduct:{prod}\nDivision:{div}\nInteger:{div_int}\nDivision remainder:{div_rem}\nExponent:{exponent}")

#todo: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().

square_a = int(input("Введите число:"))
square_s = square_a ** 2
print(f"Площадь квадрата:{square_s}")

#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))

length_ac = A + B + C
length_bc = B + C
length_sum = length_ac + length_bc

print(f"AC:{length_ac}\nBC:{length_bc}\nSum:{length_sum}")

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

# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

A = int(input("A * x + B = 0. Введите коэффициент A:"))
B = int(input(f"{A} * x + B = 0. Введите коэффициент B:"))
x = -B / A
print()

# todo: 10.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 10.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.


print(not bool(int(input("A:")) % 2))  # 10.1

print(bool(int(input("A:")) % 2))  # 10.2


