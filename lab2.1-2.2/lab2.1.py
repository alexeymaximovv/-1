money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

all_money = money_capital
count = 0
while all_money > 6000:
    count += 1
    all_money += salary
    all_money -= spend
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", count)
