# Recurtion using Parameters with head and Tail recurtion

# print 1 to N number using parameter Recurtion with Head recurtion


def func(i, N):
    if i == N:
        return
    print(i)
    func(i + 1, N)


func(1, 5)

# print 1 to N number using parameter Recurtion with Tail recurtion also called BackTracking


def func(i, N):
    if i == N:
        return
    func(i + 1, N)
    print(i)


func(1, 5)

# print 1 to N number using parameter Recurtion with Tail recurtion.


def func(i, N):
    if i == N:
        return
    func(i - 1, N)
    print(i)


func(4, 0)
