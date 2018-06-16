#!/usr/bin/python
import psycopg2
import sys

from database import create_db, create_table, set_initial_price
from bitfinex import get_last, get_previous
from validate_data import validate_data
from seperate_data import percentage_over_periods


try:
    conn = psycopg2.connect("dbname=divergence25 user=bkawk")
except psycopg2.OperationalError as err:
    print(err)
    create_db('divergence25')
    create_table('divergence25', 'price')


def main():
    qty = 1000
    most_recent = get_last('BTCUSD')[0]
    # Previous below also needs adding to the database too!
    previous = get_previous('BTCUSD', most_recent, qty)
    for i in previous:
        try:
            time = int(i[0])
            open = int(i[1])
            close = int(i[2])
            high = int(i[3])
            low = int(i[4])
            volume = int(i[5])
            set_initial_price(time, open, close, high, low, volume)
        except:
            pass
    end_one = previous[qty-1][0]
    for _ in range(46):
        try:
            loop_data = get_previous('BTCUSD', end_one, qty)
            for i in loop_data:
                try:
                    time = int(i[0])
                    open = int(i[1])
                    close = int(i[2])
                    high = int(i[3])
                    low = int(i[4])
                    volume = int(i[5])
                    set_initial_price(time, open, close, high, low, volume)
                except:
                    pass
            end_one = loop_data[qty-1][0]
        except:
            print('Done')
    validate_data()


if __name__ == "__main__":
    #main()
    # validate_data()
    percentage_over_periods(5, 3, 1)
