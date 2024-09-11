input = 1258

revNum = 0

while input > 0:
    revNum = input % 10+revNum*10
    input = input//10
    
print(revNum)