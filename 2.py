import datetime as dt

# Дата выхода первой серии.
start_time = dt.datetime(2011, 4, 17) 

# Дата выхода последней серии.
final_time = dt.datetime(2019, 4, 15) 

# Вычисление продолжительности сериала.
duration = final_time - start_time

# Вывод результата.
print(duration)
