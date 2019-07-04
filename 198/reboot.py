from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    reboot_list = reboots.split('\n')
    date_list = [ x.split('~')[1].strip() for x in reboot_list if x]
    max_diff = 0
    max_date = ''
    for i in range(0,len(date_list)-1):
        delta = relativedelta(parse(date_list[i]),parse(date_list[i+1]))
        days = int(delta.days + delta.hours/24 + delta.minutes/60/24)
        if days > max_diff:
            max_diff = days
            max_date = parse(date_list[i]).strftime('%Y-%m-%d')
    return (max_diff, max_date)
    
