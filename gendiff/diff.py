# from pathlib import Path
# from gendiff.parser import parse
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import get_json

FORMATTER = {
    'stylish': stylish,
    'plain': plain,
    'json': get_json
}


def get_diff(dicts):
    data1 = dicts[0]
    data2 = dicts[1]
    keys = data1.keys() | data2.keys()
    diff = {}
    for key in keys:
        if all(map(lambda el: isinstance(el.get(key), dict), dicts)):
            diff[key] = ['nested', get_diff([data1[key], data2[key]])]
        elif data1.get(key) == data2.get(key):
            diff[key] = ['same', data1.get(key)]
        elif key not in data1:
            diff[key] = ['added', data2.get(key)]
        elif key not in data2:
            diff[key] = ['deleted', data1.get(key)]
        else:
            diff[key] = ['modified', data1.get(key), data2.get(key)]
    return diff


""" def generate_diff(first_file, second_file, format):
    try:
        first_path = parse(Path(first_file))
        second_path = parse(Path(second_file))
        parse_file = [first_path, second_path]
    except FileNotFoundError:
        return print('Неверный путь к файлу')  # Wrong file path

    return FORMATTER[format](get_diff(parse_file)) """
