def check_armstrong(n):
    num = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit**len(str(num))
        n //= 10

    return num == sum

def main():
    number = 153
    if check_armstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")

if __name__ == "__main__":
    main()