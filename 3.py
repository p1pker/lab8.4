import datetime as dt

# Укажите момент времени, когда вы начали проходить курс (например, 1 января 2023 года в 22:30)
start_moment = dt.datetime(2023, 1, 1, 22, 30)

# Текущий момент времени
current_moment = dt.datetime.now()

# Вычисление разницы между текущим моментом и моментом начала курса
total_time = current_moment - start_moment

# Вывод результата
print(total_time)
