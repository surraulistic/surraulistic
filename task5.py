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
