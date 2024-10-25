#!/usr/bin/python3
""" Log parsing """
import sys


def print_stats(file_size, status_codes):
    """ Print stats """
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v:
            print("{}: {}".format(k, v))


def parse_line(line, file_size, status_codes):
    """ Parse line """
    try:
        data = line.split()
        file_size += int(data[-1])
        if data[-2] in status_codes:
            status_codes[data[-2]] += 1
        return file_size, status_codes
    except Exception:
        return file_size, status_codes


if __name__ == "__main__":
    file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            file_size, status_codes = parse_line(line, file_size, status_codes)
            if count == 10:
                print_stats(file_size, status_codes)
                count = 0
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats(file_size, status_codes)
