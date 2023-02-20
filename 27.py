

class Player:
    def __init__(self, id):
        self.ID = id
        self.color = "w" if id == 0 else "b"

        self.steps = 1
        self.pebbles = 9



class Game:

    def __init__(self):
        self.player0 = 1
        self.player1 = 1
        self.turn = 0
        self.map = self.init_map()


    def init_map(self):
        map = [["b", "b", "b", "b", "b", "b", "b", "b", "b"],
                [], [], [], [], [], [],  [],
                ["w", "w", "w", "w", "w", "w", "w", "w", "w"]]
        print(map)
        return map

    def end_of_turn(self):
        if self.turn == 0:
            self.turn += 1
        else:
            self.turn -= 1


    def calculate_steps(self, player):
        if player == self.player0:
            pass


def main():
    new_map = Map()


if __name__ == "__main__":
    main()