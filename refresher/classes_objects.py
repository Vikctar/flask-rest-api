class LotteryPlayer:
    def __init__(self):
        self.name = 'Kalf'
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player = LotteryPlayer()
print(player.name)
print(player.total())

player_one = LotteryPlayer()
player_two = LotteryPlayer()

print(player_one == player_two)
print(player_one.name == player_two.name)
