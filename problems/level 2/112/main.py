# %%
from more_itertools import peekable

def is_increasing(number):
  it = peekable(str(number))
  try:
    for s in it:
      if s > it.peek():
        return False
  except StopIteration:
    return True

def is_decreasing(number):
  it = peekable(str(number))
  try:
    for s in it:
      if s < it.peek():
        return False
  except StopIteration:
    return True
  
def is_bouncy(number):
  return not is_increasing(number) and not is_decreasing(number)

print(
  (is_increasing(134468), not is_decreasing(134468), not is_bouncy(134468)),
  (not is_increasing(66420), is_decreasing(66420), not is_bouncy(66420)),
  (not is_increasing(155349), not is_decreasing(155349), is_bouncy(155349))
)
# %% 
def least_number_bouncy_p(porpotion, timeout=1_000_000):
  bouncy_n = 0
  for i in range(1, timeout):
    if is_bouncy(i):
      bouncy_n += 1
    if bouncy_n/i == porpotion:
      return i

print(least_number_bouncy_p(0.5, timeout=1000))

# %%
print(least_number_bouncy_p(0.99, timeout=1_000_000_000))