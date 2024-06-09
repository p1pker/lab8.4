# Библиотеки в Python

Библиотека или модуль — это набор готовых функций, объединённых общей темой. Например, в библиотеке ```math``` собраны функции для подсчёта математических величин, в библиотеке random — инструменты для получения случайных значений, а библиотека ```datetime``` работает с датами (как узнать, сколько дней осталось до Нового Года? Через инструменты библиотеки datetime!).

Чтобы получить доступ к этим функциям, нужно в начале программы импортировать библиотеку командой ```import``` — «подключить» её. Тогда в коде можно будет применять все функции, которые есть в библиотеке. 

Для импорта библиотеки math нужно написать ```import math```.
После импорта можно, например, при помощи функции ```sqrt()``` библиотеки math извлечь квадратный корень из заданного числа. Чтобы вызвать функцию из импортированной библиотеки — к ней обращаются через имя библиотеки: ```имя_библиотеки.имя_функции```.

Пример:
```python=
# Импорт библиотеки math. 
import math 

# Теперь в программе можно применять любые функции из неё.
square_root = math.sqrt(16)
print(square_root)
```
Сразу возникает нестыковка: как же так, функцию ```print()``` мы применяем уже давно, но импортировать её не приходилось. Дело в том, что часть функций не нуждаются в импорте, они встроены в Python и доступны без дополнительных манипуляций.

Продолжим эксперименты.

Импортируем библиотеку random — и станут доступны её функции, например

- функция ```random.randint(min, max)``` выберет случайное целое число в диапазоне от числа min до числа max;
- функция ```random.choice(список)``` вернёт случайный элемент из списка;
- функция ```random.random()``` вернёт случайное дробное число от 0.0 до 1.0.

Если все функции библиотеки не нужны, можно импортировать только те, которые требуются: ```from random import choice```  (из библиотеки **random** подключить функцию  **choice**).

Вот отличная программа для нерешительных родителей: она выбирает подарок ребёнку. В код импортирована не вся библиотека random, а лишь одна функция из неё. 

В таком случае к этой функции обращаются напрямую, без указания имени библиотеки.

Запустите этот код несколько раз, посмотрите, что он выведет.

```python=
from random import choice  # Импорт одной функции из библиотеки

def find_a_present(prizes):
    # Обращаемся к функции напрямую: choice(), а не random.choice()
    return choice(prizes) 

print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
print(find_a_present(['мяч', 'чебурашка', 'лосяш']))
```

Иногда у библиотек очень длинные имена, и, если не хочется при каждом вызове писать её полное имя и загромождать код, при импорте можно дать библиотеке короткий «псевдоним» через ключевое слово ```as```:

```python=
import random as r

# Теперь к библиотеке random нужно обращаться только через псевдоним r:
print(r.randint(0, 100)) # Случайное целое число от 0 до 100
```

:::info
Ловите [Шпоргалка по библиотекам](https://ftp.codimd.ru/f/770c2e03ebd840d8946f/)
:::

## Задача №1
Научите Анфису отвечать на вопрос «Анфиса, как дела?» случайным образом.

Напишите функцию ```how_are_you()```, она должна вернуть случайный элемент из списка answers. Добавьте в список свои варианты ответов: ничего не сломается, а работать станет интереснее.

```python=
# Подключите библиотеку random и дайте ей краткое имя

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    # Напишите ваш код здесь


print(how_are_you())
```

## Работа со временем

Для работы со временем в Python импортируют библиотеку **```datetime```**. В ней есть не только отдельные функции, но и целый новый тип данных — *```datetime```*.

Название типа данных точно совпадает с библиотекой, и это не слишком удобно. Чтобы не путаться, библиотеку будем подключать под именем ```dt```:
```python=
import datetime as dt
```

Тип данных *```datetime```* — ещё один тип, как **int**, **string** или **dict**. Он нужен, чтобы хранить информацию о конкретном моменте времени: год, месяц, день, час, минуты, секунды и микросекунды. 

Чтобы создать объект этого типа, нужно вызвать функцию **datetime()**  из библиотеки **dt**. Она принимает обязательные аргументы — год, месяц и день, — и необязательные: час, минута, секунда и микросекунда, которые по умолчанию равны нулю.

Создадим объект типа ```datetime``` с датой и временем старта Гагарина:
```python=
import datetime as dt 

# Взлёт: 1961 год, 12 апреля, 9 часов утра, 7 минут 
start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

print('Уже', start_time, 'Поехали!') 
```

Тип данных datetime позволяет просто вычитать даты друг из друга, как обычные числа. Если решать такие задачи обычными математическими выражениями — код будет гораздо сложнее.

```python=
import datetime as dt 

start_time = dt.datetime(1961, 4, 12, 9, 7, 0)

# Дата и время посадки: 1961 год, 12 апреля, 10 часов, 55 минут
landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)

print(landing_time - start_time) 
```

При создании данных типа datetime можно не указывать время и обойтись только датой. В этом случае метка времени будет установлена автоматически, это будет полночь, начало заданной даты:

```python=
import datetime as dt 

start_day = dt.datetime(1961, 4, 12)

print(start_day) 
```
## Задача №2
Научите Анфису сообщать пользователю, сколько времени шёл его любимый сериал.

Дата выхода первой серии - 17 апреля 2011 года.

Дата выхода последней серии - 15 апреля 2019 года.

```python=
import datetime as dt

# Дата выхода первой серии.
start_time = dt.datetime(2011, 4, 17) 
# Укажите дату выхода последней серии.
final_time = dt.datetime(...) 

# Вычислите, сколько времени шёл сериал.
duration = ...  

print(duration)
```

## Задача №3

Напишите код, который рассчитает, сколько времени у вас ушло на вводный курс по бэкенд-разработке.

Вспомните, в какой день и во сколько вы начали проходить курс. Запишите этот момент времени (полностью, с часами и минутами) в переменную ```start_moment```.  В переменную ```current_moment``` запишите текущий момент времени. Затем вычислите разницу двух этих моментов, запишите её в переменную ```total_time```, и напечатайте её.

```python=
# подключите библиотеку datetime под именем dt

start_moment = ...  # Напишите код здесь
current_moment = ...  # и здесь

total_time = ...  # и здесь

print(...)
```

## Стандарт времени UTC

Есть несколько стандартов измерения и записи времени. Раньше в основном придерживались GMT (англ. «Greenwich Mean Time», среднее время по гринвичскому меридиану). Позже этот всемирный формат заменили на новый, определяемый атомными часами. Это UTC — «coordinated universal time» — всемирное координированное время. 

У любой переменной типа данных datetime можно вызвать метод **utcnow()**. Он вернёт текущий момент времени по UTC с эталонной точностью до микросекунд.

Напишем программу-часы:

```python=
import datetime as dt

utc_time = dt.datetime.utcnow()
print(utc_time)
```

Скорее всего, вы получили не то время, которое сейчас у вас на часах. Что-то пошло не так? Да нет, всё в порядке: вы получили время на нулевом меридиане, и если вы живёте не на нулевой долготе — у вас другое время.

Дело в том, что Python «узнаёт время» у того компьютера или сервера, на котором выполняется код; код, который вы выполнили, запускается на сервере Яндекс.Практикума. Там выставлен нулевой часовой пояс по UTC. Московское время обгоняет UTC на три часа: UTC+3. Время в Ванкувере отстаёт на семь часов, UTC-7, а в Петропавловске-Камчатском — вообще UTC+12.

Похоже, получить точное текущее время в своём городе — не проблема, нужно просто прибавить или вычесть поправку к UTC. Для эксперимента вычислим московское время:

```python=
import datetime as dt

utc_time = dt.datetime.utcnow()
moscow_time = utc_time + 3
```

Не вышло. Python сообщает об ошибке в строке ```moscow_time = utc_time + 3```: «нельзя складывать переменную типа datetime с переменной типа **int**». Точно как при попытке сложить строку с числом.

Не беда! На такой случай есть тип данных **timedelta**, в котором можно сохранить определённый промежуток времени — в часах, днях, годах, как угодно. Этот тип данных тоже хранится в библиотеке ```dt```. А объект такого типа создаётся функцией ```timedelta()```

```python=
import datetime as dt

# Как и раньше - определяем текущее время UTC
utc_time = dt.datetime.utcnow()

# Создаём промежуток времени в три часа
period = dt.timedelta(hours=3)

# И прибавляем к значению времени по UTC поправку в три часа:
moscow_time = utc_time + period

# Печатаем
print(moscow_time) 
```
В аргументах функции ```timedelta()``` можно указывать days, hours, minutes, seconds, microseconds.

Победитель Гран-при Австралии чемпионата мира Формулы-1 2019 года, Валттери Боттас, проехал свой самый быстрый круг за 1 минуту 25 секунд и 273250 микросекунд. Второй результат показал Льюис Хэмилтон, отстав от Боттаса на 208860 микросекунд.

Вычислим время самого быстрого круга Хэмилтона.
```python=
import datetime as dt

# Время, за которое Боттас сделал круг — это не дата, 
# а продолжительность, промежуток времени. Создаём данные типа timedelta:
time_bottas = dt.timedelta(minutes=1, seconds=25, microseconds=273250)

# Вычисляем timedelta Хэмилтона:
time_hamilton = time_bottas + dt.timedelta(microseconds = 208860)

print(time_hamilton)
```

## Задача №4

Напишите функцию, которая по названию города скажет, сколько там сейчас времени.

Мы заготовили словарь *UTC_OFFSET*, где для каждого города записана его поправка к **UTC** в часах.
```python=
import datetime as dt

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

def what_time(city):
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city


print(what_time('Екатеринбург'))
```

## Задача №5

В код добавлен словарь **DATABASE**, в нём хранятся данные о том, кто из друзей где живёт. 

Напишите код функции **what_time()**, которая по имени друга скажет, сколько у него сейчас времени. 

На вход функция должна получить имя друга, а вернуть — текущее время в его городе.

```python=
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
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend


print(what_time('Соня'))
```

## Форматирование времени 

До сих пор вы печатали время только в одном формате.

```python=
import datetime as dt


arrival_time = dt.datetime(2019, 5, 10, 19, 45)
    
print('Самолёт прибывает в', arrival_time)

## Самолёт прибывает в 2019-05-10 19:45:00
```

Что делать, если хочется напечатать сообщение по-человечески, скажем: Сейчас 10:31? Для этого существует метод **strftime()**. Его можно применить к любому объекту типа **datetime** и аргументом задать формат вывода времени:

```python=
print('Самолёт прибывает в', arrival_time.strftime('%H:%M'))
## Самолёт прибывает в 19:45 
```

Здесь ```%H``` означает часы, ```%M``` — минуты. 

Кроме этих параметров, бывают ещё, например ```%B```  — месяц, ```%Y``` — год и ```%S``` — секунды, ```%A``` — название дня недели по-английски, ```%U``` — номер недели в году.

```python=
import datetime as dt


# дата первого осеннего снега в Новосибирске в 2018
first_snow = dt.datetime(2018, 9, 9)

# дата последнего весеннего снега в Новосибирске в 2018
last_snow = dt.datetime(2018, 5, 19)

print(last_snow.strftime('Последний снег выпал в %U-ю неделю года.'))
print(first_snow.strftime('А первый снег пошёл в %U-ю неделю.'))

# # Последний снег выпал в 19-ю неделю года.
# А первый снег пошёл в 36-ю неделю. 
```

В 2018 году новосибирцы прожили без снега целых 17 недель!

## Задача №6 

Сделайте так, чтобы функция what_time() возвращала время в формате часы:минуты.
```python=
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
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    return utc_time + dt.timedelta(hours=UTC_OFFSET[city])


print(what_time('Соня'))
```

## Задача №7

Примените все полученные в этой теме знания, чтобы научить Анфису отвечать на вопросы про друзей, сколько у них сейчас времени:

- Артём, который час?
- Антон, который час?

Примеры таких запросов уже добавлены в список queries в функции ```runner()```.

Измените функцию ```process_friend()```, чтобы она обрабатывала ещё один запрос, а именно ```query == 'который час?'```

Если город друга есть в базе ```UTC_OFFSET```, вызовите функцию ```what_time()``` и, подставив полученный результат, верните ответ в формате Там сейчас 19:28.

Если город отсутствует в базе ```UTC_OFFSET```, то верните сообщение об ошибке ```<не могу определить время в городе {название}>```. 

```python=
DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))

runner()
```
