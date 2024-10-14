#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))

length_ac = A + B + C
length_bc = B + C
length_sum = length_ac + length_bc

print(f"AC:{length_ac}\nBC:{length_bc}\nSum:{length_sum}")