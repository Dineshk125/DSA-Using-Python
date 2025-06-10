"""
Print Sum of i To N Using Parameters Recurtion.
Input: 5 -> 1+2+3+4+5
ouput: 15

"""


def func(sum, i, N):
    if i > N:
        print(sum)
        return
    func(sum + i, i + 1, N)


func(0, 1, 5)

"""
Print Sum of N Numbers Using functional Recurtion.
Input: 5 -> 5+4+3+2+1
ouput: 15

"""


def func(N):
    if N == 1:
        return 1
    return N + func(N - 1)


x = func(10)
print(x)


"""
Print Multiple of N Numbers Using functional Recurtion.
Input: 5 -> 5*4*3*2*1
ouput: 15

"""


def func(N):
    if N == 1:
        return 1
    return N * func(N - 1)


x = func(3)
print(x)
