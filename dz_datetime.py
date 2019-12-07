from datetime import date, datetime, timedelta

dt_now = datetime.now()

# Вчера
yesterday = dt_now - timedelta(days=1)
print("Вчера: ", yesterday)

# Сегодня
print("Сегодня: ", dt_now)

# Месяц назад
last_month = dt_now.replace(day=1) - timedelta(days=1)
last_month = last_month.replace(day=1) + (dt_now - dt_now.replace(day=1))
print("Месяц назад: ", last_month)

# Превратить строку
data_str = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(data_str, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)