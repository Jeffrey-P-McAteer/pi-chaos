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

@numba.jit(nopython=True, fastmath=True, cache=True)
def leibniz_seq(k):
  return (( (-1) ** k ) * 4.0 ) / ((2*k) + 1)

@numba.jit(nopython=True, fastmath=True, cache=True)
def leibniz_sum_to(term_num):
  return sum([leibniz_seq(k) for k in range(0, term_num)])


#@numba.jit(nopython=True, fastmath=True, cache=True)
@numba.jit(nopython=False, fastmath=False, cache=False)
def leibniz_squared_seq(k):
  value = ( (( (-1) ** k ) * 4.0 ) / ((2*k) + 1) ) ** ( (( (-1) ** k ) * 4.0 ) / ((2*k) + 1) )
  if isinstance(value, complex):
    return value
  if not math.isnan(value):
    return complex(value, 0.0)
  return complex(0.0, 0.0)

@numba.jit(nopython=False, fastmath=False, cache=False)
def leibniz_squared_sum_to(term_num):
  complex_values = [leibniz_squared_seq(k) for k in range(0, term_num)]
  complex_sum = sum([v.real for v in complex_values])
  imaginary_sum = sum([v.imag for v in complex_values])
  return (complex_sum, imaginary_sum)


def main(args=sys.argv):
  leibniz_num_terms = 5000000
  leibniz_pi_approx = leibniz_sum_to(leibniz_num_terms)
  print(f'leibniz_sum_to({leibniz_num_terms}) = {leibniz_pi_approx}')

  pi_squared_approx = leibniz_pi_approx ** leibniz_pi_approx
  print(f'pi_squared_approx = {pi_squared_approx}')

  leibniz_squared_pi_approx = leibniz_squared_sum_to(leibniz_num_terms)
  print(f'leibniz_squared_pi_approx = {leibniz_squared_pi_approx}')







if __name__ == '__main__':
  main()

