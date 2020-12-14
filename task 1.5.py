income = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if income > costs:
    print("Фирма отработала с прибылью!")
    print(f"Рентабельность составила: {income / costs:.1f}")
    workers = int(input("Введите количество сотрудников в фирме: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника составила: {costs / workers:.1f}")
elif income == costs:
    print("Фирма отработала в ноль.")
else:
    print("Фирма отработала в убыток.")
