#creating two phrases to check the time format

from datetime import datetime

datetime_for_sting=datetime(2022,6,12,0,0)
datetime_string_format= "%b %d %Y %H:%M:%S"
print(datetime.strftime(datetime_for_sting,datetime_string_format))
