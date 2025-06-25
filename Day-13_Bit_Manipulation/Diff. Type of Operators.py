"""
AND Operator -> all True - true
                once False - False

OR(||) Operator

XOR(^) Operator -> 1. Number of 1's are Odd - 1
                2. Number of 1's are even - 0

Not(~) Operator ->  True - False( 1 - 0 )
                 False - True( 0 - 1 )

                 x = ~(13)
                 1. flip
                 2.check -ive and +ive

                if -ive Find 2's compliment
                if +ive  Stop


Shift Operator -> Two type -> 1. Right Shift( >> ) -> ex. 13>>1 = 6 - .......1101>>1 -> .....0110, formula - x>>k ->x/2**k
                              2. Left Shift( << ) -> ex. 13<<1 - 000.......01101 << 1 - 00......01101


"""

## OR Operator

print("OR Operator")
for i in range(0, 3):
    for j in range(0, 3):
        print(i | j, end=" ")
    print()

## AND Operator

print("AND Operator")
for i in range(0, 3):
    for j in range(0, 3):
        print(i & j, end=" ")
    print()


## XOR Operator

print("XOR Operator")
for i in range(0, 3):
    for j in range(0, 3):
        print(i ^ j, end=" ")
    print()


## NOT Operator

print("NOT Operator")
for i in range(0, 3):
    print(~(i))


"""5. Shift operator ---> << or >>"""
# left shift
print("Left Shift")
print(1 << 2)

# right shift

print("Right Shift")
print(1 >> 1)
