
# Python Date and Time Workbook with Solutions

from datetime import datetime, date, time, timedelta
import time as t
import calendar

# Exercise 1: Current date and time
now = datetime.now()
print("Exercise 1: Current date and time:", now)

# Exercise 2: Current date only
today = date.today()
print("Exercise 2: Today's date:", today)

# Exercise 3: Combine date and time
d = date(2025, 7, 29)
t1 = time(12, 30, 45)
dt = datetime.combine(d, t1)
print("Exercise 3: Combined datetime:", dt)

# Exercise 4: Format date and time
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Exercise 4: Formatted datetime:", formatted)

# Exercise 5: Finding duration
start = datetime(2025, 7, 1)
end = datetime(2025, 7, 29)
duration = end - start
print("Exercise 5: Duration in days:", duration.days)

# Exercise 6: Comparing dates
date1 = datetime(2025, 7, 1)
date2 = datetime(2025, 8, 1)
print("Exercise 6:", date1 < date2)  # Output: True

# Exercise 7: Sorting list of dates
dates = [datetime(2025, 7, 30), datetime(2024, 12, 25), datetime(2025, 1, 1)]
dates.sort()
print("Exercise 7: Sorted dates:", dates)

# Exercise 8: Pause execution temporarily
print("Exercise 8: Pausing for 2 seconds...")
t.sleep(2)
print("Resumed!")

# Exercise 9: Calculate execution time
start_time = t.time()
# some dummy operation
for i in range(1000000):
    pass
end_time = t.time()
print("Exercise 9: Duration of execution:", end_time - start_time, "seconds")

# Exercise 10: Display calendar
print("Exercise 10: Calendar of July 2025:")
print(calendar.month(2025, 7))
