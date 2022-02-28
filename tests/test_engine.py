from gendiff.engine import generate_diff

file1 = 'tests/fixtures/first.json'
file2 = 'tests/fixtures/second.json'
result_file = open('tests/fixtures/result.txt').read()


def test_engine():
    assert generate_diff(file1, file2) == result_file
