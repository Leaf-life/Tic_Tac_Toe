import os

class Tic_Tac_Toe():
    def __init__(self) -> None:
        self.Main()

    def Main(self):
        '''Main Method, instalies all importat vzribles and holds the main loop and win condition for the game'''
        Size = 3
        self.Master_Array = [[ "_" for i in range(Size)] for j in range(Size)]
        self.turn = "X"
        Victor = False
        while Victor == False:
            self.Display()
            self.input_space()
            Victor = self.Check()
            self.Turn()
            if Victor:
                self.Display()
                print("Victory")

    def Display(self):
        '''Creates the Tic Tac Toe board and displya it the the players'''
        self.clear()
        n = len(self.Master_Array)
        print(" _" * n)
        for y in range(n):
            for x in range(n):
                print("|" + self.Master_Array[y][x], end = "")
            print("|")

    def clear(self):
        '''delets pass boards and moves'''
        os.system("cls" if os.name == "nt" else "printf '\033c'")

    def input_space(self):
        "Allows the user to impot spaces ranging from 1-9 for a 3x3 board"
        spot = int(input(""))
        if spot <= 3:
            self.Master_Array[0][spot-1] = self.turn
        elif spot <= 6:
            self.Master_Array[1][spot-4] = self.turn
        elif spot <= 9:
            self.Master_Array[2][spot-7] = self.turn

    def Check(self):
        '''Determines the win condition'''
        vert = self.Vert()
        hort = self.Hort()
        diag = self.Diag()
        if vert or hort or diag:
            return True
        else:
            return False

    def Hort(self):
        '''Checks the horizontall rows for a win or not'''
        n = len(self.Master_Array)
        for y in range(n):
            Victory = 0
            for x in range(n):
                if self.Master_Array[y][x] == self.turn:
                    Victory += 1
            if Victory == 3:
                return True
        return False

    def Vert(self):
        '''Checks the vertical rows for a win or not'''
        n = len(self.Master_Array)
        for y in range(n):
            Victory = 0
            for x in range(n):
                if self.Master_Array[x][y] == self.turn:
                    Victory += 1
            if Victory == 3:
                return True
        return False

    def Diag(self):
        '''checks the diaganls for a win or not'''
        n = len(self.Master_Array)
        Victory = 0
        Victory2 = 0
        for pos in range(n):
            if self.Master_Array[pos][pos] == self.turn:
                Victory += 1
            if self.Master_Array[pos][(n-1) - pos] == self.turn:
                print(pos)
                Victory2 += 1
        if Victory == n or Victory2 == n:
            return True
        else:
            return False

    def Turn(self):
        '''Determines whos turn it is and changes it every time the game loops'''
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

if __name__ == '__main__':
    Tic_Tac_Toe()