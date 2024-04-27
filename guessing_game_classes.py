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

class Triceratops(Herbivore):
    def __init__(self):
        super().__init__("Triceratops")
        self.special = "two long horns"
        self.size = "small"

class Ankylosaurus(Herbivore):
    def __init__(self):
        super().__init__("Ankylosaurus")
        self.special = "armoured body"
        self.size = "small"

class Brachiosaurus(Herbivore):
    def __init__(self):
        super().__init__("Brachiosaurus")
        self.special = "long neck"
        self.size = "big"

#Carnivores

class T_rex(Carnivore):
    def __init__(self):
        super().__init__("T-Rex")
        self.special = "short arms"
        self.size = "big"


class Velociraptor(Carnivore):
    def __init__(self):
        super().__init__("Velocirator")
        self.special = "smart"
        self.size = "small"

class Dilophodorus(Carnivore):
    def __init__(self):
        super().__init__("Dilophodorus")
        self.special = "can throw poison"
        self.size = "small"

class Gallimimus(Carnivore):
    def __init__(self):
        super().__init__("Gallimimus")
        self.special = "very fast"
        self.size = "small"
