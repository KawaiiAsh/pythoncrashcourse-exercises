import unittest
from cities import get_city_info


class Cities_Test(unittest.TestCase):

    def test_city_info(self):
        city_info = get_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')

    def test_city_info_population(self):
        city_info = get_city_info('santiago', 'chile', '50000')
        self.assertEqual(city_info, 'Santiago, Chile - population 50000')

    def test_city_info_no_population(self):
        city_info = get_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()