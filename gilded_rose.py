# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Handles quality
            if item.name != "Aged Brie" and item.name != "Backstage passes":
                # Normal, Conjured, Sulfuras
                if item.name == "Conjured":
                    # Conjured (to decrease by 2)
                    item.quality = max(item.quality - 2, 0)
                elif item.name != "Sulfuras":
                    # Normal
                    item.quality = max(item.quality - 1, 0)
            else:
                # Aged Brie, Backstage passes
                if item.quality < 50:
                    item.quality = item.quality + 1

                    if item.name == "Backstage passes":
                        if item.sell_in < 11 and item.quality < 50:
                            item.quality = item.quality + 1
                        if item.sell_in < 6 and item.quality < 50:
                            item.quality = item.quality + 1

            # Handles sell_in
            if item.name != "Sulfuras":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                # Past expiration
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes":
                        # Normal (to decrease), Conjured (to decrease), Sulfuras (to be constant)
                        if item.quality > 0:
                            # Quality shouldn't be negative
                            if item.name == "Conjured":
                                # Conjured (to decrease by 4 in total)
                                item.quality = max(item.quality - 2, 0)
                            elif item.name != "Sulfuras":
                                # Normal (to decrease by 2 in total)
                                item.quality = item.quality - 1

                    else:
                        item.quality = item.quality - item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
