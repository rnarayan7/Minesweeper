import random

class MinesweeperEngine:

    def __init__(self):
        self.active = True

    def startGame(self, board_size: int):
        self.mines = set()
        self.board_size = board_size
        self.board = [["*" for x in range(self.board_size)] for y in range(self.board_size)]
        self.num_unknown_squares = self.board_size*self.board_size
        num_mines = self.num_unknown_squares // 7

        while len(self.mines) < num_mines:
            x = random.randint(0, self.board_size - 1)
            y = random.randint(0, self.board_size - 1)
            self.mines.add((x,y))

    def hit(self, x: int, y: int):
        if (x,y) in self.mines:
            self.board[x][y] = "X"
            print("You hit a mine!")
            print("GAME OVER")
            self.active = False
        else:
            stk = [(x, y)]
            visited = set()
            while stk:
                (a, b) = stk.pop()
                num_local_mines = 0
                add_to_stk = []
                if a - 1 >= 0:
                    w = a - 1
                    if (w, b) in self.mines:
                        num_local_mines += 1
                    elif self.board[w][b] == "*" and (w, b) not in visited:
                        visited.add((w, b))
                        add_to_stk.append((w, b))
                if a + 1 < self.board_size:
                    e = a + 1
                    if (e, b) in self.mines:
                        num_local_mines += 1
                    elif self.board[e][b] == "*" and (e, b) not in visited:
                        visited.add((e, b))
                        add_to_stk.append((e, b))
                if b - 1 >= 0:
                    n = b - 1
                    if (a, n) in self.mines:
                        num_local_mines += 1
                    elif self.board[a][n] == "*" and (a, n) not in visited:
                        visited.add((a, n))
                        add_to_stk.append((a, n))
                if b + 1 < self.board_size:
                    s = b + 1
                    if (a, s) in self.mines:
                        num_local_mines += 1
                    elif self.board[a][s] == "*" and (a, s) not in visited:
                        visited.add((a, s))
                        add_to_stk.append((a, s))
                if a - 1 >= 0 and b - 1 >= 0:
                    w = a - 1
                    n = b - 1
                    if (w, n) in self.mines:
                        num_local_mines += 1
                    elif self.board[w][n] == "*" and (w, n) not in visited:
                        visited.add((w, n))
                        add_to_stk.append((w, n))
                if a - 1 > 0 and b + 1 < self.board_size:
                    w = a - 1
                    s = b + 1
                    if (w, s) in self.mines:
                        num_local_mines += 1
                    elif self.board[w][s] == "*" and (w, s) not in visited:
                        visited.add((w, s))
                        add_to_stk.append((w, s))
                if a + 1 < self.board_size and b - 1 >= 0:
                    e = a + 1
                    n = b - 1
                    if (e, n) in self.mines:
                        num_local_mines += 1
                    elif self.board[e][n] == "*" and (e, n) not in visited:
                        visited.add((e, n))
                        add_to_stk.append((e, n))
                if a + 1 < self.board_size and b + 1 < self.board_size:
                    e = a + 1
                    s = b + 1
                    if (e, s) in self.mines:
                        num_local_mines += 1
                    elif self.board[e][s] == "*" and (e, s) not in visited:
                        visited.add((e, s))
                        add_to_stk.append((e, s))
                if num_local_mines:
                    self.board[a][b] = str(num_local_mines)
                else:
                    stk.extend(add_to_stk)
                    self.board[a][b] = " "
                self.num_unknown_squares -= 1

        if self.num_unknown_squares == len(self.mines):
            for mine in self.mines:
                self.board[mine[0]][mine[1]] = "X"
            print("You Won!")
            print("GAME OVER")
            self.active = False

    def printCurrentGame(self):
        indeces = map(lambda x: str(x), list(range(self.board_size)))
        top_string = "  " + " ".join(indeces)
        print(top_string)
        for i in range(self.board_size):
            current_string = str(i) + " " + " ".join(self.board[i])
            print(current_string)

    def isActive(self):
        return self.active

    def getBoardSize(self):
        return self.board_size

if __name__ == "__main__":
    print("*** MINESWEEPER ***")
    engine = MinesweeperEngine()
    active = True
    print("What do you want the dimension of the board to be? Input one value, dimension is (input * input)")
    dimension = input()
    while True:
        try:
            dimension = int(dimension)
            assert(dimension > 0)
            break
        except Exception:
            print("Invalid input, try again")
    engine.startGame(board_size = dimension)
    engine.printCurrentGame()

    while active:
        print("Next hit:")

        # Input x
        x, y = None, None
        while True:
            print("x:")
            x = input()
            try:
                x = int(x)
                assert(x >= 0)
                assert(x < engine.getBoardSize())
                break
            except Exception:
                print("Invalid input, try again")

        # Input y
        while True:
            print("y:")
            y = input()
            try:
                y = int(y)
                assert(y >= 0)
                assert(y < engine.getBoardSize())
                break
            except Exception:
                print("Invalid input, try again")

        # Call hit on board
        engine.hit(x, y)

        # Output board
        engine.printCurrentGame()

        # Check if game finished
        active = engine.isActive()
        if active is False:
            print("Would you like to start a new game? (y or n)")
            answer = input().lower()
            while answer != "y" and answer != "n":
                print("Invalid input, try again")
                answer = input().lower()
            if answer == "y":
                active = True
                print("What do you want the dimension of the board to be? Input one value, dimension is (input * input)")
                dimension = input()
                while True:
                    try:
                        dimension = int(dimension)
                        assert(dimension > 0)
                        break
                    except Exception:
                        print("Invalid input, try again")
                engine.startGame(board_size = dimension)
                engine.printCurrentGame()
