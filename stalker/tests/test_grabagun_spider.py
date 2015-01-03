import unittest
from stalker.spiders.grabagun import GrabagunSpider
from responses import fake_response_from_file


class GrabagunSpiderTestCase(unittest.TestCase):
    def setUp(self):
        self.spider = GrabagunSpider()

    def test_parse_item(self):
        fake_response = fake_response_from_file(file_name="grabagun_product.html", url="http://grabagun.com/aac-aac-1911-enhanced.html")
        item = self.spider.parse_item(fake_response)
        self.assertEquals(item['headline'], "Advanced Armament Corp 1911 - Enhanced 96338 Online Gun Store")
        self.assertEquals(item['img'], "http://grabagun.com/media/catalog/product/cache/1/small_image/250x250/9df78eab33525d08d6e5fb8d27136e95/A/d/Advanced-Armament-AAC-1911-Enhanced-96338-885293963382.jpg.jpg")
        self.assertEquals(item['desc'], "AAC 1911 - Enhanced .45 ACP 5 Inch Threaded Barrel AAC Engraving Custom VZ Grips with AAC Logo Black Finish 8 Round")
        self.assertEquals(item['price'], "$1025.55")
    def test(self):
      self.assertEquals(1,2)


if __name__ == '__main__':
    unittest.main()
