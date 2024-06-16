#!/usr/bin/python3
"""Log Parser"""
import sys

if __name__ == '__main__':
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """ Print statistics """
        print('File size: {}'.format(file_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_line(line):
        """ Checks the line for matches """
        global file_size
        try:
            parts = line.split()
            if len(parts) < 7:
                return
            # Extract file size and status code
            size = int(parts[-1])
            code = int(parts[-2])
            file_size += size
            if code in status_codes:
                status_codes[code] += 1
        except Exception:
            pass

    linenum = 0
    try:
        for line in sys.stdin:
            parse_line(line)
            linenum += 1
            if linenum % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
