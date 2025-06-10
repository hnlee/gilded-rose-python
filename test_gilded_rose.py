# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Conjured", 5, 30), Item("Backstage passes to a TAFKAL80ETC concert", 7, 20)]
        gilded_rose = GildedRose(items)
        [print(item) for item in gilded_rose.items]
        gilded_rose.update_quality()
        print("After update:")
        [print(item) for item in gilded_rose.items]
        self.assertEqual(gilded_rose.items[0].quality, 28, "Conjured Support Isn't Working")
        self.assertEqual(gilded_rose.items[1].quality, 22, "Backstage passes Support is broken")
        gilded_rose.update_quality()
        [print(item) for item in gilded_rose.items]
        self.assertEqual(gilded_rose.items[0].quality, 26, "Conjured Support Isn't Working")
        self.assertEqual(gilded_rose.items[1].quality, 24, "Backstage passes Support is broken")
        
    def test_all_current_cases(self):
        items = [
            Item("Aged Brie", 2, 0),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Conjured", 3, 6),
            Item("Normal Item", 5, 10),
            Item("Aged Brie", -2, 10),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(gilded_rose.items[0].quality, 1, "Aged Brie should increase in quality")
        self.assertEqual(gilded_rose.items[1].quality, 21, "Backstage passes should increase in quality")
        self.assertEqual(gilded_rose.items[2].quality, 80, "Sulfuras should not change quality")
        self.assertEqual(gilded_rose.items[3].quality, 4, "Conjured items should decrease in quality")
        self.assertEqual(gilded_rose.items[4].quality, 9, "Normal items should decrease in quality")
        self.assertEqual(gilded_rose.items[5].quality, 11, "Aged Brie should still go up")
        
if __name__ == '__main__':
    unittest.main()
