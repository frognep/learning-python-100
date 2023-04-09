# DETECTING COLLISION W/ FOOD
# CREATE A SCOREBOARD
# DETECT COLLISION WITH A WALL
# DETECT COLLISION WITH TAIL

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")
    
class Fish(Animal):
     
    # super() obtains all attributes from the super class + more
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)