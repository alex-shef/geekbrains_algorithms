"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

import heapq
from collections import Counter


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf:
    def __init__(self, ch):
        self.ch = ch

    def walk(self, code, acc):
        code[self.ch] = acc or "0"


def huffman_code(string):
    h = []
    for ch, freq in Counter(string).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(code, encoded):
    result = ""
    new_code = {key: value for value, key in code.items()}
    while encoded:
        for ch in new_code:
            if encoded.startswith(ch):
                result += new_code[ch]
                encoded = encoded[len(ch):]
    return print(result)


if __name__ == '__main__':
    string = input("Input the string for encoding: ")
    code = huffman_code(string)
    encoded = "".join(code[ch] for ch in string)
    print("Keys =", len(code), "Encoded string length =", len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)
    huffman_decode(code, encoded)
