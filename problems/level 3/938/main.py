from dataclasses import dataclass
@dataclass
class Deck:
  n_red: int
  n_black: int

  def take_2_red(self) -> "Deck":
    return Deck(self.n_red - 2, self.n_black)

  def take_2_black(self) -> "Deck":
    return Deck(self.n_red - 2, self.n_black)
  
  def take_1_each(self) -> "Deck":
    return Deck(self.n_red - 1, self.n_black - 1)

  @property
  def all_red(self):
    return self.n_black <= 0 and self.n_red > 0
  @property
  def all_black(self):
    return self.n_red <= 0 and self.n_black > 0
  
# %% 
# calculate tree and check which ones are all black
out = {
  "all_red_n" : 0,
  "all_black_n": 0
}

def reset_out():
  global out
  out = {
    "all_red_n" : 0,
    "all_black_n": 0
  }

def simulate(deck: Deck):
  if deck.all_red:
    out["all_red_n"] += 1
    return
  elif deck.all_black:
    out["all_black_n"] += 1
    return
  else:
    # deck.take_2_black() path
    if deck.all_black

reset_out()
simulate(Deck(2,2))
print(out)
# %% 
print(0.4666666667 / ((1/3)** 7))
print(1020.6000000729005/3)
# %%
