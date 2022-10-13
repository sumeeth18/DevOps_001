#to get weekday we use following method

from datetime import datetime

days = ["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

d = datetime.strptime("30-09-2022 15:39:42", "%d-%m-%Y %H:%M:%S")

print(days[d.weekday()]+"day")