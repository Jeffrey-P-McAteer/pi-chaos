#!/usr/bin/env python

import os
import sys
import math

def leibniz_seq(k):
  return (( (-1) ** k ) * 4.0 ) / ((2*k) + 1)

def leibniz_sum_to(term_num):
  return sum([leibniz_seq(k) for k in range(0, term_num)])

def main(args=sys.argv):
  print(f'leibniz_sum_to(250000) = {leibniz_sum_to(250000)}')




if __name__ == '__main__':
  main()

