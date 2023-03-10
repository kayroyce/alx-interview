#!/usr/bin/python3
'''Module to validUtf8 '''


def validUTF8(data):
    b = 0
    for i, n in enumerate(data):
        byte = n & 0xFF
        if b:
            if byte >> 6 != 2:
                return False
            b -= 1
            continue
        while (1 << abs(7 - b)) & byte:
            b += 1
        if b == 1 or b > 4:
            return False
        b = max(b - 1, 0)
    return b == 0