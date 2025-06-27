def genParen(index, total):
    global result
    global brackets
    global n
    if index >= len(brackets):
        if total == 0:
            result.append("".join(brackets))
        return
    if total > len(brackets) // 2:
        return
    elif total < 0:
        return

    brackets[index] = "("
    summ = total + 1
    genParen(index + 1, summ)
    brackets[index] = ")"
    summ = total - 1
    genParen(index + 1, summ)
    return result


n = 3
brackets = [""] * (n * 2)
result = []
print(genParen(index=0, total=0))
# genParen(index=0, total=0)
# print(result)
