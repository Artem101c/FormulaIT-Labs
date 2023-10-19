salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money = 0
for i in range(1, months+1):
    money = spend - salary + money
    spend = spend + spend * increase

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money:.0f}")
