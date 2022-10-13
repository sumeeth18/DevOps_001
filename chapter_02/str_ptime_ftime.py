# strptime and strftime

from datetime import date, datetime

print(datetime.now())

from datetime import  timedelta
date_01=datetime.strptime("26-01-2022 5:30:16", "%d-%m-%Y %H:%M:%S")
print(date_01.strftime("%d-%m-%Y %H:%M:%S"))