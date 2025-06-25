## Binary to Decimal, T.C. and S.C. -> O(logN)


def binaryToDecimal(x: int):
    result = " "
    while x > 0:
        if x % 2 == 1:
            result += "1"
        else:
            result += "0"

        x = x // 2

    result = result[::-1]
    return result


print(binaryToDecimal(9))


# Decimal to Binary


def binary2decimal(binary):
    index = len(binary) - 1
    decimal = 0
    power = 0
    while index >= 0:
        d = int(binary[index]) * (2**power)
        decimal += d
        index -= 1
        power += 1
    return decimal


print(binary2decimal("1011"))
