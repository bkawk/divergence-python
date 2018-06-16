#!/usr/bin/python
from database import get_time, get_count
from bitfinex import get_last, get_previous


def validate_data():
    most_recent = get_last('BTCUSD')[0]
    previous = get_previous('BTCUSD', most_recent, 2)[1][0]
    period = abs(previous - most_recent)
    qty = get_count()
    for i in range(qty):
        time_to_check = most_recent - (i * period)
        get_time(time_to_check)
