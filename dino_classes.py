    
                            #Main classes

class Herbivore:
    def __init__(self, dino_name):
        self.food = "grass"
        self.dino_name = dino_name

    def print_me(self):
        print(f"It's a {self.dino_name}!")


class Carnivore:
    def __init__(self, dino_name):
        self.food = "meat"
        self.dino_name = dino_name
    
    def print_me(self):
       print(f"It's a {self.dino_name}!")

        

                                # Subclasses
#Herbivores

class Stegosaur(Herbivore):
    def __init__(self, ):
        super().__init__("Stegosaur")
        self.special = "scales on its back"
        self.size = "big"
        self.legs = "four"

class Triceratops(Herbivore):
    def __init__(self):
        super().__init__("Triceratops")
        self.special = "two long horns"
        self.size = "big"
        self.legs = "four"

class Ankylosaurus(Herbivore):
    def __init__(self, dino_name):
        super().__init__("Ankylosaurus")
        self.special = "armoured body"
        self.size = "small"
        self.legs = "four"
        self.dino_name = dino_name

    def print_me(self):
        print(f"It's an {self.dino_name}!")

class Brachiosaurus(Herbivore):
    def __init__(self):
        super().__init__("Brachiosaurus")
        self.special = "long neck"
        self.size = "big"
        self.legs = "four"

class Parasaurolophus(Herbivore):
    def __init__(self):
        super().__init__("Parasaurolophus")
        self.special = "crest on its head"
        self.size = "small"
        self.legs = "four"

#Carnivores

class T_rex(Carnivore):
    def __init__(self):
        super().__init__("T-Rex")
        self.special = "short arms"
        self.size = "big"
        self.legs = "two"


class Velociraptor(Carnivore):
    def __init__(self):
        super().__init__("Velocirator")
        self.special = "smart"
        self.size = "small"
        self.legs = "two"

class Dilophosaurus(Carnivore):
    def __init__(self):
        super().__init__("Dilophosaurus")
        self.special = "can throw poison"
        self.size = "small"
        self.legs = "four"

class Gallimimus(Carnivore):
    def __init__(self):
        super().__init__("Gallimimus")
        self.special = "very fast"
        self.size = "small"
        self.legs = "two"
