
#%% 
def is_palindrome(number):
  return list(str(number)) == list(reversed(str(number)))

is_palindrome(505)
# %%
def to_base2(number):
  return bin(number)[2:]

to_base2(585)
# %%
is_palindrome(to_base2(585))

# %%
ret = 0
for i in range(1_000_000):
  if is_palindrome(i) and is_palindrome(to_base2(i)):
    ret += i
    
print(ret)