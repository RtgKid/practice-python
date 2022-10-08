import time


class AnimalNode:
    def __init__(self, animal_type, name = None, next=None):
        self.name = name
        self.time = time.time()
        self.animal_type = animal_type
        self.next = next

    def print(self):
        p = self
        while p:
            print(p.name, p.time)
            p = p.next


class Shelter:
    def __init__(self):
        self.cats = None
        self.last_cat = None
        self.dogs = None 
        self.last_dog = None

    def print(self):
        if self.cats: 
            p = self.cats
            print("Cats")
            p.print()
            
        if self.last_cat:
            print("Last cat ")
            self.last_cat.print()
        
        if self.dogs:
            p = self.dogs
            print("Dogs")
            p.print()

        if self.last_dog:
            print("Last dog ")  
            self.last_dog.print() 
        
        print('\n')

    def enqueue(self, animal : AnimalNode):
        if animal.animal_type == 'cat':
            if not self.cats:
                self.cats = animal
                self.last_cat = animal
            else:
                self.last_cat.next = animal
                self.last_cat = animal
        elif animal.animal_type == 'dog':
            if not self.dogs:
                self.dogs = animal
                self.last_dog = animal
            else:
                self.last_dog.next = animal
                self.last_dog = animal

    def __getFirstCat(self):
        if self.cats:
            p = self.cats
            if not p.next:
                self.last_cat = None
            
            self.cats = p.next
            return p

    def __getFirstDog(self):
        if self.dogs:
            p = self.dogs
            if not p.next:
                self.last_dog = None

            self.dogs = p.next    
            return p

    def dequeueAny(self):
        if self.cats and self.dogs and self.cats.time < self.dogs.time:
            return self.__getFirstCat()
        else:
            return self.__getFirstDog()

    def dequeueCat(self):
        return self.__getFirstCat()

    def dequeueDog(self):
        return self.__getFirstDog()

    
shelter = Shelter()
shelter.enqueue(AnimalNode('cat', 'c1'))
shelter.enqueue(AnimalNode('cat', 'c2'))
shelter.enqueue(AnimalNode('dog', 'd1'))
# shelter.enqueue(AnimalNode('cat', 'c3'))
# shelter.enqueue(AnimalNode('dog', 'd2'))
shelter.print()
shelter.dequeueAny()
shelter.enqueue(AnimalNode('dog', 'd3'))
shelter.print()
shelter.dequeueDog()
shelter.dequeueCat()
shelter.print()