from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("today's date is", today)
print("\nCurrent Date and time is ", now)
print("\nDate components", today.year, today.month, today.day)