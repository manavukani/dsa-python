input = 1241

revNum = 0
test = input # to compare at the end

while input > 0:
    revNum = input % 10 + 10*revNum
    input = input//10

if revNum == test:
    print('Palindrome')
else:
    print('Not Palindrome')
