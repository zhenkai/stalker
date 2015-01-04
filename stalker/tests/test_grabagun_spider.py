import unittest
from stalker.spiders.grabagun import GrabagunSpider
from responses import fake_response_from_file


class GrabagunSpiderTestCase(unittest.TestCase):
    def setUp(self):
        self.spider = GrabagunSpider()

    def test_parse_item_normal(self):
        fake_response = fake_response_from_file(file_name="grabagun_product.html", url="http://grabagun.com/aac-aac-1911-enhanced.html")
        item = self.spider.parse_item(fake_response)
        self.assertEquals(item['headline'], "Advanced Armament Corp 1911 - Enhanced 96338 Online Gun Store".encode('utf-8'))
        self.assertEquals(item['img'], "http://grabagun.com/media/catalog/product/cache/1/small_image/250x250/9df78eab33525d08d6e5fb8d27136e95/A/d/Advanced-Armament-AAC-1911-Enhanced-96338-885293963382.jpg.jpg")
        self.assertEquals(item['desc'], "AAC 1911 - Enhanced .45 ACP 5 Inch Threaded Barrel AAC Engraving Custom VZ Grips with AAC Logo Black Finish 8 Round")
        self.assertAlmostEqual(item['price'], 1025.24)
        self.assertFalse(item['oos'])

    def test_parse_item_multiple_price(self):
        fake_response = fake_response_from_file(file_name="grabagun_multiple_price.html", url="http://grabagun.com/amer-clsc-amigo-45acp-3-5-7rd-mbl.html")
        item = self.spider.parse_item(fake_response)
        self.assertAlmostEqual(item['price'], 512.96)
        self.assertFalse(item['oos'])

    def test_parse_item_oos(self):
        fake_response = fake_response_from_file(file_name="grabagun_oos.html", url="http://grabagun.com/eotech-512-tactical-std-aa-bttry.html")
        item = self.spider.parse_item(fake_response)
        self.assertTrue(item['oos'])
        self.assertAlmostEqual(item['price'], 429.00)

    def test_parse_item_sale(self):
        fake_response = fake_response_from_file(file_name="grabagun_click_for_price.html", url="http://grabagun.com/beretta-nano-9mm-3-07-6rd-blk-3dot.html")
        item = self.spider.parse_item(fake_response)
        self.assertFalse(item['oos'])
        self.assertAlmostEqual(item['price'], 372.73)

if __name__ == '__main__':
    unittest.main()
