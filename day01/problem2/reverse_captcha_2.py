#!/usr/bin/env python

"""A simple python script template.
"""

from __future__ import print_function
import os
import sys
import argparse

def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
def sum_seq(infile):
    sum = 0
    sequence_raw = []
    map(sequence_raw.extend, infile.readline())
    sequence = filter(lambda n: is_int(n), sequence_raw)
#     print(sequence)
    length = len(sequence)
    offset = length / 2
#     print("length = %s, offset = %s" % (length, offset))
    offset = len(sequence) / 2
    for i in range(0,len(sequence)):
        if sequence[i] == sequence[(i+offset)%length]:
            sum += int(sequence[i])
    return sum

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)

    print(sum_seq(args.infile))
    args.infile.close()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))