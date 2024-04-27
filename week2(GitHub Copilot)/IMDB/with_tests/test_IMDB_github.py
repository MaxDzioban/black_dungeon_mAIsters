import unittest

def test_find_films_with_keywords():
    film_keywords = {'gonki': ['nfs_mw', 'dark souls'], 'tututu': ['dark souls', 'fepeen'], 'yabko': ['fepeen', 'dark souls', 'nfs_mw'], 'gegege' : ['abc'], 'hi': ['dark room', 'nfs_mw', 'abc']}
    result = find_films_with_keywords(film_keywords, 4)
    expected_result = [('dark souls', 3), ('nfs_mw', 3), ('abc', 2), ('fepeen', 2)]
    assert result == expected_result

class TestFindFilmsWithKeywords(unittest.TestCase):
    def test_1(self):
        film_keywords = {'magic' : ['Duck Out (1927)', 'Film2'], 'comedy': ['Film2', 'Film3']}
        result = find_films_with_keywords(film_keywords, 2)
        expected_result = [('Film2', 2), ('Duck Out (1927)', 1)]
        self.assertEqual(result, expected_result)

    def test_2(self):
        film_keywords = {'action' : ['Film1', 'Film2'], 'adventure': ['Film2', 'Film3'], 'comedy': ['Film3', 'Film1']}
        result = find_films_with_keywords(film_keywords, 3)
        expected_result = [('Film1', 2), ('Film2', 2), ('Film3', 2)]
        self.assertEqual(result, expected_result)

    def test_3(self):
        film_keywords = {'drama' : ['Film1'], 'romance': ['Film2'], 'thriller': ['Film3']}
        result = find_films_with_keywords(film_keywords, 1)
        expected_result = [('Film1', 1)]
        self.assertEqual(result, expected_result)

    def test_4(self):
        film_keywords = {}
        result = find_films_with_keywords(film_keywords, 0)
        expected_result = []
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()