while True:
    try:
        number=int(input("Whats ur fave num")) #may be we gonnaa get error here
        print(10/number)
        break
    except ValueError: #if we get value error from above code ...below code is run
        print("Make sure enter a number")
    except ZeroDivisionError:
        print("Dont pick 0")
    except: #general exception
        break
    finally: #no matter what exceute this code
        print("Loop complete")

