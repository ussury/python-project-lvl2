import json


def generate_diff(data1, data2):
    first_file = json.load(open(data1))
    second_file = json.load(open(data2))
    keys = sorted(first_file.keys() | second_file.keys())
    result_list = []
    for key in keys:
        if key not in first_file:
            result_list.append(f' + {key}: {second_file[key]}')
        elif key not in second_file:
            result_list.append(f' - {key}: {first_file[key]}')
        elif second_file[key] == first_file[key]:
            result_list.append(f'   {key}: {first_file[key]}')
        else:
            result_list.append(f' - {key}: {first_file[key]}')
            result_list.append(f' + {key}: {second_file[key]}')

    return '{\n ' + '\n '.join(result_list) + '\n}'
