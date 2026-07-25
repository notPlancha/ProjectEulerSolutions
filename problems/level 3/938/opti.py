from dataclasses import dataclass
from math import comb
from functools import cache
import sys
from sympy import Function
from tqdm import tqdm

sys.setrecursionlimit(10**8)

@cache
def prob_a(a, b):
  if a < 2:
    return 0
  return comb(a, 2) / comb(a + b, 2)

@cache
def prob_b(a, b):
  if b < 2:
    return 0
  return comb(b, 2) / comb(a + b, 2)


@cache
def prob_c(a, b):
  if a < 1 or b < 1:
    return 0
  return comb(a, 1) * comb(b, 1) / comb(a + b, 2)

f = Function('f')

@cache
def prob(a,b):
  if a <= 0:
    return 1
  if b <= 0:
    return 0
  
  alpha = prob_a(a,b)
  beta = prob_b(a,b)
  gamma = prob_c(a,b)
  y = prob(a-2, b)
  z = prob(a, b-1)  
  return (gamma * z + alpha * y) / (1 - beta)

def main(a, b):
  for curr_a in tqdm(range(2, a + 1)):
    for curr_b in range(2, b + 1):
      prob(curr_a, curr_b)
  return prob(a, b)

if __name__ == "__main__":
  print(main(2,2))
  print(main(10,9))
  print(main(34, 25))
  print(main(24690, 12345))