from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        self.side = randint(1,self.sides)
        print(self.side)

dice = Dice(20)
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
dice.roll_dice()
