# #1
# class MooreMachineEqualLastTwo:
#     def __init__(self):
#         self.prev = None
#         self.curr = None
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             self.prev, self.curr = self.curr, bit
#             if self.prev is None:
#                 self.output.append('-')
#             else:
#                 self.output.append(int(self.prev == self.curr))
#         return self.output

# #2
# class MooreMachineCompression:
#     def __init__(self):
#         self.last = None
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             if bit != self.last:
#                 self.output.append(bit)
#             self.last = bit
#         return self.output

#3
# class MooreMachineDetect101:
#     def __init__(self):
#         self.state = 0
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             if self.state == 0:
#                 self.state = 1 if bit == 1 else 0
#             elif self.state == 1:
#                 self.state = 2 if bit == 0 else 1
#             elif self.state == 2:
#                 self.state = 3 if bit == 1 else 0
#             elif self.state == 3:
#                 self.state = 1 if bit == 1 else 0
#
#             self.output.append(1 if self.state == 3 else 0)
#         return self.output

#4
# class MooreMachineOnesDiv3:
#     def __init__(self):
#         self.count = 0
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             if bit == 1:
#                 self.count += 1
#             self.output.append(1 if self.count % 3 == 0 else 0)
#         return self.output

# #5
# class MooreMachineAlternatingBits:
#     def __init__(self):
#         self.last = None
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             if self.last is None:
#                 self.output.append(1)
#             else:
#                 self.output.append(1 if bit != self.last else 0)
#             self.last = bit
#         return self.output

# #6
# class MooreMachineLastTwoAB:
#     def __init__(self):
#         self.prev = None
#         self.output = []
#
#     def process(self, sequence):
#         for ch in sequence:
#             if self.prev is None:
#                 self.output.append(0)
#             else:
#                 self.output.append(1 if self.prev == 'a' and ch == 'b' else 0)
#             self.prev = ch
#         return self.output

# #7
# class MooreMachineEvenSumLastThree:
#     def __init__(self):
#         self.window = []
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             self.window.append(bit)
#             if len(self.window) > 3:
#                 self.window.pop(0)
#             s = sum(self.window)
#             self.output.append(1 if s % 2 == 0 else 0)
#         return self.output

# #8
# class MooreMachineCurrentEqualsPrevious:
#     def __init__(self):
#         self.prev = None
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             if self.prev is None:
#                 self.output.append('-')
#             else:
#                 self.output.append(1 if bit == self.prev else 0)
#             self.prev = bit
#         return self.output

# #9
# class MooreMachineParity:
#     def __init__(self):
#         self.parity = 0
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             self.parity ^= bit
#             self.output.append(self.parity)
#         return self.output

# #10
# class MooreMachineDetect1101:
#     def __init__(self):
#         self.state = 0
#         self.output = []
#
#     def process(self, sequence):
#         for bit in sequence:
#             if self.state == 0:
#                 self.state = 1 if bit == 1 else 0
#             elif self.state == 1:
#                 self.state = 2 if bit == 1 else 0
#             elif self.state == 2:
#                 self.state = 3 if bit == 0 else 2
#             elif self.state == 3:
#                 self.state = 1 if bit == 1 else 0
#
#             self.output.append(1 if self.state == 0 and bit == 1 else 0)
#         return self.output

