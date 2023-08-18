import numpy as np
import os
from PIL import Image
from heapq import heappush, heappop, heapify
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanEncoder:
    def __init__(self, text):
        self.text = text
        self.frequencies = self.get_frequencies()
        self.huffman_tree = self.build_huffman_tree()
        self.huffman_table = self.build_huffman_table()

    def simp(self, text):
        temp = [byte for byte in text]
        temp.sort(reverse = True)
        return bytes(temp)

    def get_frequencies(self):
        frequencies = defaultdict(int)
        for char in self.simp(self.text):
            frequencies[char] += 1
        return frequencies

    def build_huffman_tree(self):
        heap = []
        for char, freq in self.frequencies.items():
            node = Node(char, freq)
            heap.append(node)
        heapify(heap)

        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            merged = Node(None, lo.freq + hi.freq)
            merged.left = lo
            merged.right = hi
            heappush(heap, merged)
        return heap[0]

    def build_huffman_table(self):
        huffman_table = {}
        self.traverse(self.huffman_tree, "", huffman_table)
        return huffman_table

    def traverse(self, node, code, huffman_table):
        if node.char is not None:
            huffman_table[node.char] = code
            return
        self.traverse(node.left, code + "0", huffman_table)
        self.traverse(node.right, code + "1", huffman_table)

    def encode_text(self):
        encoded_text = ""
        for char in self.text:
            encoded_text += self.huffman_table[char]
        return encoded_text
    
    def decode_text(self, encoded_text):
        decoded_text = []
        node = self.huffman_tree
        for bit in encoded_text:
            if bit == "0":
                node = node.left
            else:
                node = node.right
            if node.char is not None:
                decoded_text.append(node.char)
                node = self.huffman_tree
        return bytes(decoded_text)


# Get image value -> (three dimensional array)
image = Image.open('secret/packed.png')
image_array = np.array(image)

ordo = len(image_array[0])
elementsLen = len(image_array)*ordo*3

# Brute Force to guess the number of files
for i in range(1, 6):
    for j in range(i):
        file = ""
        freq = []
        idx = 0
        # Get Bytes for each file
        while(idx*i+j < elementsLen):
            # Get The Number of freq (0-255)
            if(idx < 512 and idx % 2 == 0):
                freq.append(image_array[(idx*i+j)//(3*ordo)][(idx*i+j)%(3*ordo)//3][(idx*i+j)%3] << 8)
            elif(idx < 512):
                freq[-1] += image_array[(idx*i+j)//(3*ordo)][(idx*i+j)%(3*ordo)//3][(idx*i+j)%3]
            else:
                file += str(bin(image_array[(idx*i+j)//(3*ordo)][(idx*i+j)%(3*ordo)//3][(idx*i+j)%3]))[2:].zfill(8)
            idx += 1
        
        # Create a byte containing each data from the freq array
        temp = bytes([byte for byte in range(len(freq)) for _ in range(freq[byte])])

        # Huffman Decode
        encoder = HuffmanEncoder(temp)
        decoded = encoder.decode_text(file)
        directory = "answer"
        os.makedirs(directory, exist_ok=True)
        if(b"PDF" in decoded):
            open(directory+f"/{j}.pdf", "wb").write(decoded)