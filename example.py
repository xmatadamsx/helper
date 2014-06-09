#!/usr/bin/env python
"""
"""

import argparse
import logging
import sys

__version__ = '0.0.1'

logging.basicConfig(level=logging.DEBUG)

class Widget(object):
    """
    """

    def __init__(self, args):
        logging.debug('widget init')
        self.someBool = args.someBool
        self.someInt = args.someInt
        self.theRest = args.theRest

    def run(self):
        logging.debug('widget run')
        print self.someBool
        print self.someInt
        print self.theRest


def main(args):
    """
    """
    parser = argparse.ArgumentParser(
        description='Description of script')
    parser.add_argument('-v', '--version', 
        action='version', version=__version__)
    parser.add_argument('-sb', '--someBool', 
        action='store_true', 
        help='A boolean value')
    parser.add_argument('-si', '--someInt', 
        type=int,
        help='An int value')
    parser.add_argument('theRest', nargs='*',
        type=str,
        help='the rest of the arguments')

    args = parser.parse_args(args)


    logging.debug('script running')

    widget = Widget(args)
    widget.run()

if __name__ == '__main__':
    main(sys.argv[1:] or 0)
