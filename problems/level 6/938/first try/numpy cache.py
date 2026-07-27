import sys
from functools import cache
from math import comb

import numpy as np
from tqdm import tqdm


import numpy as np
from functools import wraps


sentinel = np.int16(-1)


def array_cache(shape):
  cache_ = np.full(shape, sentinel, dtype=np.int16)

  def decorator(func):
    @wraps(func)
    def wrapper(a, b):
      value = cache_[a, b]
      if value != sentinel:
        return value

      value = func(a, b)
      cache_[a, b] = value
      return value

    wrapper.cache = cache_
    return wrapper

  return decorator


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


@array_cache((24691, 12346))
def prob(a, b):
  if a <= 0:
    return 1
  if b <= 0:
    return 0

  alpha = prob_a(a, b)
  beta = prob_b(a, b)
  gamma = prob_c(a, b)
  y = prob(a - 2, b)
  z = prob(a, b - 1)
  return (gamma * z + alpha * y) / (1 - beta)


def main(a, b):
  for curr_a in tqdm(range(2, a + 1)):
    for curr_b in range(2, b + 1):
      prob(curr_a, curr_b)
  return prob(a, b)


if __name__ == "__main__":
  print("main(2,2):", main(2, 2))
  print("main(10,9):", main(10, 9))
  print("main(34, 25):", main(34, 25))
  print("main(24690, 12345):", main(24690, 12345))
