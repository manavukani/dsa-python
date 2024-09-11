input = 5

# for i in range(input):
#     for j in range(input):
#         print('*', end=' ')
#     print()



# for i in range(input):
#     for j in range(i+1):
#         print('*', end=' ')
#     print()


# for i in range(1, input+1):
#     for j in range(i):
#         print(j+1, end=' ')
#     print()



# for i in range(1, input+1):
#     for j in range(i):
#         print(i, end=' ')
#     print()


# for i in range(input):
#     for j in range(input, i, -1):
#         print('*', end=' ')
#     print()


# for i in range(input):
#     for j in range(input, i, -1):
#         print(input-j+1, end=' ')
#     print()


for i in range(input):
    for j in range(input - i - 1):
        print(" ", end=' ')
    for j in range(2*i+1):
        print("*", end=' ')
    print()

