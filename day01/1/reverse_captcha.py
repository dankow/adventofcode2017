#!/usr/bin/env python

"""A simple python script template.
"""

from __future__ import print_function
import os
import sys
import argparse

def sum_seq(infile):
    sum = 0
    sequence = []
    
    map(sequence.extend, infile.readline())
#     print(sequence)
#     print("length = %s" % len(sequence))
    for i in range(0,len(sequence)-1):
        if sequence[i] == "\n":
            break
        elif sequence[i] == sequence[i+1]:
            sum += int(sequence[i])
        elif sequence[i+1] == "\n" and sequence[i] == sequence[0]:
            sum += int(sequence[i])
#         print(i, sequence[i], sum)
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