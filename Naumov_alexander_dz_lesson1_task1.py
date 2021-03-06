# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек


# input duration
duration = int(input('input duration in second: '))

# string variables for result line
days = ' day(s) '
hours = ' hour(s) '
minutes = ' minute(s) '
seconds = ' second(s) '

# int constants for secs quantities
sec_in_minute = 60
sec_in_hour = sec_in_minute * 60
sec_in_day = sec_in_hour * 24

# calculation quantity of days, hours, minutes, sec
days_qnty = duration // sec_in_day
hours_qnty = (duration - days_qnty * sec_in_day) // sec_in_hour
minutes_qnty = (duration - days_qnty * sec_in_day - hours_qnty * sec_in_hour) // sec_in_minute
seconds_qnty = duration - days_qnty * sec_in_day - hours_qnty * sec_in_hour - minutes_qnty * sec_in_minute

# showing result on a screen
if days_qnty > 0:
    print(days_qnty, days, hours_qnty, hours, minutes_qnty, minutes, seconds_qnty, seconds)
elif days_qnty == 0 and hours_qnty > 0:
    print(hours_qnty, hours, minutes_qnty, minutes, seconds_qnty, seconds)
elif days_qnty == 0 and hours_qnty == 0 and minutes_qnty > 0:
    print(minutes_qnty, minutes, seconds_qnty, seconds)
elif days_qnty == 0 and hours_qnty == 0 and minutes_qnty == 0:
    print(seconds_qnty, seconds)
