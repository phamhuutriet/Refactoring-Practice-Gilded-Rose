from gilded_rose_subclasses import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def is_backstage(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def gildedRose_item_factory(self, item):
        if self.is_aged_brie(item):
            return AgedBrieGildedRoseItem(item)
        elif self.is_backstage(item):
            return BackstageGildedRoseItem(item)
        elif self.is_sulfuras(item):
            return SulfuricGildedRoseItem(item)
        else:
            return NormalGildedRoseItem(item)

    def update_item(self, item, new_item):
        item.sell_in, item.quality = new_item.sell_in, new_item.quality

    def update_quality(self):
        for item in self.items:
            new_item = self.gildedRose_item_factory(item)
            new_item.update_quality()
            self.update_item(item, new_item)
    

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)