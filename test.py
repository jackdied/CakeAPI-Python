import unittest
import urllib

from cakeapi import php_encode

class TestAPI(unittest.TestCase):
    def test_php_encode(self):
        params = {'0' : {'foo':7}, '1' : {'bar':3, 'baz':5}}
        want = 'record[0][foo]=7&record[1][bar]=3&record[1][baz]=5'
        self.assertEqual(want, urllib.unquote(php_encode({'record' : params})))
        # the hash order of the following happens to match the sort order
        params = {'allo' : 7, 'world' : '!'}
        self.assertEqual(urllib.urlencode(params), php_encode(params))
