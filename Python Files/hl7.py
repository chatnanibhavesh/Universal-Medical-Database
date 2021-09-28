import datetime
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def get_DateTime():
    date = datetime.datetime.now()
    year, month, day, hour, minute, second = str(date.year), '%02d'%date.month, \
                                             '%02d'%date.day, '%02d'%date.hour, \
                                             '%02d'%date.minute, '%02d'%date.second
    Date = year + month + day
    Time = hour + minute
    return Date, Time

