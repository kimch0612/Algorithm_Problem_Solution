l1 = input()
l2 = input()
l3 = input()
l4 = input()
l5 = input()
l6 = input()
l7 = input()
l8 = input()
l9 = input()

max = 0
max_location = ""

for _ in range(0, 9):
    if int(l1.split(" ")[_]) > int(max):
        max = l1.split(" ")[_]
        max_location = "1 " + str(_ + 1)
for _ in range(0, 9):
    if int(l2.split(" ")[_]) > int(max):
        max = l2.split(" ")[_]
        max_location = "2 " + str(_ + 1)
for _ in range(0, 9):
    if int(l3.split(" ")[_]) > int(max):
        max = l3.split(" ")[_]
        max_location = "3 " + str(_ + 1)
for _ in range(0, 9):
    if int(l4.split(" ")[_]) > int(max):
        max = l4.split(" ")[_]
        max_location = "4 " + str(_ + 1)
for _ in range(0, 9):
    if int(l5.split(" ")[_]) > int(max):
        max = l5.split(" ")[_]
        max_location = "5 " + str(_ + 1)
for _ in range(0, 9):
    if int(l6.split(" ")[_]) > int(max):
        max = l6.split(" ")[_]
        max_location = "6 " + str(_ + 1)
for _ in range(0, 9):
    if int(l7.split(" ")[_]) > int(max):
        max = l7.split(" ")[_]
        max_location = "7 " + str(_ + 1)
for _ in range(0, 9):
    if int(l8.split(" ")[_]) > int(max):
        max = l8.split(" ")[_]
        max_location = "8 " + str(_ + 1)
for _ in range(0, 9):
    if int(l9.split(" ")[_]) > int(max):
        max = l9.split(" ")[_]
        max_location = "9 " + str(_ + 1)

print(max)
print(max_location)