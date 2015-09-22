#!/usr/bin/env python3

import re
import sys
import argparse
import urllib.request
import urllib.error


def get_parser():
    """
    Build an argument parser.
    """
    parser = argparse.ArgumentParser(description='Add a new press review entry.')
    parser.add_argument('date', help='The publication date (YYYY-MM-DD)')
    parser.add_argument('publisher', help='The publisher, e.g. "20 Minuten" or "NZZ"')
    parser.add_argument('title', help='The publication title')
    parser.add_argument('url', help='The URL')
    parser.add_argument('-d', '--dry-run', action='store_true', default=False,
            help='Only print press review entry, don\'t save it')
    parser.add_argument('-f', '--force', action='store_true', default=False,
            help='Skip validation')
    return parser


class Validator:
    """
    A class to validate the arguments.
    """
    def __init__(self, args):
        self.args = args

    def _validate_date(self):
        year_re = r'(19|20)\d\d'
        month_re = r'(0[1-9]|1[012])'
        day_re = r'(0[1-9]|[12][0-9]|3[01])'
        if not re.match('^%s-%s-%s$' % (year_re, month_re, day_re), self.args.date):
            print('Invalid date: %s' % self.args.date)
            print('Date must be in the YYYY-MM-DD format.')
            sys.exit(1)

    def _validate_url(self):
        try:
            urllib.request.urlopen(self.args.url)
        except urllib.error.URLError as e:
            print('Invalid or dead URL: %s' % self.args.url)
            print(str(e))
            sys.exit(1)

    def validate(self):
        self._validate_date()
        self._validate_url()


if __name__ == '__main__':

    # Parse arguments
    parser = get_parser()
    args = parser.parse_args()

    # Validate arguments
    if not args.force:
        v = Validator(args)
        v.validate()
