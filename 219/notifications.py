from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    count = 0
    td = timedelta(days=num_days)
    start_date = start_date + td
    while True:
        yield start_date
        count += 1
        if count == num_bites:
            start_date = start_date + td
            count = 0
