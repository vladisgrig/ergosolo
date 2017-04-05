#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import requests_cache
import argparse
import xml.etree.ElementTree as ET
from decimal import *

def init_parser():
    parser = argparse.ArgumentParser(description='The current exchange rate is set.')
    parser.add_argument('-cc', '--currency_code', metavar='CODE', nargs='*', default=['EUR', 'USD'], help='Currency code in ISO 4217 format. Default: EUR, USD')
    parser.add_argument('-cn', '--currency_num', metavar='NUM', nargs='*', type=int, help='Currency number in ISO 4217 format.')
    parser.add_argument('-cache', metavar='CACHE_TIME', type=int, default=60, help='Cache time')
    return parser.parse_args()

def get_char_code(element):
    return element.find('CharCode').text

def get_num_code(element):
    return int(element.find('NumCode').text)

def get_currency(element):
    getcontext().prec = 2
    value = float(element.find('Value').text.replace(',', '.'))
    nominal = float(element.find('Nominal').text.replace(',', '.'))
    return float("%.2f" % (value/nominal))

def parse_data(data, codes=[], numbers=[]):
    root = ET.fromstring(data)
    currency = {get_char_code(child): get_currency(child) for child in root
                if get_char_code(child) in codes or get_num_code(child) in numbers }
    print currency

def main():
    args = init_parser()
    requests_cache.install_cache(cache_name='currency_cache', backend='sqlite', expire_after=args.cache)
    codes = [c.upper() for c in args.currency_code]
    nums = args.currency_num if type(args.currency_num) is list else []
    try:
        r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        if r.status_code == requests.codes.ok:
            parse_data(r.content, codes, nums)
        else:
            print unicode("Запрашиваемый ресурс недоступен", encoding="utf8")
            print unicode("Код ошибки: %(status_code)s" % {"status_code": r.status_code}, encoding="utf8")
    except requests.exceptions.ConnectionError:
        print unicode("Проблемы с сетью, проверьте настройки интернет соединения.", encoding="utf8")

if __name__ == '__main__':
    main()
