
import random


class Player:
    id = 0
    turn = True
    count = 0
    start = 0
    end = 0
    random_num = 0
    total_turns = 0
    win = False
    def __init__(self, aturn, astart, aend, a_random, aturns, a_Id):
        self.turn = aturn
        self.count = 0
        self.end = aend
        self.start = astart
        self.random_num = a_random
        self.total_turns = aturns
        self.id = a_Id
        self.win = False
    def play(self):

        print(f"Number you have to find lies between {self.start} to {self.end}")
        print(f"You have {self.total_turns} turns to find your target.")
        for i in range(self.total_turns):
            self.count += 1
            choice = int(input("Now Enter your choice(Number) to find out that number generated by computer : "))
            if choice < self.random_num:
                print("Number you have to find is greater than your entered number.")
            elif choice > self.random_num:
                print("Number you have to find is smaller than your entered number.")
            elif choice == self.random_num:
                print(f"CONGRATULATIONS!!! You have won the contest and you have find the generated number which is {self.random_num}")
                print(f"You have find your target in {self.count} turns.")
                self.win = True
                return self.count

        print(f"You couldn't find that generated Number :*(. Better luck next time.... The number was {self.random_num}")
        pass
    def __repr__(self):
        if self.win:
            print(f"Player {self.id} have won the contest and he find the target in {self.count} turns.")
        else:
            print("No Player find the target in given turns....")

if __name__ == '__main__':
    ls = []
    num_of_players = int(input("Enter number of players in this game : "))
    for i in range(num_of_players):
        turns = int(input(f"Enter how many turs you want to give to player {i+1} : "))
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        rand = random.randint(num1, num2)
        print(f"random number : {rand}")
        player = Player(True, num1, num2, rand, turns, i+1)
        count = player.play()
        ls.append(player)
    ls.sort(key = lambda p:p.count)
    ls[0].__repr__()



