class Mario():
    def move(self):
        print("I am moving")
class Shroom():
    def eat(self):
        print("Now I am big")


class BigMario(Mario,Shroom):
    pass #pass does nothing

bigmario=BigMario()
bigmario.move()
bigmario.eat()