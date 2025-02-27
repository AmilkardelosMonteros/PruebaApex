import numpy as np
import random
board = np.array([[0,0,0,0],\
                 [0,0,0,0],\
                 [0,0,-0.4,0],\
                 [0,0,1,-0.1]])

class agent:
    def __init__(self,board):
        self.board                             = board
        self.is_visited                        = np.array([[False for x in range(4)], [False for x in range(4)], [False for x in range(4)], [False for x in range(4)]])
        self.current_position                  = [3,1]#[np.random.randint(len(self.board)),np.random.randint(len(self.board))]
        self.is_visited[self.current_position[0],self.current_position[1]] = True
        self.trayectory                        = [[self.current_position[0],self.current_position[1]]]
        self.rewards                           = [self.board[self.current_position[0],self.current_position[1]]]
        self.steps = 1
        

    def move_left(self):
        self.current_position[1] -=1
        print(self.current_position)
        self.trayectory.append([self.current_position[0],self.current_position[1]])
        self.rewards.append(self.board[self.current_position[0],self.current_position[1]])

    def move_right(self):
        self.current_position[1] +=1
        print(self.current_position)
        self.trayectory.append([self.current_position[0],self.current_position[1]])
        self.rewards.append(self.board[self.current_position[0],self.current_position[1]])
        

    def move_up(self):
        self.current_position[0] -=1
        print(self.current_position)
        self.trayectory.append([self.current_position[0],self.current_position[1]])
        self.rewards.append(self.board[self.current_position[0],self.current_position[1]])

    def move_down(self):
        self.current_position[0] +=1
        print(self.current_position)
        self.trayectory.append([self.current_position[0],self.current_position[1]])
        self.rewards.append(self.board[self.current_position[0],self.current_position[1]])
        

    def moves_right(self):
        print('rigth')
        while self.current_position[1] !=3:
            self.move_right()

    def moves_up(self):
        print('up')
        while self.current_position[0] != 0:
            self.move_up()
        
    def moves_left(self):
        print('left')
        while self.current_position[1] != 0:
            self.move_left()

    def moves_down(self):
        print('down')
        while self.current_position[0] != 3:
            self.move_down()
    

    def moves_cuadro_externo(self):
        print('cuadro externo')
        if self.current_position[0] == 3:
            print('Caso1')
            self.moves_right()
            self.moves_up()
            self.moves_left()
            self.moves_down()
        elif self.current_position[0] == 0:
            print('Caso2')
            self.moves_left()
            self.moves_down()
            self.moves_right()
            self.moves_up()
        elif self.current_position[1] == 0:
            print('Caso3')
            self.moves_down()
            self.moves_right()
            self.moves_up()
            self.moves_left()
        elif self.current_position[1] == 3:
            print('Caso4')
            self.moves_down()
            self.moves_right()
            self.moves_up()
            self.moves_left()

    def moves_cuadro_interno(self):
        print(self.current_position)
        #two cases:
        if self.current_position in [[1,1],[1,2],[2,1],[2,2]]:
            print('cuadro interno')
            if self.current_position == [1,1]:
                self.move_down()
                self.move_right()
                self.move_up()
                self.move_up()
            elif self.current_position == [2,1]:
                self.move_right()
                self.move_up()
                self.move_left()
                self.move_left()
            elif self.current_position == [2,2]:
                self.move_left()
                self.move_up()
                self.move_right()
                self.move_right()
            elif self.current_position == [1,2]:
                self.move_left()
                self.move_down()
                self.move_right()
                self.move_right()

    def solve(self):
        if self.current_position[0] == 3:
            if self.current_position[1] in [1,2]:
                self.move_up()
            elif self.current_position == [3,0]:
                self.move_right()
                self.move_up()
            elif self.current_position == [3,3]:
                self.move_left()
                self.move_up()
            self.moves_cuadro_interno()
            self.moves_cuadro_externo()

        elif self.current_position[0] == 0:
            ...
        elif self.current_position[1] == 0:
            ...
        elif self.current_position[1] == 3:
            ...
        argmax  = np.argmax(self.rewards)
        casilla = self.trayectory[argmax] 
        print(f'The goal is {casilla}')
 

def main():
    Agent = agent(board)
    Agent.solve()


if __name__ == '__main__':
    main()