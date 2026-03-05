from gilded_rose import Item, GildedRose
import pytest

def test_normal_item_degrades_quality_and_sellin():
    item = Item("+5 Dexterity Vest", 10, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    
    assert item.sell_in == 9
    assert item.quality == 19