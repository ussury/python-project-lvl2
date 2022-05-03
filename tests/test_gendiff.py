from gendiff.engine import generate_diff
from pathlib import Path


def get_fixture_path(file_name):
    current_dir = Path(__file__).parent
    return current_dir / 'fixtures' / file_name


plain_result_file = open(get_fixture_path('plain/plain.txt')).read()
nested_result_file = open(get_fixture_path('nested/stylish_diff.txt')).read()

plain_file1_json = get_fixture_path('plain/file1.json')
plain_file2_json = get_fixture_path('plain/file2.json')
plain_dicts_json = [plain_file1_json, plain_file2_json]

plain_file1_yaml = get_fixture_path('plain/file1.yaml')
plain_file2_yaml = get_fixture_path('plain/file2.yml')
plain_dicts_yaml = [plain_file1_yaml, plain_file2_yaml]

nested_file1_json = get_fixture_path('nested/file1.json')
nested_file2_json = get_fixture_path('nested/file2.json')
nested_dicts_json = [nested_file1_json, nested_file2_json]

nested_file1_yaml = get_fixture_path('nested/file1.yaml')
nested_file2_yaml = get_fixture_path('nested/file2.yml')
nested_dicts_yaml = [nested_file1_yaml, nested_file2_yaml]


def test_plain_diff():
    assert generate_diff(*plain_dicts_json) == plain_result_file
    assert generate_diff(*plain_dicts_yaml) == plain_result_file


def test_nested_diff():
    assert generate_diff(*nested_dicts_json) == nested_result_file
    assert generate_diff(*nested_dicts_yaml) == nested_result_file
