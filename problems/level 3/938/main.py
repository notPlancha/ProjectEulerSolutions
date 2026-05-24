from dataclasses import dataclass
@dataclass
class Deck:
  n_red: int
  n_black: int
  
  @property
  def prob_red(self):
    return self.n_red/(self.n_red + self.n_black)
  @property
  def prob_black(self):
    return 1-self.prob_red

  @property
  def take_red(self) -> "Deck":
    return Deck(self.n_red - 1, self.n_black)
  @property
  def take_black(self) -> "Deck":
    return Deck(self.n_red, self.n_black - 1)
  
  @property
  def prob_both_red(self):
    return self.prob_red * self.take_red.prob_red
  @property
  def prob_both_black(self):
    return self.prob_black * self.take_black.prob_black
  @property
  def prob_one_or_other(self):
    return (self.prob_red * self.take_red.prob_black + self.prob_black * self.take_black.prob_red)/2
  
  @property
  def all_red(self):
    return self.n_black == 0 and self.n_red > 0
  @property
  def all_black(self):
    return self.n_red == 0 and self.n_black > 0