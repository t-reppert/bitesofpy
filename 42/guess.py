MAX_GUESSES = 5
START, END = 1, 20
import random

def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        inpt = input("Guess a number between 1 and 20: ")
        if inpt == "" or inpt == None:
            raise ValueError("Please enter a number")
        if type(inpt) != int:
            if not inpt.isdigit():
                raise ValueError("Should be a number")
            else:
                guess = int(inpt)
        else:
            guess = inpt
        if guess < 1 or guess > 20:
            raise ValueError("Number not in range")
        if guess in self._guesses:
            raise ValueError("Already guessed")
        else:
            self._guesses.add(guess)
            return guess


    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        elif guess < self._answer:
            print(f'{guess} is too low')
            return False
        elif guess > self._answer:
            print(f'{guess} is too high')
            return False
        

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while not self._win:
            try:
                guess = self.guess()
            except ValueError as e:
                print(e)
                continue
            if guess == False:
                continue
            resp = self._validate_guess(guess)
            if resp:
                self._win = True
                print(f'It took you {len(self._guesses)} guesses')
                break
            if len(self._guesses) == 5:
                print(f'Guessed 5 times, answer was {self._answer}')
                break
            

if __name__ == '__main__':
    game = Game()
    game()