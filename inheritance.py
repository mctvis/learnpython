class Parent():
    def print_last_name(self):
        print('Adhikari')

class Child(Parent): #inheritance.. inherit from parent class named Parent.
    def print_first_name(self):
        print('Avash')

    #overiding
    def print_last_name(self):
        print('Kennedy')

avash=Child()
avash.print_first_name()
avash.print_last_name()