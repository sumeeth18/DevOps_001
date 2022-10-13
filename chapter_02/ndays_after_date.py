# ndays after prsent date

# 
from datetime import datetime
import pytz

cur_time=datetime.now()

print(cur_time.today())

all_timezones=pytz.all_timezones

print(all_timezones)

londo_time=datetime.now(pytz.timezone('Europe/London'))
print(f'{londo_time} is london time')
