
def month_to_season(месяц):
    if месяц in [12, 1, 2]:
        return "Зима"
    elif месяц in [3, 4, 5]:
        return "Весна"
    elif месяц in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"


num = int(input("Введите число"))
result = month_to_season(num)
print(result)
