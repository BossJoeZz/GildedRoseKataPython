# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # According to the description provided in the readme, Aged Brie is a backstage pass, and its quality should be reduced to 0 after the concert. However, in the original code, this is an incorrect test (indicating that the logic of the original code does not reduce the quality to 0)
    def test_aged_brie(self):
        Aged_Brie = "Aged Brie"
        items = [Item(Aged_Brie, -1, 20)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(0, items[0].quality)

    # According to the description provided in the readme, Sulfuras is a legendary item and as such its Quality is 80 and it never alters. Therefore, the quality should return to 80, however, in the original code, this is an incorrect test (indicating that the logic of the original code does not fix the quality at 80)
    def test_sulfuras(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 75)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(80, items[0].quality)

    # According to the description provided in the readme, "Conjured" items degrade in Quality twice as fast as normal items. Therefore, the quality should be 10-2=8 after one day. However, in the original code, this is an incorrect test (indicating that the logic of the original code does not achieve a faster quality reduction speed for conjured items)
    def test_conjured(self):
        conjured = "Conjured Mana Cake"
        items = [Item(conjured, 5, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(8, items[0].quality)

    # The above 3 incorrect tests will be successfully passed by modifying the original code and applying the design pattern strategy.
if __name__ == '__main__':
    unittest.main()
