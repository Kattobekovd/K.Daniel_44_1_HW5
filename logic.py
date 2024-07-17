import random

class Game:
    def __init__(self, min_number, max_number, attempts, initial_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.attempts = attempts
        self.capital = initial_capital

    def start(self):
        print(f"Добро пожаловать в игру 'Угадай число'!")
        print(f"У вас {self.capital} сомов, и {self.attempts} попыток, чтобы угадать число от {self.min_number} до {self.max_number}.")
        target_number = random.randint(self.min_number, self.max_number)

        while self.attempts > 0 and self.capital > 0:
            try:
                bet = int(input("Введите вашу ставку: "))
                if bet > self.capital or bet <= 0:
                    print(f"Ваша ставка должна быть положительной и не превышать ваш капитал ({self.capital}).")
                    continue

                guess = int(input(f"Угадайте число от {self.min_number} до {self.max_number}: "))

                if guess == target_number:
                    self.capital += bet
                    print(f"Поздравляем! Вы угадали число. Ваш текущий капитал: {self.capital}.")
                    break
                else:
                    self.capital -= bet
                    self.attempts -= 1
                    print(f"Неверно! У вас осталось {self.attempts} попыток и {self.capital} сомов.")

            except ValueError:
                print("Введите допустимое число.")

        if self.capital <= 0:
            print("Вы проиграли весь капитал!")
        elif self.attempts <= 0:
            print(f"Ваши попытки закончились! Загаданное число было {target_number}.")

        print("Спасибо за игру!")
