class Node:
    def __init__(self, char,  freq, left, right):
        self.c = char
        self.f = freq
        self.l = left
        self.r = right
        self.code = None


### HuffmanCode Class ###
class HuffmanCode():
    def __init__(self, text):
        self.__text = text
        self.__node_list = None # a list containing Nodes
        self.__huffman_tree_root = None
        self.__code_list = {}

    def get_char_freq(self):  # return a node_list
        char_freq = {}
        for ch in self.__text:
            if ch in char_freq:
                char_freq[ch] += 1
            else:
                char_freq[ch] = 1
        return char_freq

    def construct_node_list(self, char_freq: dict):
        self.__node_list = [Node(each[0], each[1], None, None) for each in sorted(char_freq.items(), key=lambda item: item[1], reverse=True)]

    def build_tree(self):
        nlist = self.__node_list[:]        # copy the original node list

        # build a huffman tree from a node list
        while len(nlist)>1:
            # construct a tree from 2 last nodes (with minimum frequency)
            sum_node = Node(nlist[-2].c + nlist[-1].c, (nlist[-1].f + nlist[-2].f), nlist[-2], nlist[-1])

            nlist[-2] = sum_node  # replace the item at -2 position with the new tree
            nlist.pop()  # remove the last item

            nlist = sorted(nlist, key=lambda item: item.f, reverse=True) # sort after each time forming a subtree

        self.__huffman_tree_node = nlist[0]  # the root of the huffman tree

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
                if node.c in self.__code_list:
                    self.__code_list[node.c] = code               # Update code list

            if isinstance(node, Node):
                self._assign_code(node.l, code + '0')             # assign code 0 for left children
                self._assign_code(node.r, code + '1')             # assign code 1 for right children

    def encoded_text(self, text):
        en_text = str(''.join([self.__code_list[each] for each in text]))
        return en_text

    def pad_encoded_text(self, en_text):
        padding = 8-(len(en_text) % 8)      # if the length of the encode text is not divisible by 8 then pad with '0'

        for i in range(padding):
            en_text += '0'

        pad_info = '0:08b'.format(padding)  # turn the len of the added chars to binary code (8 bit)
        return pad_info + en_text           # return 8 bits of padding + encoded text

    def byte_array(self, pad_encoded_text):
        n = len(pad_encoded_text)
        if n % 8 != 0:
            print('Encoded text length not allowed')

        byte_array = bytearray()
        for i in range(0, n, 8):    # from 0 to n, iterate by 8 items
            byte = pad_encoded_text[i:i+8]
            byte_array.append(int(byte, 2))                # change a byte of base 2 into integer

        return byte_array

############## END of HUFFMAN CLASS ###############
