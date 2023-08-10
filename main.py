import sys

from extract_pypdf2 import extract_surf_from_invoice

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('missing argument invoice file')
    else:
        bytes_used, usage_per_day = extract_surf_from_invoice(sys.argv.pop())
        for dt, bytes_used_that_day in usage_per_day.items():
            print(f'{dt} {bytes_used_that_day / (1024 * 1024 * 1024):.3} gb used')
        print(f'Total {bytes_used / (1024 * 1024 * 1024):.3} gb used')
