import unittest
from MyHashTable import *


class Test(unittest.TestCase):
    def test_insert(self):
        hashtable = MyHashTable(11)
        hashtable.insert(1, 'apple')
        hashtable.insert(2, 'banana')
        hashtable.insert(3, 'mango')
        self.assertEqual(hashtable.hashtable, [[], [[1, 'apple']], [[2, 'banana']], [[3, 'mango']], [], [], [], [], [], [], []])

    def test_get(self):
        hashtable = MyHashTable(11)
        hashtable.insert(1, 'apple')
        hashtable.insert(2, 'banana')
        hashtable.insert(3, 'mango')
        self.assertEqual(hashtable.get(1), (1, 'apple'))
        self.assertEqual(hashtable.get(2), (2, 'banana'))
        self.assertEqual(hashtable.get(3), (3, 'mango'))

    def test_remove(self):
        hashtable = MyHashTable(11)
        hashtable.insert(2, 'banana')
        hashtable.insert(7, 'cherry')
        hashtable.insert(11, 'grape')
        self.assertEqual(hashtable.remove(11), [11, 'grape'])
        self.assertEqual(hashtable.remove(2), [2, 'banana'])

    def test_size(self):
        hashtable = MyHashTable(11)
        hashtable.insert(1, 'apple')
        hashtable.insert(2, 'banana')
        hashtable.insert(3, 'mango')
        hashtable.insert(4, 'watermelon')
        hashtable.insert(5, 'apricot')
        hashtable.insert(6, 'orange')
        self.assertEqual(hashtable.size(), 6)

    def test_load_factor(self):
        hashtable = MyHashTable(11)
        hashtable.insert(3, 'mango')
        hashtable.insert(4, 'watermelon')
        hashtable.insert(5, 'apricot')
        hashtable.insert(6, 'orange')
        self.assertEqual(hashtable.load_factor(), 0.36363636363636365)

    def test_collision(self):
        hashtable = MyHashTable(11)
        # modulus
        hashtable.insert(1, 'apple')
        hashtable.insert(12, 'apple1')
        hashtable.insert(2, 'banana')
        hashtable.insert(13, 'banana1')
        hashtable.insert(3, 'mango')
        hashtable.insert(14, 'mango1')
        self.assertEqual(hashtable.collisions(), 3)

if __name__ == "__main__":
    unittest.main()

    '''
    We want to test:

    creation of Hash Table

    inserting key into hash table and if it matches with something

    deletion/removal of key

    get the current key

    get the size of the hash table

    return load_factor

    find number of collisions

    '''