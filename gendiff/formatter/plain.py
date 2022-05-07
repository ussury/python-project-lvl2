from gendiff.formatter.stylish import get_bool_text


def value_view(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value in (True, False, None):
        return get_bool_text(value)
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def add_string(full_path, value1, status, value2=None):
    value1 = value_view(value1)
    value2 = value_view(value2)
    if status == 'added':
        return f"Property '{full_path}' was added with value: {value1}\n"
    if status == 'deleted':
        return f"Property '{full_path}' was removed\n"
    if status == 'modified':
        return (f"Property '{full_path}' was updated. "
                f"From {value1} to {value2}\n")
    return ''


def plain(diff):

    def iter(data, full_path=''):
        keys = sorted(data)
        view = ''
        for key in keys:
            if data[key][0] == 'nested':
                view += iter(data[key][1], f'{full_path}{key}.')
            elif data[key][0] == 'modified':
                view += add_string(f'{full_path}{key}', data[key][1],
                                   'modified', data[key][2])
            else:
                view += add_string(f'{full_path}{key}',
                                   data[key][1], data[key][0])
        return view

    return iter(diff)[:-1]
