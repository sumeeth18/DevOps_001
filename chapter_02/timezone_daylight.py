#importing datetime from datetime
import datetime
from datetime import datetime
from dateutil import tz

local= tz.gettz()
PT=tz.gettz('US/Pacific')
print(PT)

from datetime import datetime, timedelta
now = datetime.now()
then=datetime(2022, 3, 12)

delta=now-then
print(delta.days)

# #n days after date
# today_date= datetime.datetime.date.today()
# print(today_date)
