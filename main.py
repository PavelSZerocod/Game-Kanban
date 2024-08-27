import random

class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона")

    def is_alive(self):
        return self.health > 0



class Game():
    def __init__(self):
        self.player = Hero(name="Игрок")
        self.computer = Hero(name="Компьютер")

    def start(self):
        print("Игра началась - в бой!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

        print(f"{self.player.name}:{self.player.health} здоровья")
        print(f"{self.computer.name}:{self.computer.health} здоровья")
        print("-" * 30)

        input("Нажмите Enter, чтобы продолжить игру")

        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Компьютер победил!")


if __name__ == "__main__":
    game = Game()
    game.start()






