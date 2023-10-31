
# Example of the current time of a timezone example is (London GMT)

from datetime import *
import pytz # Using pytz module 


# Current Time Zone # 
tz_UNITEDKINGDOM = pytz.timezone("Europe/London")

datetime_UNITEDKINGDOM = datetime.now(tz_UNITEDKINGDOM)
print("UNITEDKINGDOM time:", datetime_UNITEDKINGDOM.strftime("%H:%M:%S"))

