# method -> 1

start = 3
goal = 4
count = 0
new = start ^ goal
for i in range(0, 32):
    if new & (1 << i) != 0:
        count += 1
print(count)

# method -> 2

start = 3
goal = 4
count = 0
new = start ^ goal
while new > 0:
    if new % 2 == 1:
        count += 1
    new = new // 2
print(count)
