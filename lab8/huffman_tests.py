import unittest
import filecmp  # allows us to bring in files
from huffman import *


class TestList(unittest.TestCase):
    # LAB 8 Test
    def test_create_code(self):
        freqlist = cnt_freq("lab.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('A')], '00')
        self.assertEqual(codes[ord('B')], '01')
        self.assertEqual(codes[ord('C')], '10')
        self.assertEqual(codes[ord('D')], '11')

    # 2.1 test case
    def test_cnt_freq(self):
        freqlist = cnt_freq("countoccurrences.txt")
        hufflist = [0] * 256
        hufflist[97:104] = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], hufflist[97:104])

    # One unique char edge case
    def test_cnt_freq1(self):
        freqlist = cnt_freq("samechar.txt")
        hufflist = [0] * 256
        hufflist[91:100] = [0, 0, 0, 0, 0, 0, 5, 0, 0]
        self.assertListEqual(freqlist[92:100], hufflist[92:100])

    def test_create_huff_tree1(self):
        freqlist = cnt_freq("samechar.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 5)
        self.assertEqual(hufftree.char, 97)

    def test_create_code1(self):
        freqlist = cnt_freq("samechar.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '')

    # Empty file edgecase
    def test_empty_file(self):
        freq_list = cnt_freq('empty.txt')
        expected_freq_list = [0] * 256
        self.assertEqual(freq_list, expected_freq_list)
        huffman_tree = create_huff_tree(freq_list)
        expected_huffman_tree = None
        self.assertEqual(huffman_tree, expected_huffman_tree)
        codes = create_code(huffman_tree)
        expected_codes = [''] * 256
        self.assertEqual(codes, expected_codes)
        tree_preorder1 = tree_preorder(huffman_tree)
        expected_tree_preorder = ''
        self.assertEqual(tree_preorder1, expected_tree_preorder)

    # 2.5 Huffman Coding Test
    def test_create_huff_tree2(self):
        freqlist = cnt_freq("createheader.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 9)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left # bs
        self.assertEqual(left.freq, 4)
        self.assertEqual(left.char, 98)
        right = hufftree.right # a & c
        self.assertEqual(right.freq, 5)
        self.assertEqual(right.char, 97)

   # Test File Encoded
    def test_encodefile(self):
        huffman_encode("encodetest.txt", "output.txt")
        self.assertTrue(filecmp.cmp("output.txt", "encodedsolution.txt"))

    # Test File Decoded
    def test_decodefile(self):
        freqlist = cnt_freq("lab.txt")
        huffman_decode(freqlist, "output1.txt", "decodefile.txt")
        self.assertTrue(filecmp.cmp("decodefile.txt", "lab.txt"))

if __name__ == '__main__':
    unittest.main()
