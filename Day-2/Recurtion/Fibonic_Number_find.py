"""Find fibonik Serise using recurtion."""


def fibonic(N):
    if N == 0 or N == 1:
        return N
    return fibonic(N - 1) + fibonic(N - 2)


x = int(input("Enter a number: "))
print(fibonic(x))
