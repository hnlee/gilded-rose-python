# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 15, 20)]
        gilded_rose = GildedRose(items)
        for _ in range(16):
            gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

        # Test zero boundary condition
        for _ in range(2):
            gilded_rose.update_quality()

        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 50, 0)]
        gilded_rose = GildedRose(items)
        for _ in range(51):
            gilded_rose.update_quality()

        # For "Aged Brie" (50 limit)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        for _ in range(10):
            gilded_rose.update_quality()

        # For "Sulfuras"
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes(self):
        items = [Item("Backstage passes", 15, 35)]
        gilded_rose = GildedRose(items)

        for _ in range(7):
            gilded_rose.update_quality()

        self.assertEqual(8, items[0].sell_in)
        self.assertEqual(40 + 4, items[0].quality)

        for _ in range(5):
            gilded_rose.update_quality()

        # For "Sulfuras"
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

        for _ in range(4):
            gilded_rose.update_quality()

        # For "Sulfuras" (Zero boundary plus loss of value)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured", 7, 20)]
        gilded_rose = GildedRose(items)
        for _ in range(8):
            gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

        # Test zero boundary condition
        for _ in range(2):
            gilded_rose.update_quality()

        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == "__main__":
    unittest.main()
