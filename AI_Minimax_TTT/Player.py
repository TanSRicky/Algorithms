#----------------------------------------------------------------------------------------
#   Player object contains different kind of players
#                
#   (c) 2020 Arjang Fahim
#
#   Date: 7/26/2020
#   email: fahim.arjang@csulb.edu
#   version: 1.0.0
#----------------------------------------------------------------------------------------

import copy


class Player():
    def __init__(self, board):
        self.board = board

class RandomComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        
    def curr_score(self,board):
        pass
    def next_move(self):
        available_space = copy.deepcopy(self.board.available_space())
        print(available_space)
        square = self.bestMove('O',copy.deepcopy(self.board.board_data),copy.deepcopy(available_space))
    
        self.board.board_data[square["position"]] = self.board.c_letter
        print("BestCompMove")
        print( square)
       # print(self.board.board_data)
    def flipLetter(self,letter):
        if(letter == 'X'): return 'O'
        if(letter == 'O'): return 'X'

    def draw_board(self,board):
                print("\n\n")
                index = 0
                for i in range(3):
                        print("\t\t\t  %s | %s  | %s  \n" %(board[index], board[index + 1], board[index + 2]))
                        index += 3
    def emptySquares(self,board):
        count = 0
        for square in board :
            if square == 0:
                count = count + 1
        return count
    def bestMove(self,letter,board,available_space):
          best = {"score"  :-999,'position':None}
          for curr in available_space:
             board[curr] = letter
             available_space.remove(curr)
             score = self.minimaxtwo(copy.deepcopy(board),False,self.flipLetter(letter),copy.deepcopy(available_space))
             board[curr] = 0
             available_space.insert(0,curr)
             
             #print(best)
             if  score["score"] >= best["score"] and letter == 'O':
              best["score"] = score["score"]
              best["position"] = curr     
          return best   
    def minimaxtwo(self,board,isMaximizing, letter,available_space):
        if self.is_winner('O',copy.deepcopy(board)):
          #  self.draw_board(board)
            return {"score":1}
        if self.is_winner('X',copy.deepcopy(board)):
            # self.draw_board(board)
             return {"score":-1}
        if self.emptySquares(copy.deepcopy(board)) == 0:
              return {"score":0}
        if len(self.emptySquaresList(copy.deepcopy(board)))==0:
             return  {"score":0}
        if(isMaximizing):
              best = {"score"  : -999,'position':None}
              for curr in available_space:
                  board[curr] = letter
                  available_space.remove(curr)
                  score = self.minimaxtwo(copy.deepcopy(board), False,self.flipLetter(letter),copy.deepcopy(available_space))
                  board[curr] = 0
                  available_space.insert(0,curr)
                  best["score"] = max(best["score"], score["score"])
        else:
             best = {"score"  : 999,'position':None}
             for curr in available_space:
                      board[curr] = letter
                      available_space.remove(curr)
                      score = self.minimaxtwo(copy.deepcopy(board), True,self.flipLetter(letter),copy.deepcopy(available_space))
                      board[curr] = 0
                      available_space.insert(0,curr)
                      best["score"] = min(best["score"], score["score"])
                      #print(" Xbest")
                    #  print(best)
        return  best

    
    def is_winner(self, letter,board_data):
                index = 0
                # checking for the row similarity
                for i in range(3):
                        
                        row_set  = set(board_data[index: index+3])
                        if len(row_set) == 1 and (letter in row_set):
                                return True
                        index +=3

                # checking for the column similarity    
                for i in range(3):
                        if (board_data[i] == letter and board_data[i+3] == letter and board_data[i+6] == letter):
                                return True     
        
                if (board_data[0] == letter and board_data[4] == letter and board_data[8] == letter):
                        return True

                if (board_data[2] == letter and board_data[4] == letter and board_data[6] == letter):
                        return True                     

                return False 
    
    def emptySquaresList(self,board):
        count = 0
        spaces = []
        for square in board :
            if square == 0:
                spaces.append(count)
                count = count + 1
        return spaces     
                
    def minimax(self, letter,board,available_space):
        score = dict()
        if letter == 'X':
             best = {"score"  : 999,'position':None}
        elif letter == 'O':
            best = {"score"  :-999,'position':None}
      
  
        if self.is_winner('O',board):
      #      self.draw_board(board)
            score["score"]= 1 * (self.emptySquares(board) + 1)
            return score
        if self.is_winner('X',board):
            # self.draw_board(board)
             score["score"]= -1 * (self.emptySquares(board) + 1)
             return score
        if self.emptySquares(board) == 0:
          #   self.draw_board(board)
              score["score"]= 0
              return score
        if len(self.emptySquaresList(board))==0:
             score["score"]= 0
             return score

        print(score)          
        return best


class HumanPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        

    def next_move(self):
        print("Please enter your move ")
        square = input()
        self.board.board_data[int(square)-1] = self.board.h_letter
        
class SmartPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        pass

    def next_move(self):
        pass

    def is_winner(self, letter):
        pass
                    
    def available_moves(self):
        pass

    def minimax(self, letter):
        pass
        
