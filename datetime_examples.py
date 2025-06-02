import datetime
current_datetime = datetime.datetime.now()
print(current_datetime)
print(current_datetime.day)
print(current_datetime.month)
print(current_datetime.year)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.date())
print(current_datetime.time())

start_date = datetime.datetime(2025,5,2,12,0,0)
print(start_date)
formatted_dt = start_date.strftime("%Y/%m/%d %H:%M:%S")
#2025/06/02 12:00:00
print(formatted_dt)

str_dt = "2025/06/02 12:00:00"
converted_dt = datetime.datetime.strptime(str_dt,"%Y/%m/%d %H:%M:%S")
print(converted_dt)

start_date = datetime.datetime.now()
end_date = datetime.datetime.now()
future_date = start_date + datetime.timedelta(days=2)
past_date = end_date - datetime.timedelta(days=2)
print(future_date)
print(past_date)

start_date = datetime.datetime(2025,5,15,0,0,0)
end_date = datetime.datetime(2025,5,30,0,0,0)

differnce = end_date - start_date
print(differnce.days)

print(differnce.total_seconds() // 3600)