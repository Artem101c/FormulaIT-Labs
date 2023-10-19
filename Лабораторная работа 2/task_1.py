money_capital = 20000  # Подушка безопасности
salar = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
while money_capital > 0:
    money_capital += salar
    money_capital -= spend
    spend = spend + increase * spend
    month += 1

if money_capital < 0:
    month -= 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
