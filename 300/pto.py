import calendar
from datetime import date, timedelta, datetime


ERROR_MSG = (
    "Unambiguous value passed, please specify either start_month or show_workdays"
)
FEDERAL_HOLIDAYS = (
    date(2020, 9, 7),
    date(2020, 10, 12),
    date(2020, 11, 11),
    date(2020, 11, 26),
    date(2020, 12, 25),
)
WFH = (calendar.TUESDAY, calendar.WEDNESDAY)
WEEKENDS = (calendar.SATURDAY, calendar.SUNDAY)
AT_HOME = WFH + WEEKENDS


def four_day_weekends(
        start_month: int = 8,
        paid_time_off: int = 200,
        year: int = 2020,
        show_workdays: bool = False
    ) -> None:
    """Generates four day weekend report

    The four day weekends are calculated from the start_month through the end of the year
    along with the number of work days for the same time period. The reports takes into
    account any holidays that might fall within that time period and days designated as
    working from home (WFH).

    If show_workdays is set to True, a report with the work days is generated instead of
    the four day weekend dates.

    Args:
        start_month (int, optional): Month to start. Defaults to 8.
        paid_time_off (int, optional): Paid vacation days
        year (int, optional): Year to calculate, defaults to current year
        show_workdays (bool, optional): Enables work day report. Defaults to False.

    Raises:
        ValueError: ERROR_MSG
    """
    four_days = []
    work_days = []
    if isinstance(start_month, bool):
        raise ValueError(ERROR_MSG)
    if not isinstance(start_month, int) or not isinstance(year, int) or not isinstance(paid_time_off, int) or not isinstance(show_workdays,bool):
        raise ValueError(ERROR_MSG)
    today = date(year=year,month=start_month,day=1)
    start = False
    end = False
    for i in range(365):
        d = today+timedelta(days=i)
        if d.year == year:
            if d.isoweekday() == 5:
                start = d
            if d.isoweekday() == 1:
                end = d
                if not start:
                    work_days.append(d)
                    continue
                if end in FEDERAL_HOLIDAYS:
                    work_days.append(start)
                if not start in FEDERAL_HOLIDAYS and not end in FEDERAL_HOLIDAYS:
                    four_days.append((start,end))
            if d.isoweekday() == 4:
                work_days.append(d)
    if show_workdays:
        remaining_count = len(work_days)
        print(f"Remaining Work Days: {remaining_count*8} ({remaining_count} days)")
        for day in work_days:
            print(day.strftime("%Y-%m-%d"))
    else:
        max_days_off = len(four_days) * 2
        diff = paid_time_off/8 - max_days_off
        print(f"  {len(four_days)} Four-Day Weekends  ")
        print("======================================")
        print(f"    PTO: {paid_time_off} ({paid_time_off//8} days)")
        print(f"BALANCE: {int(diff*8)} ({abs(int(diff))} days)")
        print()
        temp_avail = max_days_off
        point = ""
        stop = False
        if temp_avail < paid_time_off/8:
            stop = True
        for idx, dates in enumerate(four_days):
            temp_avail -= 2
            friday = dates[0].strftime("%Y-%m-%d")
            monday = dates[1].strftime("%Y-%m-%d")
            if temp_avail < (paid_time_off/8) and stop == False:
                print(f"{friday} - {monday} *")
                stop = True
            else:
                print(f"{friday} - {monday}")
        
    
if __name__ == "__main__":
    four_day_weekends()