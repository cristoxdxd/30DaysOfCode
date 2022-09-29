import datetime

def get_days_between_dates(date1, date2):
    return abs((date2 - date1).days)

def get_hours_per_day_without_weekends(hours, days):
    return hours / (days - (days // 7) * 2)

def main():
    date1 = input("Enter the start date (DD/MM/YYYY): ")
    date2 = input("Enter the end date (DD/MM/YYYY): ")
    hours = input("Enter the number of hours: ")
    date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
    date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
    days = get_days_between_dates(date1, date2)
    hours_per_day = get_hours_per_day_without_weekends(int(hours), days)
    date1 = date1.strftime("%d/%m/%Y")
    date2 = date2.strftime("%d/%m/%Y")
    print("\n\nStart Date: {}".format(date1))
    print("End Date: {}".format(date2))
    hours_per_day = datetime.timedelta(hours=hours_per_day)
    # format the hours per day to %HH:%MM:%SS
    hours_per_day = '{:02}:{:02}:{:02}'.format(hours_per_day.seconds // 3600, (hours_per_day.seconds // 60) % 60, hours_per_day.seconds % 60)
    print("Hours per day: {}".format(hours_per_day))

main()