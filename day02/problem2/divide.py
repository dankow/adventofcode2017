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
    
def sort_line(line):
    int_values = map(int,line)
    int_values.sort()
    return int_values

def divide(line):
    for a in reversed(line):
        for b in line:
            if a % b == 0 and a != b:
                break
        else:
            continue
        break
        
#     print("a = %d, b = %d, a/b = %d\n" % (a,b,a / (b * 1.0)))
    return a / b

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
        sorted = sort_line(line)
#         print(sorted)
        checksum += divide(sorted)

    print(checksum)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))