# customer pays 5, 10, 20
# return True if we can provide change, False otherwise

def lemonade_change(bills):
    # no need to keep track of 20s -- not used in change 
    five, ten = 0, 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five >= 1:
                five -= 1
                ten += 1
            else:
                return False
        elif bill == 20:
            if five >= 1 and ten >= 1:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True

# test
bills = [5, 5, 5, 10, 20]
print(lemonade_change(bills))  # True
bills = [5, 5, 10]
print(lemonade_change(bills))  # True
bills = [10, 10]
print(lemonade_change(bills))  # False