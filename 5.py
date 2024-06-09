import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # Получаем город проживания друга из словаря DATABASE
    city = DATABASE.get(friend)
    
    if city is None:
        return "Друг не найден"
    
    # Получаем поправку для указанного города из словаря UTC_OFFSET
    offset = UTC_OFFSET.get(city)
    
    if offset is None:
        return "Поправка к UTC для указанного города не найдена"
    
    # Получаем текущее время по UTC
    utc_time = dt.datetime.utcnow()
    
    # Создаем объект timedelta с полученной поправкой
    period = dt.timedelta(hours=offset)
    
    # Вычисляем текущее локальное время друга
    local_time = utc_time + period
    
    return local_time

# Пример использования
print(what_time('Соня'))
