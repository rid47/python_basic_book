# a = [100, 50, 60, 2, 35]

# for i in range(len(a)):
#     swap = False
#     for j in range(0, len(a)-i-1):
#         if a[j] > a[j+1]:
#             container = a[j+1]
#             a[j+1] = a[j]
#             a[j] = container
#             swap = True
#     if not swap:
#         break

# print(a)

a = [100, 50, 60, 2, 35]
print(len(a))

while True:
    swap = False
    for j in range(0, len(a)-1):
        print(j)
        if a[j] > a[j+1]:
            container = a[j+1]
            a[j+1] = a[j]
            a[j] = container
            swap = True
    if not swap:
        break

print(a)

