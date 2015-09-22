#!/usr/bin/env python3

import argparse
import io
import re
import sys
import unicodedata
import urllib.error
import urllib.request


class PressReview:
    """
    Model for a press review entry.
    """
    _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

    def __init__(self, date, publisher, title, url):
        self.date = date
        self.publisher = publisher
        self.title = title
        self.url = url
        self.lang = 'de'

    @property
    def slug(self):
        result = []
        for word in self._punct_re.split(self.publisher.lower()):
            word = unicodedata.normalize('NFKD', word)
            if word:
                result.append(word)
        slug = '%s_%s' % (self.date, '-'.join(result))
        return slug.encode('ascii', 'ignore').decode('ascii')

    def get_text(self):
        text = io.StringIO()
        text.write('Title: %s\n' % self.title)
        text.write('Slug: %s\n' % self.slug)
        text.write('Date: %s\n' % self.date)
        text.write('Lang: %s\n' % self.lang)
        text.write('Publisher: %s\n' % self.publisher)
        text.write('Ext_url: %s' % self.url)
        return text.getvalue()


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

    # Create press review entry
    pr = PressReview(args.date, args.publisher, args.title, args.url)
    text = pr.get_text()

    if args.dry_run:
        print(text)
    else:
        print('Generating %s...' % 'NOT YET IMPLEMENTED')
