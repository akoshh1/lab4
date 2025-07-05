import math
import heapq

def entropy(p):
    return round(-sum(pi * math.log2(pi) for pi in p if pi > 0), 3)
def message_info(n, m):
    return round(n * math.log2(m), 3)
def shannon_avg(p):
    return round(sum(p[i] * math.ceil(-math.log2(p[i])) for i in range(len(p))), 3)
def redundancy(H, Hmax):
    return round(Hmax - H, 3)
def info_uniform(N):
    return round(math.log2(N), 3)
def uniform_entropy(n):
    return round(math.log2(n), 3)
def reliable_info(n, p):
    if p in (0, 1):
        return 0
    H = -p * math.log2(p) - (1 - p) * math.log2(1 - p)
    return round(n * (1 - H), 3)
def entropy_change():
    return round(entropy([0.5, 0.5]), 3), round(entropy([0.9, 0.1]), 3)
def message_bits(n, per):
    return round(n * per, 3)
def binary_info(p):
    return round(-p * math.log2(p) - (1 - p) * math.log2(1 - p), 3)
def num_messages(n, b):
    return 2 ** (b * n)
def avg_log(p):
    return round(sum(-pi * math.log2(pi) for pi in p), 3)
def doubling(info, l1, l2):
    return round(info * l2, 3)

# Хаффман-код
class Node:
    def __init__(self, s, p):
        (self.s, self.p, self.l, self.r) = s, p, None, None
    def __lt__(a, b):
        return a.p < b.p
def huffman(p_dict):
    heap = [Node(s, p) for s, p in p_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        parent = Node(None, a.p + b.p); parent.l, parent.r = a, b
        heapq.heappush(heap, parent)
    codes = {}
    def build(node, code=""):
        if node.s: codes[node.s] = code
        else: build(node.l, code + "0"); build(node.r, code + "1")
    build(heap[0])
    avg_len = round(sum(p_dict[s] * len(codes[s]) for s in p_dict), 3)
    return avg_len

print("Задача 1:", entropy([0.1, 0.2, 0.3, 0.4]))
print("Задача 2:", message_info(10, 8))
print("Задача 3:", shannon_avg([0.5, 0.3, 0.2]))
print("Задача 4:", redundancy(1.8, 2))
print("Задача 5:", huffman({'0': 0.9, '1': 0.1}))
print("Задача 6:", info_uniform(16))
print("Задача 7:", uniform_entropy(5))
print("Задача 8:", reliable_info(8, 0.1))
print("Задача 9:", huffman({'A': 0.4, 'B': 0.3, 'C': 0.2, 'D': 0.1}))
before, after = entropy_change()
print("Задача 10:", "До =", before, "После =", after)
print("Задача 11:", message_bits(100, 2.5))
print("Задача 12:", binary_info(0.75))
print("Задача 13:", entropy([1.0]))
print("Задача 14:", huffman({'A': 0.5, 'B': 0.3, 'C': 0.2}))
print("Задача 15:", round(1 - binary_info(0.1), 3))
print("Задача 16:", entropy([0.5, 0.5]), "(равновер.) vs", entropy([0.9, 0.1]), "(неравновер.)")
print("Задача 17:", num_messages(5, 4))
print("Задача 18:", avg_log([0.5, 0.3, 0.2]))
print("Задача 19:", doubling(2.5, 10, 20))
print("Задача 20:", entropy([0.5, 0.3, 0.2]))
