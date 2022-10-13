# to get list of dates 

from datetime import datetime, timedelta

dt= datetime.strptime("30-09-2022 16:15:38", "%d-%m-%Y %H:%M:%S")
list_dates=[]

for x in range(0,7):
    dt=dt+timedelta(days=1)
    list_dates.append(dt)
for item in list_dates:
    print(item)