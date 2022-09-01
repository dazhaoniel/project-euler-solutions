# Digit factorials
# https://projecteuler.net/problem=34
# 9!7 = 2540160 which is the upper limit
import math

def digit_factorials():
    s = 0
    for i in range(3, 2540160):
        t = [math.factorial(int(char)) for char in str(i)]
        if (sum(t) == i): s += i

    return s


if __name__ == '__main__':
    print(digit_factorials())

