# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

# year = int(input("Введите год:"))
# first_two = str(year)[0:2]
# century = int(first_two) + 1
# print(f"{year} год это {century} век")

#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)

mass_measure = int(input('1 - килограммы\n2 - миллиграммы\n3 - граммы\n4 - тонны\n5- - центнеры\nВыберите единицу массы:'))
match mass_measure:
	case 1:
		print(f'{float(input("Введите вес в килограммах:"))} килограмм')
	case 2:
		b = float(input("Введите вес в миллиграммах:"))
		print(f'{b * (10 ** -6)} килограмм')
	case 3:
		c = float(input("Введите вес в граммах:"))
		print(f'{c * 0.001} килограмм')
	case 4:
		d = float(input("Введите вес в тоннах:"))
		print(f'{d * 1000} килограмм')
	case 5:
		e = float(input("Введите вес в центнерах:"))
		print(f'{e * 100} килограмм')
		pass