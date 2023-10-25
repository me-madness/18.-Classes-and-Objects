# First task from the lecture

class Zoo:
    __animals = 0
    def __init__(self,name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        
    
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)    
    
    def get_info(self, species):
        pass
    
    
zoo_name = input() 
zoo_object = Zoo(zoo_name)       
count_of_animals = int(input())
for animals in range(count_of_animals):
    species, name = input().split()
    zoo_object.add_animal(species, name)


## Input one
# Great Zoo
# 5
# mammal lion
# mammal bear
# fish salmon
# bird owl
# mammal tiger
# mammal

## Input two
# Blah
# 1
# mammal bear
# mammal


# Second task from me
