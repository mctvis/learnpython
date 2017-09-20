#set is Collection of items but cant any duplicates like a list can
groceries={'cereal', 'milk','starcrunch','beer','ducttape','lotion','beer'} #notice the use of curly braces is sets
print(groceries) #notice beer gets printed only once and also notice curly brackets are also printed

if 'milk' in groceries:
    print("You already haave milk")
else:
    print("Oh yeah u need milk")


list=[1,2,3,4,5]
if 1 in list:
    print("rasgula")
else:
    print("no rasgula")