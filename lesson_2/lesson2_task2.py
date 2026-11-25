def is_year_leap(year):
    return year % 4 == 0


n = int(input("Введите год"))
result = is_year_leap(n)
print("Год", n, ":", result)
