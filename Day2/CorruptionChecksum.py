import os


def load_test_input(file_name):
    currentdir = os.path.dirname(os.path.realpath(__file__)) + '/' + file_name
    with open(currentdir, "r") as f:
        return [[int(n) for n in line.split()] for line in f.readlines()]


def get_difference(l):
    return int(max(l)) - int(min(l))


def calculate_checksum(data):
    return sum(get_difference(line) for line in data)


if __name__ == '__main__':
    testdata = load_test_input('input.txt')
    print calculate_checksum(testdata)
