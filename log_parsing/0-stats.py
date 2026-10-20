#!/usr/bin/python3
"""Module: Log Parsing"""
import re
import sys

def capture_lines():
    """Captures stdin lines"""
    input_format = r"^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(\.\d{1,6})?\] \"GET /projects/260 HTTP/1\.1\" \d{3} \d{1,4}$"

    i = 0
    split_line = []
    status_code = []
    file_size = 0

    try:
        while True:
            for line in sys.stdin:
                line = line.strip()
                if re.match(input_format, line):
                    split_line.append(line.split())
                    status_code.append(split_line[0][7])
                    file_size = file_size + int(split_line[0][8])
                    split_line.clear()
                    i += 1
                    if i == 10:
                        print_stats(status_code, file_size)
                        i = 0
                        status_code.clear()
                else:
                    continue
            print(status_code, file_size)
    except KeyboardInterrupt:
        print_stats(status_code, file_size)


def print_stats(status_code, file_size):
    """Prints stats of the captured stdin lines"""
    status_code.sort()
    print(f"File size: {file_size}")
 
    counts = {}
    for code in status_code:
        counts[code] = status_code.count(code)
    for code in counts:
        print(f"{code}: {counts[code]}")


if __name__ == "__main__":
    capture_lines()
