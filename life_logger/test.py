import datetime
import pytz

ctime = datetime.datetime.now(pytz.timezone('UTC'))
print(ctime)
ctime = ctime + datetime.timedelta(hours=9)
print(ctime)