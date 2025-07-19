#region Calculate days count between 2 dates
"""
Створіть функцію get_days_from_today(date),
яка розраховує кількість днів між 
заданою датою і поточною датою.
"""

from datetime import datetime, timedelta
from random import random,randrange

def get_days_from_today(date):
    try:
        _date_formated = datetime.strptime(date,"%Y-%m-%d")
        _result = int((_date_formated - datetime.today() ).days)
    except TypeError :
        _result =  f"Incorrect input data. Date should be DateTime object"
    except ValueError:
        _result =  f"Incorrect input data. Date should be in YYYY-MM-DD format"
    finally:
        return _result
    
new_date = "2015-06-27"
print (f"Difference between date = {get_days_from_today(new_date)} days")
#endregion

#region Generate a ragne of numbers

def get_numbers_ticket(min, max, quantity):
    if (min > max):
        _return = "Range start value should be more that finish value"
    elif (quantity <= 0 or type(quantity) != int) :
        _return =  "The quantity value should be integer and positive"
    elif (min <0 or max <0 or type(min) != int  or type(max) != int):
        _return =  "The boundaries of range should be integer and positive"
    else:
        temp_list = list()
        while len(temp_list) <= quantity-1:
            _random = randrange(min,max)
            if  _random not in temp_list:
                temp_list.append(_random)
        temp_list.sort()
        _return =  f"The random set is {temp_list}"
    return _return

print(get_numbers_ticket(46,625,5))

#endregion