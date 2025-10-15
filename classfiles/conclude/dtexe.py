from datetime import date,time,datetime,timedelta

now =datetime.now()
print("current date and time",now)

d =date(2025,7,29)
t=time(12,15,0)

dt =datetime.combine(d,t)
print(dt)

formatted = now.strftime("%d-%b-%Y %I:%M %p")
print(formatted)

date_str ="29-07-2025 13:15"

ds = datetime.strptime(date_str,"%d-%m-%Y %H:%M")
print("Parsed",ds)

start = datetime(2025,7,29,12,0)
end = datetime(2025,7,29,14,30)
duration = end-start
print("duration",duration)

d1 =datetime(2025,7,29)
d2 =datetime(2025,7,30)



  






