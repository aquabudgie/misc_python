def reverse_Bits(n):
    result = 0
    while n > 0:
        # result = result << 1, returns result with bits shifted to the left by 1 place, new bits on the right hand side are zeros
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

if __name__ == "__main__":
    print(reverse_Bits(3))