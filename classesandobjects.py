class Enemy:#normally begin with capital letter
    life = 3
    def attack(self): #self is not a keyword..Alwyas use self to acceess instance(global) variable
        print("ouch!!")
        self.life -= 1

    def checklife(self):
        if self.life<=0:
            print("I am dead")
        else:
            print(str(self.life)+ "life left")

#to access anything inside a class we need to create a object
enemyone=Enemy()  #very imp...we donot need to specify the data type..eg we didnt do int var...float var..similarly we donot need to do class var...jusst var=Class() o create a object
enemyone.attack()
enemyone.checklife()

enemytwo=Enemy() #Note each object is independent to another ..just simple stuff
enemytwo.attack()
enemytwo.checklife()
