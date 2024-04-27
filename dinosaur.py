class Dinosaur:
   def __init__(self, name): 
      self.name = name
      self.skin = "scales"
      self.egg = 'lay eggs'
      self.print_me()
    
   def print_me(self):
      print(f"It's a {self.name}.")
      print(f"All dinosaurs have {self.skin} and {self.egg}.")

   def get_info(self): #Getter
      return(self.skin)
      

class Herbivore(Dinosaur):
    def __init__(self, name):
       super().__init__(name) #calls super class
       self.teeth = "square teeth"
       self.eat_grass()
       
    def eat_grass(self):
        print(f"It eats grass with its {self.teeth}")

class Carnivore(Dinosaur):
    def __init__(self):
       super().__init__()
       self.teeth = "pointy teeth"
       self.eat_meat()
       
    
    def eat_meat(self):
       print(f"It eats meat with its {self.teeth}")


# all_dinos = Dinosaur()


dino_name = "stegosaur"
herbivores = Herbivore(dino_name)


# carnivores = Carnivore()

# scales_or_feathers = all_dinos.get_info()
# print(scales_or_feathers)


      