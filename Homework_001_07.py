#   7 (Дополнительно). Спортсмен занимается ежедневными пробежками.
#   В первый день его результат составил a километров.
#   Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
#   Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#   Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#   Например: a = 2, b = 3.
#   Результат:
#   1-й день: 2
#   2-й день: 2,2
#   3-й день: 2,42
#   4-й день: 2,66
#   5-й день: 2,93
#   6-й день: 3,22
#   Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

result_first_day = int(input('Введите целочисленное количество километров, которое спортсмен пробежал в первый день: '))
result_overal = int(input('Введите целочисленное количество километров, которое спортсмен должен пробежать: '))
day_z = 1
while result_first_day < result_overal:
    result_first_day = result_first_day * 1.1
    day_z = day_z + 1
print("На", str(day_z) + '-й день спортсмен достиг результата - не менее', result_overal,'км')