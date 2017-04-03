#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

def init_parser():
    parser = argparse.ArgumentParser(description='The words from the file are filtered.')
    parser.add_argument('file', type=file, help='File containing the words.')
    parser.add_argument('letter', choices=['у','е','э','о','а','ы','ю','и','я','ё',], help='The letter used for filtering.')
    return parser.parse_args()

def main():
    args = init_parser()
    vowels = ur'аеёиоуыэюя'
    acceptable_vowels = vowels.replace(unicode(args.letter, encoding="utf8"), "")

    pattern = re.compile(ur'(^[б-дж-зй-нп-тф-ь]*[%(acceptable_vowels)s]([б-дж-зй-нп-тф-ь]) \2[^б-дж-зй-нп-тф-ь][а-я]*$)|(^[а-я]*[%(acceptable_vowels)s]([б-дж-зй-нп-тф-ь]) \4[^б-дж-зй-нп-тф-ь]?$)|(^[а-я]*[%(acceptable_vowels)s]([б-дж-зй-нп-тф-ь]) \6[^б-дж-зй-нп-тф-ь][б-дж-зй-нп-тф-ь]*$)' % {"acceptable_vowels": acceptable_vowels}, re.X|re.U)

    for line in args.file:
        string = unicode(str.strip(line).lower(), encoding="utf8")
        result = pattern.match(string)
        if  not(result is None):
                    print string

if __name__ == '__main__':
    main()

# получает нужное совпадение на втором слоге
# ^[б-дж-зй-нп-тф-ь]*[аеёиоуыэюя]{1}([б-дж-зй-нп-тф-ь]) \1[^б-дж-зй-нп-тф-ь][а-я]*$

# получает нужное совпадение на последнем слоге
# (^[а-я]*[аеёиоуыэюя]([б-дж-зй-нп-тф-ь]) \2[^б-дж-зй-нп-тф-ь]?$)|(^[а-я]*[аеёиоуыэюя]([б-дж-зй-нп-тф-ь]) \4[^б-дж-зй-нп-тф-ь][б-дж-зй-нп-тф-ь]*$)

# полное регулярное выражение
# (^[б-дж-зй-нп-тф-ь]*[аеёиоуыэюя]([б-дж-зй-нп-тф-ь]) \2[^б-дж-зй-нп-тф-ь][а-я]*$)|(^[а-я]*[аеёиоуыэюя]([б-дж-зй-нп-тф-ь]) \4[^б-дж-зй-нп-тф-ь]?$)|(^[а-я]*[аеёиоуыэюя]([б-дж-зй-нп-тф-ь]) \6[^б-дж-зй-нп-тф-ь][б-дж-зй-нп-тф-ь]*$)
