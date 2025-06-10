# Recurtion -> when the function call itself

# Normal function call

# def greet():
#     print("Dinesh")


# greet()

# # Print "Dinesh" 4 times only Using Head Recurtion

# count = 0


# def func():
#     global count
#     if count == 4:
#         return
#     print("Dinesh")
#     count += 1
#     func()


# func()


# Print "Dinesh" 4 times only Using Tail Recurtion

count = 0


def func():
    global count
    if count == 4:
        return
    count += 1
    func()
    print("Dinesh")


func()
