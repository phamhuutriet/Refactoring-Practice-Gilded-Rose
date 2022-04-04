from pyparsing import GoToColumn


class GildedRoseItem:
  def __init__(self, item):
      self.sell_in = item.sell_in
      self.quality = item.quality

  def update_quality(self):
    self.handle_quality()
    self.handle_sellin()

  def handle_quality(self):
    pass

  def handle_sellin(self):
    pass

class NormalGildedRoseItem(GildedRoseItem):
  def handle_quality(self):
      self.quality = max(0, self.quality - 1)

  def handle_sellin(self):
      self.sell_in = self.sell_in - 1
      if self.sell_in < 0:
          self.quality = max(0, self.quality - 1)

class AgedBrieGildedRoseItem(GildedRoseItem):
  def handle_quality(self):
      self.quality = min(50, self.quality + 1)

  def handle_sellin(self):
      self.sell_in = self.sell_in - 1
      if self.sell_in < 0:
          self.quality = min(50, self.quality + 1)

class BackstageGildedRoseItem(GildedRoseItem):
  def handle_quality(self):
      self.quality = self.quality + 1
      if self.sell_in < 11:
          self.quality = self.quality + 1
      if self.sell_in < 6:
          self.quality = self.quality + 1
      self.quality = min(50, self.quality)
  
  def handle_sellin(self):
      self.sell_in = self.sell_in - 1
      if self.sell_in < 0:
          self.quality = 0

class SulfuricGildedRoseItem(GildedRoseItem):
  def handle_quality(self):
      return 

  def handle_sellin(self):
      return 