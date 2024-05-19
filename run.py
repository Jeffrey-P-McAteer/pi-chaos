#!/usr/bin/env python

import os
import sys
import math
import subprocess

pyenv = os.path.join(os.path.dirname(__file__), 'pyenv')
os.makedirs(pyenv, exist_ok=True)
sys.path.append(pyenv)

numba_cache_dir = os.path.join(os.path.dirname(__file__), 'numba-cache')
os.makedirs(numba_cache_dir, exist_ok=True)
os.environ['NUMBA_CACHE_DIR'] = numba_cache_dir

try:
  import numba
except:
  subprocess.run([
    sys.executable, '-m', 'pip', 'install', f'--target={pyenv}', 'numba'
  ])
  import numba

@numba.jit(nopython=True)
def leibniz_seq(k):
  return (( (-1) ** k ) * 4.0 ) / ((2*k) + 1)

@numba.jit(nopython=True, fastmath=True, cache=True)
def leibniz_sum_to(term_num):
  return sum([leibniz_seq(k) for k in range(0, term_num)])

def main(args=sys.argv):
  print(f'leibniz_sum_to(250000) = {leibniz_sum_to(250000)}')




if __name__ == '__main__':
  main()

