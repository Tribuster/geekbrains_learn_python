#   3. Узнайте у пользователя число n.
#   Найдите сумму чисел n + nn + nnn.
#   Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_n = int(input("Enter a number from 0 to 9"))
print(number_n + number_n * 11 + number_n * 111)



