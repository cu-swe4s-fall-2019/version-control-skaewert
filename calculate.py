""" Uses div and add functions from the math_lib.py file
"""
from math_lib import div
from math_lib import add
import argparse
import sys

parser = argparse.ArgumentParser(description = 'take two integer inputs and do math with them')
parser.add_argument('--first_integer', type = int, help = 'the first of two integers', required = True)
parser.add_argument('--second_integer', type = int, help = 'the second of two integers', required = True)
args = parser.parse_args()


a = args.first_integer
b = args.second_integer

print(div(a, b) + add(b, b))




