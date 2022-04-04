import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items) 
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_quality_normal_unexpired_sellin(self):
        items = [Item("Sword", 4, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_quality_normal_expired_sellin(self):
        items = [Item("Sword", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_quality_agedBrie_lower50_unexpired_sellin(self):
        items = [Item("Aged Brie", 4, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_agedBrie_lower50_expired_sellin(self):
        items = [Item("Aged Brie", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)
    
    def test_quality_agedBrie_equal50_unexpired_sellin(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_agedBrie_equal50_expired_sellin(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_backstage_quality_lower50_sellin_higher10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_backstage_quality_lower50_sellin_lower10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)
    
    def test_quality_backstage_quality_lower50_sellin_lower5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_quality_backstage_quality_equal50_sellin_higher10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_backstage_quality_equal50_sellin_lower10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_backstage_quality_equal50_sellin_lower5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_backstage_quality_equal50_expired_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_backstage_quality_lower50_expired_sellin(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sellin_normal(self):
        items = [Item("Sword", 4, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)

    def test_sellin_agedBrie(self):
        items = [Item("Aged Brie", 4, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)

    def test_sellin_backstage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_quality_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)

    def test_sellin_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        
        
if __name__ == '__main__':
    unittest.main()