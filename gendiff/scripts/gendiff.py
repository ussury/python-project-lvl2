#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.diff import generate_diff


def main():
    args = get_args()
    print(generate_diff(*args))


if __name__ == '__main__':
    main()
