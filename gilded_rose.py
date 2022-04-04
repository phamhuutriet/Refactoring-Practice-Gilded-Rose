class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def is_normal_item(self, item):
        return item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros"

    def update_quality(self):
        for item in self.items:
            # Sulfuras quality never change
            # Item's not Aged Brie or Backstage will decrease its quality by 1 each day
            if self.is_normal_item(item):
                # The quality's never negative
                item.quality = max(0, item.quality - 1)

            # Item's Aged Brie or Backstage
            elif item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                # 50 is the maximum quality for each item
                # Increase by one each day
                item.quality = item.quality + 1
                # Backstage item will increase its quality rate as the sell in date is near
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    # quality will increase by 2 (add 1 more) if it's sell in days <= 10 
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                    # quality will increase more by 3 (add 1 more) if it's sell in days <= 5
                    if item.sell_in < 6:
                        item.quality = item.quality + 1
                item.quality = min(50, item.quality)

            # After dealing with quality, we'll handle sell in
            # If it's not sulfuras, its sell in date will decrease by one
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            # If it's passed the sell in date, normal item's quality will decrease by another 1 (2)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                # If it's normal item and sell in date has passed, its quality decrease by 2 (1 more)
                                item.quality = item.quality - 1
                    # If it's passed Backstage concert, item quality will be 0
                    else:
                        item.quality = item.quality - item.quality
                # If it's Aged Brie, it's quality keep getting better (twice as fast for increase and decrease?)
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)