def add_numbers(*args):  #flexible argument commonly named as args
    total = 0
    for a in args:
        total+=a
    print(total)

add_numbers(3)
add_numbers(3,43,55,66)

