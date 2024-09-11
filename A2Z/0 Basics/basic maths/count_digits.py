import math

input = 1532

cnt = 0
while (input > 0):
    cnt +=1
    input = input // 10
    
print("Normal ", cnt)


def optimal_count_digits(input):
    return int(math.log10(input) + 1)

print("Optimal ", optimal_count_digits(1532))