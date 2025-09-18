import random
from exercise_2_dogs import Dog  

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = ', '.join([dog.name for dog in args] + [self.name])
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet")


dog_a = PetDog("Rocky", 4, 20)
dog_b = PetDog("Lucky", 3, 15)
dog_a.train()
dog_a.play(dog_b)
dog_a.do_a_trick()
