from dino_classes import Stegosaur, Triceratops, Ankylosaurus, Brachiosaurus, T_rex, Velociraptor, Dilophosaurus, Gallimimus, Parasaurolophus



                                #Class instances

stegosaur = Stegosaur()
triceratops = Triceratops()
ankylosaurus = Ankylosaurus("Ankylosaurus") #Its name start with a vowel, so I had to make a slight change to the method and add an extra attribute
brachiosaurus = Brachiosaurus()
t_rex = T_rex()
velociraptor = Velociraptor()
dilophosaurus = Dilophosaurus()
gallimimus = Gallimimus()
parasaurolophus = Parasaurolophus()

# Stock them in an array
computer_guess = [stegosaur, t_rex, velociraptor, brachiosaurus, gallimimus, triceratops, ankylosaurus, dilophosaurus, parasaurolophus]

                                #If remaining guess in array == 1, stop the game

if len(computer_guess) == 1:
    computer_guess[0].print_me()
    exit()


                                 #Variables


user_choice = input("Do you have a dinosaur in mind? Type 'Yes' or 'No': ")

ask_questions = [
                "Does it stand on two legs? ",
                "Does it eat meat? ",
                "Is it big? ",
                "Does it have scales on its back? ",
                "Does it have a long neck? ",
                "Does it have horns? ",
                "Does it have an armoured body?: ",
                "Does it have a crest on its head?: ",
                "Does it have tiny arms? ",
                "Is it smart? ",
                "Is it fast? ",
                "Can it throw poison? "]


                                #Functions 


#Will only take the carnivores/Herbivores or big/small according to the answer
def sort_by(array, func):
   return list(filter(func, array)) #Has to be turned into a list

#Filters Herbivores and Carnivores #Serves as argument(func) for the function sort_by  
def is_herbivore(dino):
    return dino.food == "grass" 

def is_carnivore(dino):
    return dino.food == "meat" 

#Filters big and small
def is_big(dino):
    return dino.size == "big"

def is_small(dino):
    return dino.size == "small"

#Filters two and four legs
def two_legs(dino):
   return dino.legs == "two"

def four_legs(dino):
   return dino.legs == "four"


#Finds the name of the dino in the array #Serves as argument(func) for the function sort_by 
def find(array, object):
    found_index = array.index(object)
    if(found_index >= 0):
       return array[found_index] #If -1, the program is gonna crash



                                #Ready?

if (user_choice == "no"):
   print("Take your time to think and start again :)")
   exit()

                                #Computer asks questions

#Stands on two or four legs

answer_is_two_legs = input(ask_questions[0])

if answer_is_two_legs == "yes":
   computer_guess = sort_by(computer_guess, two_legs)
else:
   computer_guess = sort_by(computer_guess, four_legs)


#Meat-eater?

is_meat = input(ask_questions[1])

if is_meat == "yes":
   computer_guess = sort_by(computer_guess, is_carnivore)
else:
   computer_guess = sort_by(computer_guess, is_herbivore)


#Is it big?

guess_is_big = input(ask_questions[2])

if guess_is_big == "yes":
   computer_guess = sort_by(computer_guess, is_big)
else:
   computer_guess = sort_by(computer_guess, is_small)


                            #More specific questions

#Does not work if I don't declare the variables beforehand
has_scales = ""
long_neck = ""
has_tiny_arms = ""
armour = ""
has_crest = ""
has_horns = ""
is_fast = ""
is_smart = ""
throw_poison = ""



if is_meat == "no" and guess_is_big == "yes": #If Herbivore and Big
    has_scales = input(ask_questions[3])
   

if has_scales == "yes":
   steg = find(computer_guess, stegosaur)
   steg.print_me()
   exit()
elif has_scales == "no":
    long_neck = input(ask_questions[4])
    if long_neck == "yes":
        brac = find(computer_guess, brachiosaurus)
        brac.print_me()
        exit()
    elif long_neck == "no":
     has_horns = input(ask_questions[5])
    if has_horns == "yes":
      tric = find(computer_guess, triceratops)
      tric.print_me()
      exit()

# if is_meat == "no" and guess_is_big == "no":   #  if Herbivore and Small
#    armour = input(ask_questions[6])


if is_meat == "yes" and guess_is_big == "yes":  # if Carnivore and Big
    has_tiny_arms = input(ask_questions[8])

if has_tiny_arms == "yes":
   rex = find(computer_guess, t_rex)
   t_rex.print_me()
   exit()

if is_meat == "yes" and guess_is_big == "no":  #If Carnivore and Small
   is_smart = input(ask_questions[9])

if is_smart == "yes":
   vel = find(computer_guess, velociraptor)
   vel.print_me()
   exit()

elif is_smart == "no":
   is_fast = input(ask_questions[10])

if is_fast == "yes":
   gal = find(computer_guess, gallimimus)
   gal.print_me()
   exit()

elif is_fast == "no":
   throw_poison = input(ask_questions[11])

if throw_poison == "yes":
      dilo = find(computer_guess, dilophosaurus)
      dilo.print_me()
else:  
   print("Sorry, I couldn't find the answer.")



