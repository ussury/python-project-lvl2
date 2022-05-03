#!/usr/bin/env python3
import argparse
from gendiff.diff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()

    return args.first_file, args.second_file


def main():
    args = get_args()
    print(generate_diff(*args))


if __name__ == '__main__':
    main()
