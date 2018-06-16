

#!/usr/bin/python
import datetime

from database import get_count, get_x_before
from bitfinex import get_last, get_previous


def percentage_over_periods(percentage, periods, direction):
    # get the number of records back as set by the periods
    # start at the most recent
    # determine if the percentage change has been reached
    most_recent = get_last('BTCUSD')[0]
    previous = get_previous('BTCUSD', most_recent, 2)[1][0]
    period = abs(previous - most_recent)
    qty = get_count()
    for i in range(qty-periods):
        time_to_check = most_recent - (i * period)
        data = get_x_before(3, time_to_check)
        start_price = data[2][0]
        target = (start_price + ((start_price / 100)*4))
        end_price = data[0][0]
        if end_price > target:
            print(str(datetime.datetime.fromtimestamp(
                int((time_to_check - (3 * period))/1000)).strftime('%Y-%m-%d %H:%M')) + ' - ' + str(start_price) + ' - ' + str(end_price))
