#!/bin/bash

echo -e 'Enter first integer'
read a

echo -e 'Enter second integer'
read b

python calculate.py --first_integer $a --second_integer $b