import sys
from functools import cache
from math import comb

import sympy
from sympy import Function

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


f = Function("f")


@cache
def prob(a, b):
  if a == 0:
    return 1
  if b == 0:
    return 0

  # x = ay + bx + cz

  y = prob(a - 2, b)
  x = f(a, b)  # here we use an undefined function to avoid infinite recursion
  z = prob(a, b - 1)

  ay = prob_a(a, b) * y
  bx = prob_b(a, b) * x
  cz = prob_c(a, b) * z
  expression = ay + bx + cz
  ret = sympy.solve(x - expression, x)
  assert len(ret) == 1

  return ret[0]


print(prob(2, 2))
print(prob(10, 9))
print(prob(34, 25))
print(prob(24690, 12345))
