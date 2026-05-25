from dataclasses import dataclass
from math import comb

@dataclass
class Deck:
  n_red: int
  n_black: int

  def prob_A(self):
    if self.n_red < 2:
      return 0
    return comb(self.n_red, 2) / comb(self.n_red + self.n_black, 2)
  
  def prob_B(self):
    if self.n_black < 2:
      return 0
    return comb(self.n_black, 2) / comb(self.n_red + self.n_black, 2)

  def prob_C(self):
    if self.n_red < 1 or self.n_black < 1:
      return 0
    return comb(self.n_red, 1) * comb(self.n_black, 1) / comb(self.n_red + self.n_black, 2)
  
  @property
  def do_A(self) -> "Deck":
    return Deck(self.n_red - 2, self.n_black)
  
  @property
  def do_B(self) -> "Deck":
    return Deck(self.n_red, self.n_black)
  
  @property
  def do_C(self) -> "Deck":
    return Deck(self.n_red, self.n_black - 1)

  
def prob(deck: Deck):
  if deck.n_red == 0:
    return 1
  if deck.n_black == 0:
      return 0
  return deck.prob_A * prob(deck.do_A) + \
    deck.prob_B * prob(deck.do_B) + \
    deck.prob_C * prob(deck.do_C)