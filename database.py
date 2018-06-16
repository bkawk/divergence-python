#!/usr/bin/python
import psycopg2
import sys


def create_db(db_name):
    print('Creating Database')
    con = psycopg2.connect(dbname='postgres', user='bkawk', host='localhost')
    con.autocommit = True
    cur = con.cursor()
    cur.execute('CREATE DATABASE {};'.format(db_name))


def create_table(db_name, table_name):
    print('Creating Table')
    con = psycopg2.connect(dbname=db_name,
                           user='bkawk', host='localhost')
    con.autocommit = True
    cur = con.cursor()
    cur.execute("CREATE TABLE " + table_name + " (id serial PRIMARY KEY, time bigint NOT NULL UNIQUE, open integer NOT NULL, close integer NOT NULL, high integer NOT NULL, low integer NOT NULL, volume integer NOT NULL, nine integer, forty_five integer, rsi integer, rsi_nine integer, rsi_fory_five integer)")


def get_count():
    con = psycopg2.connect(dbname='divergence25',
                           user='bkawk', host='localhost')
    con.autocommit = True
    cur = con.cursor()
    try:
        cur.execute(f"SELECT COUNT(*) FROM price")
        rows = cur.fetchall()
        for row in rows:
            return row[0]
    except:
        print("Data is inconsistent")
        sys.exit("Data is inconsistent")


def get_x_before(periods, time):
    con = psycopg2.connect(dbname='divergence25',
                           user='bkawk', host='localhost')
    con.autocommit = True
    cur = con.cursor()
    try:
        cur.execute(
            f"SELECT close, time FROM price WHERE time <= {time} LIMIT 3")
        rows = cur.fetchall()
        return rows
    except:
        print("SQL Error")


def get_time(time):
    con = psycopg2.connect(dbname='divergence25',
                           user='bkawk', host='localhost')
    con.autocommit = True
    cur = con.cursor()
    try:
        cur.execute(f"SELECT time FROM price WHERE time={time}")
    except:
        print("Data is inconsistent")
        sys.exit("Data is inconsistent")


def set_initial_price(time, open, close, high, low, volume):
    con = psycopg2.connect(dbname='divergence25',
                           user='bkawk', host='localhost')
    con.autocommit = True
    cur = con.cursor()
    cur.execute(
        f"UPDATE price SET open={open}, close={close}, high={high}, low={low}, volume={volume} WHERE time={time}")
    if cur.rowcount == 0:
        cur.execute(
            f"INSERT INTO price (time, open, close, high, low, volume) VALUES ({time}, {open}, {close}, {high}, {low}, {volume})")
