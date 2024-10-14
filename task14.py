
# #todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# # Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]


# # Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# # Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# # Для числа 17 нет минимального растояния т.к элемент в массиве один.

# min_distance = dict.fromkeys(mass, [])
# def get_distance(n):
# 	if n not in min_distance:
# 		return "Key not found"
# 	for index, num in enumerate(mass):
# 		print(index, num)
# 		if num == n:
# 			min_distance[n].append(index)
# 	print(min_distance[n])
# 	min_distance[n].sort(reverse=True)
# 	if len(min_distance[n]) > 1:
# 		min_distance[n] = min_distance[n][0] - min_distance[n][1]
# 	else:
# 		min_distance[n] = 0
# 	return min_distance[n]
# print(get_distance(54))



def xx():
	for i in range(10):
		yield i
x = xx()
x = range(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))