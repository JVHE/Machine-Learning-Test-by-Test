import random
class NumberGuesser:
    """It guesses next number using input histories"""
    def __init__(self):
        self._guessed_numbers = []
    def number_was(self, guessed_number):
        self._guessed_numbers.append(guessed_number)
    def numbers_were(self, guessed_numbers):
        self._guessed_numbers += guessed_numbers
    def guess(self):
        if self._guessed_numbers == []:
            return None
        return random.choice(self._guessed_numbers)
