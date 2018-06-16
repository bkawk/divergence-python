#!/usr/bin/python
import requests
import json


api_url_base = 'https://api.bitfinex.com/v2/'


def get_last(pair):
    """gets the last pair

    Arguments:
        pair {string} -- the name of the pair eg. EOSUSD

    Returns:
        list -- list of price and volume
    """

    api_url = api_url_base + 'candles/trade:1h:t' + pair + '/last'
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def get_previous(pair, end, qty):
    """get the previous pairs

    Arguments:
        pair {string} -- the name of the pair eg. EOSUSD
        end {int} -- time of the last records to request
        qty {int} -- the number of records to request

    Returns:
        list -- qty prices before end for the pair
    """

    api_url = api_url_base + 'candles/trade:1h:t' + pair + \
        '/hist?limit=' + str(qty) + '&end=' + str(end) + ''
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
