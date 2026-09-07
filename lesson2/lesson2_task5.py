def month_to_season(месяц):
    if месяц < 3:
        return "Зима"
    elif месяц < 6:
        return "Весна"
    elif месяц < 9:
        return "Лето"
    elif месяц < 12:
        return "Осень"
    else:
        return "Зима"


num = int(input("Введите число"))
result = month_to_season(num)
print(result)
