import datetime


def get_birth_date():
    print('Please tell me when you were born:')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [mm]: '))
    day = int(input('Day [dd]: '))
    print('\n')
    bdate = datetime.date(year, month, day)
    return bdate


def is_a_leap_year(year):
    leap_year = False
    if year % 4 == 0:
        leap_year = True
        if year % 100 == 0:
            leap_year = False
            if year % 400 == 0:
                leap_year = True
    return leap_year


def leap_year_check(date):
    # If person was born on Feb 29, and the current
    # year isn't a leap year, we should adjust the birthday
    # for the current year to be Feb 28.
    if (date.month, date.day) == (2, 29):
        print('Wow - you were born on Feb 29th!  A leap year ...')
        current_year = datetime.date.today().year
        if is_a_leap_year(current_year):
            print('This year, {}, is also a leap year.'.format(current_year))
        else:
            print('This year, {}, is not a leap year, so your birthday is / was Feb 28th.'.format(current_year))
            return date - datetime.timedelta(days=1)
    return date


def main():
    # print header
    print('{0}\n{1:^25}\n{0}'.format('-' * 25, 'BIRTHDAY APP'))

    # Get date of birth
    bdate = get_birth_date()
    print('It looks like you were born on {}'.format(bdate))

    # Do a leap year check
    # Could be born on Feb 29 but have birthday on Feb 28 this year ...
    bdate = leap_year_check(bdate)

    today = datetime.date.today()
    # Current year's birthday
    birthday = datetime.date(today.year, bdate.month, bdate.day)

    diff = today - birthday
    if diff.days == 0:
        print('Congrats!  It\'s your birthday today!')
    elif diff.days < 0:
        print('It is your birthday in {} days time'.format(-diff.days))
    else:
        print('It was your birthday {} days ago'.format(diff.days))


if __name__ == '__main__':
    main()
