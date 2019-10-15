import datetime
import pytz

print (datetime.datetime.now())
print (pytz.all_timezones)

aus_date = datetime.datetime.now(pytz.timezone('Asia/Qatar'))
print (aus_date )
