#-------------
#I am copying the answer to valid month in an attempt to learn python
#This program verifies that a user enters a valid month

month = ['January',
         'February',
         'March',
         'April',
         'May',
         'June',
         'July',
         'August',
         'September',
         'October',
         'November',
         'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

def valid_day(day):
    try:
        d = int(day)
        if 1 <= d <= 31:
            return d
    except ValueError:
            pass
    return None

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year

