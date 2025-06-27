## First Start Converting with - 0


class Solution:
    def BinaryString(self, index, flag, number, result):
        if index >= len(number):
            result.append("".join(number))
            return
        number[index] = "0"
        self.BinaryString(index + 1, True, number, result)
        if flag == True:
            number[index] = "1"
            self.BinaryString(index + 1, False, number, result)
            number[index] = "0"

    def generateBinaryString(self, n):
        number = ["0"] * n
        result = []
        self.BinaryString(0, True, number, result)
        return result


s1 = Solution()

print(s1.generateBinaryString(3))

## First Start Converting with - 1


class Solution:
    def BinaryString(self, index, flag, number, result):
        if index >= len(number):
            result.append("".join(number))
            return
        number[index] = "1"
        self.BinaryString(index + 1, True, number, result)
        if flag == True:
            number[index] = "0"
            self.BinaryString(index + 1, False, number, result)
            number[index] = "1"

    def generateBinaryString(self, n):
        number = ["0"] * n
        result = []
        self.BinaryString(0, True, number, result)
        return result


s1 = Solution()

print(s1.generateBinaryString(3))
