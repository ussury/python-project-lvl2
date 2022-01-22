#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first file', type=str)
parser.add_argument('second file', type=str)

args = parser.parse_args()


def main():
    print(args)


if __name__ == '__main__':
    main()
