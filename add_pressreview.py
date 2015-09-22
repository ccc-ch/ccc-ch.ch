#!/usr/bin/env python3
import argparse


def get_parser():
    """
    Build an argument parser.
    """
    parser = argparse.ArgumentParser(description='Add a new press review entry.')
    parser.add_argument('date', nargs=1, help='The publication date (YYYY-MM-DD)')
    parser.add_argument('publisher', nargs=1, help='The publisher, e.g. "20 Minuten" or "NZZ"')
    parser.add_argument('title', nargs=1, help='The publication title')
    parser.add_argument('url', nargs=1, help='The URL')
    parser.add_argument('-d', '--dry-run', action='store_true', default=False,
            help='Only print press review entry, don\'t save it')
    return parser


if __name__ == '__main__':

    parser = get_parser()
    args = parser.parse_args()
