import os
from select import select

from setuptools.command.test import test


class Node:
    def __init__(self, char,  freq, left, right):
        self.c = char
        self.f = freq
        self.l = left
        self.r = right
        self.code = None

### HuffmanCode Class ###
class HuffmanCode():
    def __init__(self, path):
        self.__path = path
        self.__text = ''
        self.__node_list = None  # a list containing Nodes
        self.__huffman_tree_root = None
        self.__code_list = {}
        self.__encoded_text = ''

    def get_text_length(self):
        return len(self.__text)

    def get_text_bit_legth(self):
        return len(self.__text) * 8

    def get_encoded_text_bit_length(self):
        return len(self.__encoded_text)

    def get_bit_from_code(self):
        bit = 0
        for i in self.__code_list.items():
            bit += len(i[1])
            print(bit)
        return bit

    def get_char_freq(self):  # return a node_list
        char_freq = {}
        for ch in self.__text:
            if ch in char_freq:
                char_freq[ch] += 1
            else:
                char_freq[ch] = 1
        self.__node_list = [Node(each[0], each[1], None, None) for each in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)]
        return char_freq


    def get_node_list(self):
        return self.__node_list

    def build_tree(self):
        nlist = self.__node_list[:]        # copy the original node list

        # build a huffman tree from a node list
        while len(nlist)>1:
            # construct a tree from 2 last nodes (with minimum frequency)
            sum_node = Node(nlist[-2].c + nlist[-1].c, (nlist[-1].f + nlist[-2].f), nlist[-2], nlist[-1])

            nlist[-2] = sum_node  # replace the item at -2 position with the new tree
            nlist.pop()  # remove the last item

            nlist = sorted(nlist, key=lambda item: item.f, reverse=True)  # sort after each time forming a subtree

        self.__huffman_tree_root = nlist[0]  # the root of the huffman tree

    def printTree(self):
            if self.__huffman_tree_root != None:
                self._printTree(self.__huffman_tree_root, 0)

    def _printTree(self, node, num_indents):
        if node != None:
            self._printTree(node.r, num_indents + 1)
            output = ""

            for i in range(num_indents):
                output += "\t"

            output += str('{}, {}, {}'.format(node.f, '" "' if node.c == ' ' else node.c, node.code))
            print(output)
            self._printTree(node.l, num_indents + 1)

    def assign_code(self):
        if self.__huffman_tree_root != None:
            self._assign_code(self.__huffman_tree_root, '')

    def _assign_code(self, node, code):
            if node is not None:
                node.code = code                                  # add new attribute 'code' to each node
            if isinstance(node, Node):
                self._assign_code(node.l, code + '0')             # assign code 0 for left children
                self._assign_code(node.r, code + '1')             # assign code 1 for right children

    def update_code_list(self):
        for each in self.__node_list:
            self.__code_list[each.c] = each.code

    def get_code_list(self):
        return self.__code_list

    def encoded_text(self):
        encoded_text = ''
        for t in self.__text:
            encoded_text += self.__code_list[t]

        self.__encoded_text = encoded_text


    def get_encoded_text(self):
        return self.__encoded_text

    def pad_encoded_text(self):
        padding = 8-(len(self.__encoded_text) % 8)        # if the length of the encode text is not divisible by 8 then pad with '0'
        en_text = self.__encoded_text
        for i in range(padding):
            en_text += '0'

        pad_info = '{0:08b}'.format(padding)  # turn the len of the added chars to binary code (8 bit)
        return pad_info + en_text             # return 8 bits of padding + encoded text

    def byte_array(self, pad_encoded_text):
        n = len(pad_encoded_text)
        if n % 8 != 0:
            print('Encoded text length not allowed')
        byte_array = bytearray()
        for i in range(0, n, 8):                           # from 0 to n, iterate by 8 items
            byte = pad_encoded_text[i:i+8]                 # 1 byte = 8 bits
            byte_array.append(int(byte, 2))                # change a byte of base 2 into integer
        return byte_array                                  # return a byte array

    # Prerequisite function to run to update all attributes
    def compress_file(self):
        file_name, file_extension = os.path.splitext(self.__path)    # os.path.splitext splits a path into 2 part:
                                                                     # e.g: 'C:/programs/text.txt' => 'C:/programs/text' & '.txt'
        compressed_file = file_name + '.bin'

        with open(self.__path, 'r+') as input_file, open(compressed_file, 'wb') as output_file:
            self.__text = input_file.read().rstrip()     # Read the text file to a string and
                                                         # remove all space on the right

            self.get_char_freq()                   # get a dictionary for char frequency
            self.build_tree()                      # build a huffman tree from self.node_list

            self.assign_code()                     # assign binary code for each character in tree
            self.update_code_list()                # update self.code_list

            self.encoded_text()                    # construct encoded text comprises 0 and 1

            pad_en_text = self.pad_encoded_text()  # pad encoded text if necessary

            byte_array = self.byte_array(pad_en_text)           # turn (padded) encoded text into a byte array
                                                                # remember 1 byte = 8 bits
            output_file.write(bytes(byte_array))                # write bytes format of the byte array to output file

            print('Compressed')
        return compressed_file

############## END of HUFFMAN CLASS ###############
if __name__ == '__main__':
    hf = HuffmanCode(str(input('Enter file path: ')))


    compressed_path = hf.compress_file()
    print('Get compressed file here: ' + compressed_path)
    print('Orginal text length: ' , hf.get_text_length())
    print('Original bit length: ' , hf.get_text_bit_legth())
    print('Encoded bit len: ', hf.get_encoded_text_bit_length())