## Using left Shift

n = 13
i = 2

if n & (1 << i) != 0:
    print("true")
else:
    print("False")


## Using Right Shift
n = 13
i = 2

if ((n >> i) & 1) == 1:
    print("true")
else:
    print("False")
