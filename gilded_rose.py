class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def is_normal_item(self, item):
        return item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros"

    def handle_quality_normal(self, item):
        item.quality = max(0, item.quality - 1)

    def handle_sellin_normal(self, item):
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 1)

    def is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def handle_quality_aged_brie(self, item):
        item.quality = min(50, item.quality + 1)

    def handle_sellin_aged_brie(self, item):
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 1)

    def is_backstage(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def handle_quality_backstage(self, item):
        item.quality = item.quality + 1
        if item.sell_in < 11:
            item.quality = item.quality + 1
        if item.sell_in < 6:
            item.quality = item.quality + 1
        item.quality = min(50, item.quality)

    def handle_sellin_backstage(self, item):
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def update_quality(self):
        for item in self.items:
            # Sulfuras quality never change
            # Item's not Aged Brie or Backstage will decrease its quality by 1 each day
            if self.is_normal_item(item):
                self.handle_quality_normal(item)
                self.handle_sellin_normal(item)

            if self.is_aged_brie(item):
                self.handle_quality_aged_brie(item)
                self.handle_sellin_aged_brie(item)

            # Item's Aged Brie or Backstage
            if self.is_backstage(item):
                self.handle_quality_backstage(item)
                self.handle_sellin_backstage(item)

            if self.is_sulfuras(item):
                continue


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)