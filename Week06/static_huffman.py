class Node:
    def __init__(self, char,  freq, left, right):
        self.c = char
        self.f = freq
        self.l = left
        self.r = right

# Function to get a list containing
# all node with characters and frequency
def get_freq(s: str):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return [Node(each[0], each[1], None, None) for each in sorted(freq.items(), key=lambda item: item[1], reverse=True)]

# Function to build a huffman tree
# Return the root node
def build_tree(node_list_org: list):
    # copy the original node list
    nlist = node_list_org[:]

    # build a huffman tree from a node list
    while len(nlist ) > 1:
        # construct a tree from 2 last nodes (with minimum frequency)
        sum_node = Node(None, (nlist[-1].f + nlist[-2].f), nlist[-2], nlist[-1])

        nlist[-2] = sum_node  # replace the item at -2 position with the new tree
        nlist.pop()  # remove the last item

        # sort after each time forming a subtree
        nlist = sorted(nlist, key=lambda item: item.f, reverse=True)
    return nlist[0]  # the root of the huffman tree

def printTree(root):
        if root != None:
            _printTree(root, 0)

def _printTree(node, num_indents):
        if node != None:
            _printTree(node.r, num_indents + 1)
            output = ""
            for i in range(num_indents):
                output += "\t"
            output += str('{}, {}, {}'.format(node.f, '" "' if node.c == ' ' else node.c , node.code))
            print(output)
            _printTree(node.l, num_indents + 1)

def assign_code(node, code):
    if node is not None:
        node.code = code  # add new attribute 'code' to each node with character
    if isinstance(node, Node):
        assign_code(node.l, code + '0')  # assign code 0 for left children
        assign_code(node.r, code + '1')  # assign code 1 for right children

def huffman_encoding():
    a = get_freq(str(input('Input a string: ')))

    b = build_tree(a)  # build a huffman tree

    assign_code(b, '')  # assigning code 1 or 0 to each node with character

    printTree(b)  # print the tree

    # sort the list again (based on the length of the code)
    # some characters with the same frequency but different code length
    a = sorted(a, key=lambda node: len(node.code))

    print('{:^10} | {:^10} | {:^10}'.format('char', 'freq', 'code'))
    for i in a:
        print('{:^10} | {:^10} |  {:10}'.format('" "' if i.c == ' ' else i.c, i.f, i.code))

huffman_encoding()
