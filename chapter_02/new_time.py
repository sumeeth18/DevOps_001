from datetime import datetime
from dateutil import tz
import pytz

pacific_time=datetime.now(pytz.timezone("US/Pacific"))
print(pacific_time)

