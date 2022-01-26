#!/usr/bin/env python3
import argparse
from gendiff.engine import generate_diff

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', type=str, help='set format of output')

args = parser.parse_args()


def main():
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
