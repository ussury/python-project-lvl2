import argparse


def get_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='%(prog)s [options] <filepath1> <filepath2>',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish', type=str,
        help='output format (default: "stylish")')
    args = parser.parse_args()

    return args.first_file, args.second_file, args.format