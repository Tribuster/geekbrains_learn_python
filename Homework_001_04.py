#   4. Пользователь вводит целое положительное число.
#   Найдите самую большую цифру в числе.
#   Для решения используйте цикл while и арифметические операции.

number_x = int(input("Enter a number from 0 to 9 "))
max_x = number_x % 10

while number_x > 1:
    number_x = number_x // 10
    if number_x % 10 > max_x:
        max_x = number_x % 10
    elif number_x > 9:
        pass

print("The maximum digit in a number:", max_x)



