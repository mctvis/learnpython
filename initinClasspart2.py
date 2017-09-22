class Enemy:
    def __init__(self,x):
        self.energy=x #to understand significance of self , remove self from self.energy in both functions
    def get_energy(self):
        print(self.energy)

jason=Enemy(5)
sandy=Enemy(18)

jason.get_energy()
sandy.get_energy()