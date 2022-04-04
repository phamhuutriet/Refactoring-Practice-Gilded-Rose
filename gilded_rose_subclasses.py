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
  