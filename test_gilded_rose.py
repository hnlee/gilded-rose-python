# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Conjured", 5, 30), Item("Backstage passes to a TAFKAL80ETC concert", 7, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 28, "Conjured Support Isn't Working")
        self.assertEqual(gilded_rose.items[1].quality, 22, "Backstage passes Support is broken")
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 26, "Conjured Support Isn't Working")
        self.assertEqual(gilded_rose.items[1].quality, 25, "Backstage passes Support is broken")
        
    def test_aged_brie(self):
        """
            Test 1. Aged Brie should increase in quality as it gets older.
            Test 2. It should not exceed 50 quality score.
            Test 3. If it is past its sell_in date, it should still increase in quality.
        """
        test_case_1 = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(test_case_1)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 11, "Aged Brie should increase in quality as it gets older")
        
        test_case_2 = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(test_case_2)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50, "Aged Brie can get 50 quality score")
        gilded_rose.update_quality()  # Update again to check max quality
        self.assertEqual(gilded_rose.items[0].quality, 50, "Aged Brie should not exceed 50 quality score")
    
    def test_conjured_items(self):
        """
            Test 1. Conjured items should decrease in quality twice as fast as normal items.
            Test 2. If it is past its sell_in date, it should decrease in quality four times as fast.
        """
        
        test_case_1 = [Item("Conjured", 5, 30)]
        gilded_rose = GildedRose(test_case_1)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 28, "Conjured items should decrease in quality twice as fast")
        gilded_rose.update_quality()  # Update again to check quality after another day
        self.assertEqual(gilded_rose.items[0].quality, 26, "Conjured items should decrease in quality twice as fast")
        
        test_case_2 = [Item("Conjured", 0, 30)]
        gilded_rose = GildedRose(test_case_2)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 26, "Conjured items should decrease in quality four times as fast after sell_in date")
    
    def test_backstage_passes(self):
        """
            Test 1. Backstage passes should increase in quality as the sell_in date approaches.
            Test 2. If the sell_in date is less than 11 days, it should increase by 2.
            Test 3. If the sell_in date is less than 6 days, it should increase by 3.
            Test 4. If the sell_in date is 0 or less, the quality should drop to 0.
            Test 5. Backstage passes should not exceed 50 quality score.
        """
        test_case_1 = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(test_case_1)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 21, "Backstage passes should increase in quality as sell_in date approaches")
        
        test_case_2 = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(test_case_2)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 22, "Backstage passes should increase by 2 when sell_in is less than 11 days")
        
        test_case_3 = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 20)]
        gilded_rose = GildedRose(test_case_3)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 25, "Backstage passes should increase by 3 when sell_in is less than 6 days")
        
        test_case_4 = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        gilded_rose = GildedRose(test_case_4)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 0, "Backstage passes should drop to 0 when sell_in is 0 or less")
        
        test_case_5 = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(test_case_5)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50, "Backstage passes should not exceed 50 quality score")
            
    def test_sulfuras(self):
        """
            Test 1. Sulfuras should always have a quality of 80.
        """
        test_case_1 = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(test_case_1)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 80, "Sulfuras should always have a quality of 80")
        gilded_rose.update_quality()  # Update again to check quality remains the same
        self.assertEqual(gilded_rose.items[0].quality, 80, "Sulfuras quality should not change")
        
    def test_normal_items(self):
        """
            Test 1. Normal items should decrease in quality by 1 each day.
            Test 2. If the sell_in date is past, it should decrease by 2.
            Test 3. Quality should not go below 0.
        """
        test_case_1 = [Item("Normal Item", 5, 20)]
        gilded_rose = GildedRose(test_case_1)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 19, "Normal items should decrease in quality by 1 each day")
        
        test_case_2 = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(test_case_2)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 18, "Normal items should decrease in quality by 2 after sell_in date")
        
        test_case_3 = [Item("Normal Item", 0, 1)]
        gilded_rose = GildedRose(test_case_3)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 0, "Normal items quality should not go below 0")
        
    def test_sell_in_decrease(self):
        """
            Test 1. All items should decrease their sell_in value by 1 each day.
            Test 2. If the item is past its sell_in date, it should still decrease.
        """
        test_case_1 = [Item("Normal Item", 5, 20), Item("Aged Brie", 5, 10), Item("Backstage passes to a TAFKAL80ETC concert", 5, 20), Item("Conjured", 5, 30)]
        gilded_rose = GildedRose(test_case_1)
        gilded_rose.update_quality()
        for item in gilded_rose.items:
            print(item)
            self.assertEqual(item.sell_in, 4, "Sell_in should decrease by 1 each day")
        gilded_rose.update_quality()
        for item in gilded_rose.items:
            self.assertEqual(item.sell_in, 3, "Sell_in should decrease by 1 each day")
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        for item in gilded_rose.items:
            self.assertEqual(item.sell_in, -1, "Sell_in should still decrease after sell_in date has passed")
        
if __name__ == '__main__':
    unittest.main()
