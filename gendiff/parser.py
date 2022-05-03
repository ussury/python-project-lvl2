import json
import yaml


def parse(file):
    if file.suffix == '.json':
        with open(file) as f:
            parse_file = json.load(f)
    else:
        with open(file) as f:
            parse_file = yaml.safe_load(f)

    return parse_file
