#   5. Запросите у пользователя значения выручки и издержек фирмы.
#   Определите, с каким финансовым результатом работает фирма.
#   Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#   Выведите соответствующее сообщение.
#   6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#   Это отношение прибыли к выручке.
#   Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue_company = float(input("Enter revenue value "))       #   выручка компании
costs_company = float(input("Enter cost value "))        #   издержки компании
financial_results = revenue_company - costs_company        #   прибыль компании

if (financial_results > 0.0):
    print("Вы в прибыли на", financial_results, 'средств. Поздравляем!')
    profitability = (financial_results / revenue_company)
    print('Рентабильность составила', profitability)
    number_of_employees = int(input("Введите число сотрудников вашей фирмы "))
    revenue_company_employees = financial_results / number_of_employees
    print("Прибыль на одного сотрудника фирмы составила", revenue_company_employees, 'средств.')

elif (financial_results < 0.0):
    print('Вы поработали в убыток на ', financial_results, 'средств. Сожалеем!')

else:
    print('Не в прибыле и не в убытке. Сработано на 0!')
