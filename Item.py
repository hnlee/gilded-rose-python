class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
class ConjuredItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Conjured", sell_in, quality)

    def update_quality(self):
        if self.sell_in > 0:
            self.quality = max(self.quality - 2, 0)
        else:
            self.quality = max(self.quality - 4, 0)
            
        if self.quality > 50:
            self.quality = 50
        
class AgedBrieItem(Item):
    
    def __init__(self, sell_in, quality):
        super().__init__('Aged Brie', sell_in, quality)
        
    def update_quality(self):
        self.quality += 1
        if self.quality > 50:
            self.quality = 50

class BackStagePassesItem(Item):
    
    def __init__(self, sell_in, quality):
        super().__init__('Backstage passes to a TAFKAL80ETC concert', sell_in, quality)
        
    def update_quality(self):
        self.quality += 1
        if self.sell_in < 11:
            self.quality += 1
        if self.sell_in < 6:
            self.quality += 1
        self.quality = min(self.quality, 50)
        if self.sell_in < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50
            
class SulfurasItem(Item):
    
    def __init__(self, quality=80):
        super().__init__('Sulfuras, Hand of Ragnaros', 0, quality)

    def update_quality(self):
        pass  # Sulfuras does not change in quality or sell_in
    
class NormalItem(Item):
    
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        if self.sell_in < 0:
            self.quality -= 1
        self.quality = max(self.quality, 0)
        if self.quality > 50:
            self.quality = 50
        
class ItemFactory:
    @staticmethod
    def create_item(name, sell_in, quality):
        if name == "Conjured":
            return ConjuredItem(sell_in, quality)
        elif name == "Aged Brie":
            return AgedBrieItem(sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackStagePassesItem(sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItem(quality)
        else:
            return NormalItem(name, sell_in, quality)
        
class ItemController:
    def __init__(self, items):
        self.items = [ItemFactory.create_item(item.name, item.sell_in, item.quality) for item in items]

    def update_quality(self):
        
        for item in self.items:
            item.sell_in -= 1
            item.update_quality()
        return self.items
    
    def __repr__(self):
        return "\n".join(str(item) for item in self.items)