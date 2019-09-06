from datetime import datetime
import time


def day_of_the_week(dt):
    '''
    Return a string stating the day of the week corresponding to datetime dt.
    Possible return values are 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'.

    Arguments
    dt: the datetime

    Examples
    day_of_the_week(datetime(2019, 9, 16, 12, 0, 0)) returns 'Friday'
    day_of_the_week(datetime(2000, 1, 22, 11, 33, 0)) returns 'Monday'
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will store the day of the week string in a variable named str
    

    # ====================================
    # Do not change the code after this

    return str


if __name__ == '__main__':
    print(day_of_the_week(datetime(2019, 9, 6, 11, 33, 0)))
    print(day_of_the_week(datetime(2000, 12, 25, 12, 0, 0)))
