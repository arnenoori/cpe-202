class Huffman:
    def __init__(self, char, freq):
        self.char = char
        self.code = None
        self.left = None
        self.right = None
        self.freq = freq


# PROJECT 4 & Part of Lab 8 Implementation

# 2.1 Count Occurrences

def cnt_freq(filename):
    try:
        with open(filename, encoding='utf-8-sig') as file:  # built-in Python count
            frequency = [0] * 256
            string = file.read()
            for character in string:
                index = ord(character)  # convert character to unicode code value
                frequency[index] += 1
    except:  # if file doesnt exist
        raise IOError('File doesnt exist')  # raises if file input/output fails
    return frequency


def tree_preorder(node, temp=''):
    if node is None:
        return ''
    if node.left is None and node.right is None:
        return temp + '1' + chr(node.char)
    temp = temp + '0'
    if node.left is not None: # left
        temp = tree_preorder(node.left, temp)
    if node.right is not None: # right
        temp = tree_preorder(node.right, temp)
    return temp


# 2.2 Data Definition for Huffman Tree & 2.3 Build a Huffman Tree

def comes_before(a, b):
    if a.freq == b.freq:
        if a.char < b.char:
            return True
        else:
            return False
    if a.freq < b.freq:
        return True
    else:
        return False


def create_huff_tree(freq_list):
    list = []
    for index in range(0, 256):
        if freq_list[index] != 0:
            new_node = Huffman(index, freq_list[index])
            list.append(new_node)
    if len(list) == 0:
        return None  # return None if does not contain any non-zero counts (i.e. input file was empty)
    while len(list) > 1:
        node1 = findMin(list)
        list.remove(node1)
        node2 = findMin(list)
        list.remove(node2)
        add_freq = node1.freq + node2.freq
        min_char = min(node1.char, node2.char)
        huff_node = Huffman(min_char, add_freq)
        huff_node.left = node1
        huff_node.right = node2
        list.insert(0, huff_node)
    return list[0]


def helper_function(node, str_list, value=""):
    if node.left is None and node.right is None:
        node.code = value
        str_list[node.char] = node.code
    if node.left is not None:
        left = value
        value = value + "0"
        helper_function(node.left, str_list, value)
        value = left
    if node.right is not None:
        temp = value
        value = value + "1"
        helper_function(node.right, str_list, value)
        value = temp


# find min to help create huff tree
def findMin(list):  # find min for binary huffman
    min = list[0]
    for index in range(0, len(list)):
        current = list[index]
        if comes_before(current, min):
            min = current
    return min


# 2.4 Build an Array for the Character Codes

def create_code(root_node):
    if root_node is None:
        return [""] * 256
    else:
        str_list = [""] * 256
        helper_function(root_node, str_list)
        return str_list


# LAB 8 PORTION & 2.5 Huffman Encoding of Project 4

def huffman_encode(in_file, out_file):
    freqlist = cnt_freq(in_file)
    hufftree = create_huff_tree(freqlist)
    codes = create_code(hufftree)
    with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
        string = fin.read()
        if hufftree is None:
            pass
        elif hufftree.left is not None and hufftree.right is not None:
            for character in string:
                converted_code = codes[ord(character)]
                fout.write(converted_code)


def huffman_decode(freqs, encoded_file, decode_file):
    with open(encoded_file) as fin, open(decode_file, 'w') as fout:
        # fin and fout allow to read and write a file
        huff_tree = create_huff_tree(freqs)
        current = huff_tree
        while True:
            string = fin.read(1)
            if not string:
                break
            else:
                if string == '0':
                    current = current.left
                else:
                    current = current.right
                if current.right is None and current.left is None:
                    fout.write(chr(current.char))
                    current = huff_tree
