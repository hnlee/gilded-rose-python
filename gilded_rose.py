# -*- coding: utf-8 -*-
import argparse

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # for item in self.items:
        #     if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
        #         if item.quality > 0:
        #             if item.name != "Sulfuras, Hand of Ragnaros":
        #                 item.quality = item.quality - 1
        #     else:
        #         if item.quality < 50:
        #             item.quality = item.quality + 1
        #             if item.name == "Backstage passes to a TAFKAL80ETC concert":
        #                 if item.sell_in < 11:
        #                     if item.quality < 50:
        #                         item.quality = item.quality + 1
        #                 if item.sell_in < 6:
        #                     if item.quality < 50:
        #                         item.quality = item.quality + 1
        #     if item.name != "Sulfuras, Hand of Ragnaros":
        #         item.sell_in = item.sell_in - 1
        #     if item.sell_in < 0:
        #         if item.name != "Aged Brie":
        #             if item.name != "Backstage passes to a TAFKAL80ETC concert":
        #                 if item.quality > 0:
        #                     if item.name != "Sulfuras, Hand of Ragnaros":
        #                         item.quality = item.quality - 1
        #             else:
        #                 item.quality = item.quality - item.quality
        #         else:
        #             if item.quality < 50:
        #                 item.quality = item.quality + 1
        for item in self.items:
            updater = create_updater(item)
            updater.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



def create_updater(item):
    if item.name == "Aged Brie":
        return AgedBrieUpdater(item)
    if item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePassUpdater(item)
    if item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater(item)
    if item.name.startswith("Conjured"):
        return ConjuredUpdater(item)
    return NormalUpdater(item)

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_sell_in()
        self.update_quality()
        if self.item.sell_in < 0:
            self.update_quality_after_sell_in()
        self.cap_quality()
    
    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_quality(self):
        pass

    def update_quality_after_sell_in(self):
        pass

    def cap_quality(self):
        if self.item.quality > 50:
            self.item.quality = 50
        if self.item.quality < 0:
            self.item.quality = 0

class AgedBrieUpdater(ItemUpdater):
    def update_quality(self):
        self.item.quality += 1
    def update_quality_after_sell_in(self):
        self.item.quality += 1

class NormalUpdater(ItemUpdater):
    def update_quality(self):
        self.item.quality -= 1
    def update_quality_after_sell_in(self):
        self.item.quality -= 1

class BackstagePassUpdater(ItemUpdater):
    def update_quality(self):
        self.item.quality += 1
        if self.item.sell_in < 10:
            self.item.quality += 1
        if self.item.sell_in < 5:
            self.item.quality += 1
    def update_quality_after_sell_in(self):
        self.item.quality = 0

class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass
class ConjuredUpdater(ItemUpdater):
    def update_quality(self):
        self.item.quality -= 2
    def update_quality_after_sell_in(self):
        self.item.quality -= 2