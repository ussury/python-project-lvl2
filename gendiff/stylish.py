def get_bool_text(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def add_dict(data, step):
    keys = sorted(data)
    result_str = '{\n'

    for key in keys:
        inner = (step + 1) * 4 * ' '
        result_str += f'{inner}{key}: '

        if isinstance(data[key], dict):
            result_str += add_dict(data[key], step + 1) + '\n'
        else:
            result_str += f'{get_bool_text(data[key])}\n'

    return result_str + step * 4 * ' ' + '}'


def add_string(status, key, value, step):
    if isinstance(value, dict):
        value = add_dict(value, step + 1)

    status = step * '    ' + status
    value = get_bool_text(value)
    result_str = f'{status}{key}: {value}\n'

    return result_str


def stylish(diff, step=0):
    keys = sorted(diff)
    result_str = '{\n'
    inner = '    '

    for key in keys:
        if diff[key][0] == 'nested':
            _step = step + 1
            new_str = f'{_step * inner}{key}: {stylish(diff[key][1], _step)}'
            result_str += new_str
        elif diff[key][0] == 'added':
            result_str += add_string('  + ', key, diff[key][1], step)
        elif diff[key][0] == 'deleted':
            result_str += add_string('  - ', key, diff[key][1], step)
        elif diff[key][0] == 'same':
            result_str += add_string('    ', key, diff[key][1], step)
        elif diff[key][0] == 'modified':
            result_str += add_string('  - ', key, diff[key][1], step)
            result_str += add_string('  + ', key, diff[key][2], step)

    result_str += step * inner + '}'

    if step > 0:
        result_str += '\n'
    return result_str
