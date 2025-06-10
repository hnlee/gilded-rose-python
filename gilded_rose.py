# -*- coding: utf-8 -*-
import argparse

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            if item.name == 'Conjured':
                
                if item.sell_in > 0:
                    item.quality = max(item.quality - 2, 0)
                else:
                    item.quality = max(item.quality - 4, 0)
                item.sell_in -= 1
                continue
            
            
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                    
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gilded Rose")
    parser.add_argument("--name", type=str, help="Name of the item")
    parser.add_argument("--sell-in", type=int, help="Sell in days")
    parser.add_argument("--quality", type=int, help="Quality of the item")
    parser.add_argument("--days", type=int, default=1, help="Number of days")
    args = parser.parse_args()

    item = Item(args.name, args.sell_in, args.quality)
    print(f"Day 0: {item.name}, sell in {item.sell_in} days, {item.quality} quality")
    gilded_rose = GildedRose([item])
    for n in range(args.days):
        gilded_rose.update_quality()
        print(f"Day {n+1}: {item.name}, sell in {item.sell_in} days, {item.quality} quality")
