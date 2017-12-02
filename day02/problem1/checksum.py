#!/usr/bin/env python

"""A simple python script template.

"""

from __future__ import print_function
import os
import sys
import argparse

def read_matrix(infile):
    with infile as text:
         lines = [line.split() for line in text]
    return lines
    
def checksum_line(line):
    int_values = map(int,line)
    checksum = max(int_values) - min(int_values)
    return checksum

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)
    
    matrix = read_matrix(args.infile)
    checksum = 0
    for line in matrix:
        checksum += checksum_line(line)
    print(checksum)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))