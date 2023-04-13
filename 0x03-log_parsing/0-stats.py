#!/usr/bin/python3
"""This Script Parses HTTP request logs.
"""
import re


def extract_data(input_line):
    """Extracts line sections from an HTTP request log.
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_format, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(file_sizes, status_codes):
    """Prints Statics
    """
    print('File size: {:d}'.format(file_sizes), flush=True)
    for status_code in sorted(status_codes.keys()):
        num = status_codes.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def pass_info(line, file_sizes, status_codes):
    """Updates logs.
    """
    line_info = extract_data(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes.keys():
        status_codes[status_code] += 1
    return file_sizes + line_info['file_size']


def run():
    """Starts the log parser.
    """
    line_num = 0
    file_sizes = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_sizes = pass_info(
                line,
                file_sizes,
                status_codes,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(file_sizes, status_codes)
    except (KeyboardInterrupt, EOFError):
        print_statistics(file_sizes, status_codes)


if __name__ == '__main__':
    run()
