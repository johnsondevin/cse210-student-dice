import random

class Thrower:
    """Code that allows for the director of the game to roll the dice.

    Attributes:
        dice: The list of numbers that the player rolls
        num_throws: A counter of how many times the player rolls each game  
    """

    def __init__(self):
        """The class constructor

        Arguments:
            self (Thrower): An instance of Thrower
        """
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        """Determines if the player rolled a 1 or a 5, or if the number of rolls
        is greater than 0 and returns a boolean value to the director.do_outputs
        function.

        Arguments:
            self (Thrower): An instance of Thrower
        """
        for num in self.dice:
            if num == 1 or num == 5 or self.num_throws > 0:
                valid_player = True
            else:
                valid_player = False

        return valid_player        

    def get_points(self):
        """Code that adds the rolled numbers together and returns that number
        to the function call.

        Arguments:
            self (Thrower): An instance of Thrower
        """
        points = 0

        for i in self.dice:
            if i == 1:
                points += 100
            elif i == 5:
                points += 50

        return points

    def throw_dice(self):
        """Code that rolls the dice for the player.

        Arguments:
            self (Thrower): An instance of Thrower
        """
        for i in range(5):
            if self.num_throws == 0:
                self.dice.append(random.randint(1,6))
            else:
                self.dice[i] = random.randint(1,6)
        self.num_throws += 1