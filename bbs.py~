#!/usr/bin/env python3
import random
import primes
import argparse
import re


class BlumBlumShub:

    def __init__(self, bits):
        self.state = 0
        self.n = self.generate_n(bits)
        seed = random.getrandbits(bits)
        self.set_seed(seed)

    @staticmethod
    def get_prime(bits):
        p = 0
        while True:
            p = primes.bigppr(bits)
            if p % 4 == 3:
                break
        return p

    def generate_n(self, bits):
        p = self.get_prime(bits // 2)
        while True:
            q = self.get_prime(bits // 2)
            if p != q:
                return p * q

    def set_seed(self, seed):
        self.state = seed % self.n

    def next(self, bits_num):
        result = 0
        for x in range(bits_num, 0, -1):
            self.state = (self.state**2) % self.n
            result = (result << 1) | (self.state & 1)
        return result


class Tests:

    def __init__(self, bits):
        self.bits = bits

    def mono_bit(self):
        singles = self.bits.count("1")
        length = len(self.bits)
        if (length//2 - length * 0.02) < singles < (length//2 + length * 0.02):
            return True
        return False

    def longrun(self):
        pattern_0 = r'0{26,}'
        pattern_1 = r'1{26,}'
        if re.search(pattern_0, self.bits) is not None:
            return False
        if re.search(pattern_1, self.bits) is not None:
            return False
        return True

    def poker(self):
        result = {}
        for x in range(0, len(self.bits), 4):
            if x + 4 < len(self.bits):
                num = int(self.bits[x:x+4], 2)
                if num not in result:
                    result[num] = 1
                else:
                    result[num] += 1
        return result
        # count = sum(result.values())
        # _sum = sum([x*x for x in result.values()])
        # p = (16/count)*_sum
        # print(p)
        # if 2.16 <= p <= 46.17:
        #    return True
        # return False

    def runs(self):
        result = {
            '0_1': len(re.findall(r'0', self.bits)),
            '0_2': len(re.findall(r'0{2}', self.bits)),
            '0_3': len(re.findall(r'0{3}', self.bits)),
            '0_4': len(re.findall(r'0{4}', self.bits)),
            '0_5': len(re.findall(r'0{5}', self.bits)),
            '0_6+': len(re.findall(r'0{6,}', self.bits)),

            '1_1': len(re.findall(r'1', self.bits)),
            '1_2': len(re.findall(r'1{2}', self.bits)),
            '1_3': len(re.findall(r'1{3}', self.bits)),
            '1_4': len(re.findall(r'1{4}', self.bits)),
            '1_5': len(re.findall(r'1{5}', self.bits)),
            '1_6+': len(re.findall(r'1{6,}', self.bits)),
        }
        return result

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="number of numbers to generate", type=int)
    parser.add_argument("--all-tests", "-a", action='store_true', help="show all tests")
    parser.add_argument("--length", "-l", action='store_true', help="display length bits")
    parser.add_argument("--all-bits", "-b", action='store_true', help="display all bits")
    args = parser.parse_args()

    amount = args.number
    number_bits = 32
    bbs = BlumBlumShub(32)
    sum_ = 0

    for i in range(amount):
        number = bbs.next(number_bits)
        #  print('bin: {:032b}'.format(number) + ' dec: %d' % (int(number)) + ' hex {:0X}'.format(number))
        sum_ += number
        sum_ <<= 32  # sys.getsizeof(number)
    sum_ >>= 32

    if args.all_bits:
        print('All bits:\n{}'.format(bin(sum_)[2:]))

    if args.length:
        print("Total length: {}".format(sum_.bit_length()))

    tests = Tests(bin(sum_))
    if args.all_tests:
        print("Mono bit test: {}".format(str(tests.mono_bit())))
        print("Long run test: {}".format(str(tests.longrun())))
        print("Poker test: {}".format(str(tests.poker())))
        print("Runs test:")
        runs = tests.runs()
        for key in sorted(runs.keys()):
            print("{}: {}".format(key, runs[key]))
