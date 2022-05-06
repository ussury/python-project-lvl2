from gendiff.diff import generate_diff
from pathlib import Path


def get_fixture_path(file_name):
    current_dir = Path(__file__).parent
    return current_dir / 'fixtures' / file_name


nested_result_file = open(get_fixture_path('stylish_diff.txt')).read()
plain_result_file = open(get_fixture_path('plain.txt')).read()

file1_json = get_fixture_path('file1.json')
file2_json = get_fixture_path('file2.json')
dicts_json = [file1_json, file2_json]

file1_yaml = get_fixture_path('file1.yaml')
file2_yaml = get_fixture_path('file2.yml')
dicts_yaml = [file1_yaml, file2_yaml]


def test_nested_diff():
    assert generate_diff(*dicts_json, 'stylish') == nested_result_file
    assert generate_diff(*dicts_yaml, 'stylish') == nested_result_file
    assert generate_diff(*dicts_json, 'plain') == plain_result_file
    assert generate_diff(*dicts_yaml, 'plain') == plain_result_file
