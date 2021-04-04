

import unittest

import tohil

from tohil import tclobj

class TestTD(unittest.TestCase):
    def test_td1(self):
        """tohil.tclobj td_get """
        x = tohil.eval("list a 1 b 2 c 3", to=tohil.tclobj)
        self.assertEqual(x.td_get('a'), '1')
        self.assertEqual(x.td_get('a',to=int), 1)
        with self.assertRaises(KeyError):
            x.td_get('z')
        self.assertEqual(x.td_get('z', default='bar'), 'bar')
        self.assertEqual(x.td_get('z', default='bar', to=list), ['bar'])
        with self.assertRaises(RuntimeError):
            x.td_get('z',default='bar',to=int)
        self.assertEqual(x.td_get('z', default='1', to=int), 1)

    def test_td2(self):
        """tohil.tclobj td_remove """
        x = tohil.eval("list a 1 b 2 c 3", to=tohil.tclobj)
        self.assertEqual(x.td_get('b'), '2')
        self.assertEqual(x.td_get('b', to=int), 2)
        x.td_remove('c')
        self.assertEqual(repr(x), "<tohil.tclobj: 'a 1 b 2'>")

    def test_td3(self):
        """tohil.tclobj td_set """
        x = tohil.tclobj()
        x.td_set('foo','bar')
        x.td_set('hey','you')
        self.assertEqual(x.td_get('foo'), 'bar')
        self.assertEqual(repr(x), "<tohil.tclobj: 'foo bar hey you'>")
        x.td_remove('foo')
        self.assertEqual(repr(x), "<tohil.tclobj: 'hey you'>")

    def test_td4(self):
        """tohil.tclobj td_set, get and remove """
        x = tclobj()
        x.td_set('foo',5)
        x.td_set('foo',5)
        self.assertEqual(x.td_get('foo'), '5')
        self.assertEqual(x.td_get('foo', to=int), 5)
        self.assertEqual(repr(x), "<tohil.tclobj: 'foo 5'>")
        x.td_remove('foo')
        self.assertEqual(repr(x), "<tohil.tclobj: ''>")

    def test_td4(self):
        """tohil.tclobj list remove """
        x = tclobj()
        x.td_set('a',1)
        x.td_set('b',2)
        x.td_set('c',3)
        x.td_remove('a')
        x.td_remove(['c'])
        x.td_remove(['c'])
        self.assertEqual(repr(x), "<tohil.tclobj: 'b 2'>")

    def test_td5(self):
        """tohil.tclobj td_set with list of keys"""
        x = tclobj()
        x.td_set(['a','b','c','d'],'bar')
        self.assertEqual(repr(x), "<tohil.tclobj: 'a {b {c {d bar}}}'>")

    def test_td6(self):
        """tohil.tclobj td_get with list of keys"""
        x = tclobj()
        x.td_set(['a','b','c','d'],'foo')
        x.td_set('b','bar')
        self.assertEqual(x.td_get(['a','b','c','d']), "foo")

    def test_td7(self):
        """tohil.tclobj td_exists"""
        x = tclobj()
        x.td_set(['a','b','c'],'foo')
        x.td_set('b','bar')
        self.assertEqual(x.td_get(['a','b','c']), "foo")
        self.assertEqual(x.td_exists(['a','b','c']), True)
        self.assertEqual(x.td_exists(['a','d','d']), False)
        x.set("monkey")
        with self.assertRaises(TypeError):
            x.td_exists(['a','b','c'])

    def test_td8(self):
        """tohil.tclobj td_get of nested dictionaries"""
        t = tclobj()
        t.td_set(['a','b','c','d'],1)
        t.td_set('b','bar')
        self.assertEqual(t.td_get(['a','b','c','d']), '1')
        self.assertEqual(t.td_get(['a','b']), 'c {d 1}')
        x = t.td_get(['a','b'], to=tohil.tclobj)
        with self.assertRaises(KeyError):
            x.td_get('d')
        self.assertEqual(x.td_get(['c','d']), '1')
        self.assertEqual(x.td_exists(['c','d']), True)

if __name__ == "__main__":
    unittest.main()