class Girl:
    gender="female" #this is class variable  common for all girls

    def __init__ (self,name):
        self.name=name #this is instance variable which is gonna be different for each girl

r=Girl('Rachel')
s=Girl('Habibi')
print(r.name)
print(s.name)
print(r.gender)
print(s.gender)
print(Girl.gender)