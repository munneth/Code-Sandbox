from datetime import datetime, timedelta


# calendar functions I have used in the past
# all are made to work with the date format YYYY-MM-DD

#parse date to get day
def getDay(date):
    day = int(date[8:10])
    return day

#parse date to get month
def getMonth(date):
    month = int(date[5:7])
    return month

# increment date by 1 day
def calendarIncrement(date):
    # date is expected in 'YYYY-MM-DD' format
    dt = datetime.strptime(date, "%Y-%m-%d")
    next_day = dt + timedelta(days=1)
    return next_day.strftime("%Y-%m-%d")