import random

class GuessGame:
    random_number = 0
    number_of_tries = 0

    def start_game(self):
        self.random_number = random.randrange(1, 11)
        self.number_of_tries = 4
        return " Привет, Игрок! \n" \
               "Предлагаю сыграть тебе в игру. \nПравила просты: я загадываю тебе цифру от 1 до 10, а ты угадываешь ее. \n" \
                "Игра началась. У тебя есть " + str(self.number_of_tries) + " попытки!"

    def guess_number(self, guessed_number):
        if self.isPlayable():
            self.number_of_tries = self.number_of_tries - 1
            if guessed_number < self.random_number:
                return "Введенное число меньше чем загаданное. У тебя осталось " + str(self.number_of_tries) + " попытки."
            elif guessed_number > self.random_number:
                return "Введенное число больше чем загаданное. У тебя осталось " + str(self.number_of_tries) + " попытки."
            else:
                self.number_of_tries = 0
                self.user_won = True
                return "Ты абсолютно прав!!! Поздравления, ты победил!!!"
        else:
            return "К сожалению ты проиграл. Начни новую игру, если хочешь сыграть еще раз"

    def isPlayable(self):
        return self.number_of_tries > 0