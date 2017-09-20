numbersTaken=[7,9,12,18,21]
print("here are the numbers that are still availabe")

for n in range(1,30):
    if n in numbersTaken:
        continue #.. flow of control goes back to loop when if condition is met
    print (n)
