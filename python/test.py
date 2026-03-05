from gilded_rose import Item, GildedRose
import pytest

def test_normal_item_degrades_quality_and_sellin():
    item = Item("+5 Dexterity Vest", 10, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    
    assert item.sell_in == 9
    assert item.quality == 19

def test_normal_item_degrades_quality_and_sellin():
    item = Item("+5 Dexterity Vest", 10, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    
    assert item.sell_in == 9
    assert item.quality == item.quality.min(0) & item.quality.max(50)

def test_normal_item_aged_brie():
    item = Item("Aged Brie", 0+1, quality=0+1 )
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

def test_normal_item_Sulfuras():
    item = Item("Sulfuras", 0, 50 )
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    