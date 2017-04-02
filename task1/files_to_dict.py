import argparse
from itertools import izip_longest
import pprint

def init_parser():
    parser = argparse.ArgumentParser(description='Combines files into a dictionary.')
    parser.add_argument('file1', type=file, help='File containing the keys.')
    parser.add_argument('file2', type=file, help='File containing the values.')
    return parser.parse_args()

def get_items(file, to_type):
    values = []
    for line in file:
        values.extend([to_type(str.strip(x)) for x in line.split()])
    return values

def make_dict(keys, values, fill_value = None):
    return {k : v for k, v in izip_longest(keys, values[:len(keys)], fillvalue=None)}

def main():
    args = init_parser()
    keys = get_items(args.file1, str)
    values = get_items(args.file2, int)
    dictionary = make_dict(keys, values)
    pp = pprint.PrettyPrinter()
    pp.pprint(dictionary)

if __name__ == '__main__':
    main()
