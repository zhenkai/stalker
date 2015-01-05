import mmh3
import unittest
from stalker.spiders.grabagun import GrabagunSpider
from responses import fake_response_from_file


class GrabagunSpiderTestCase(unittest.TestCase):
    def setUp(self):
        self.spider = GrabagunSpider()

    def test_parse_item_normal(self):
        fake_response = fake_response_from_file(file_name="grabagun_list.html")
        items = []
        for item in self.spider.parse_item(fake_response):
            items.append(item)

        self.assertEquals(len(items), 20)

        p0 = items[0]
        self.assertAlmostEqual(p0['price'], 799.00)
        self.assertEquals(p0['headline'], u'Adams Arms Arms UA-16-M-TEVO-556 Upper 5.56 16-inch MID T-EVO')
        self.assertFalse(p0['oos'])
        self.assertEquals(p0['url'], u'http://grabagun.com/ada-upper-tac-evo-mid-16.html')

        p7 = items[7]
        self.assertAlmostEqual(p7['price'], 599.00)
        self.assertEquals(p7['headline'], u'American Classic MAC 1911 BOBCUT .45ACP 8+1 Blue')
        self.assertEquals(p7['url'], u'http://grabagun.com/bersa-m19bc45b-1911-bobcat-pistol.html')
        self.assertFalse(p7['oos'])

        # click for price
        p18 = items[18]
        self.assertAlmostEqual(p18['price'], 551.91)


if __name__ == '__main__':
    unittest.main()
