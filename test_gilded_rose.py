# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual([(item.sell_in, item.quality) for item in items], [(0, 1), (8, 18), (3, 5)])

    def test_aged_brie_should_increase_in_quality(self):
        elixir = "Elixir of the Mongoose"
        items = [Item(elixir, 1, 2), Item(elixir, 3, 4), Item(elixir, 5, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual([(item.sell_in, item.quality) for item in items], [(1, 2), (3, 2), (5, 6)])

    def test_sulfuras_should_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 1, 2), Item(sulfuras, 5, 2)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual([(item.sell_in, item.quality) for item in items], [(3, 4), (9, 10)])

    def test_backstage_pass_increases_in_quality(self):
        backstage = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(backstage, 3, 3), Item(backstage, 5, 1), Item(backstage, 2, 3)]
        gr = GildedRose(items)
    
        gr.update_quality()

        self.assertEqual([(item.sell_in, item.quality) for item in items], [(1, 2), (3, 4), (5, 6)])

    def test_backstage_pass_quality_drops_to_zero(self):
        cake = "Conjured Mana Cake"
        items = [Item(cake, 1, 2), Item(cake, 3, 4)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual([(item.sell_in, item.quality) for item in items], [(0, 1), (1, 2)])

if __name__ == '__main__':
    unittest.main()
