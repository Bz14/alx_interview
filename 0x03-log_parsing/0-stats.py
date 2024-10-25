#!/usr/bin/python3
""" Log parsing """
import sys
import re


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
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')
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
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                count += 1
                status = match.group(1)
                size = int(match.group(2))
                file_size += size
                if status.isDecimal():
                    status_codes[status] += 1
                
                if count % 10 == 0:
                    print_stats(file_size, status_codes)
    finally:
        print_stats(file_size, status_codes)
