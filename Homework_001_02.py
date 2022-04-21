#    2. Пользователь вводит время в секундах.
#    время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.

print('Hi, my dear!' )
name_user = input('What is your name?.. ')
print('Hello,', name_user + '!')
time_in_seconds = int(input("Write the time in seconds "))
time_hours = time_in_seconds // 3600
time_minets = (time_in_seconds - time_hours * 3600) // 60
time_seconds = (time_in_seconds - time_hours * 3600) % 60
print('Time is', str(time_hours) + ":" + str(time_minets) + ":" + str(time_seconds))
