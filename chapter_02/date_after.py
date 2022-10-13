#n days after date
import datetime
from datetime import timedelta
from xmlrpc.client import _datetime_type

def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)
