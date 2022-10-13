# checking date differebnce

from datetime import date, datetime

d1= datetime.now()
d2=datetime.strptime("18-06-2021 23:36:00", "%d-%m-%Y %H:%M:%S")
d3=d1.today()
d4=d3-d2
print(d4)