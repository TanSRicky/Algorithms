#-------------------------------------------------------------------
#       Converts a standard gameboard to a maze and can solve the maze 
#                                
#       (c) 2020 Ricky Tan 018662109
#
#       Date: 07/13/2020
#       email: Tan.Ricky@student.csulb.edu
#   version: 1.0.0
#------------------------------------------------------------------

from array import *
import traceback
import sys
import collections
class GameBoard(object):
        
        def __init__(self, maze_file):
                self.file = maze_file
                self.list = ({})
                self.goal = None
                self.start = None
                self.goalIndex = None
                self.startIndex = None
                self.numNodes = None
                self.mapList = []
                self.coordMap = ({})
                # load your data here


        # returns goal node position
        def GoalNode(self):
                return self.goalIndex

        # returns starting node position        
        def StartNode(self):
                return self.startIndex
                # returns goal node position
                
        def GoalNodeNumber(self):
                return self.goal

        # returns starting node position        
        def StartNodeNumber(self):
                return self.start

        #creates matrix out of .lay file
        def MazeMatrix_Build(self):
                print("Building gameboard...")
                line = file.readline()
               
                self.mapList.append(line)
                #get lines as list of  lists 
                while line:
                        line = file.readline()
                        self.mapList.append(line)
                count = 0
                colSize = 0
                vertexSet = set()
                rowSize = len(self.mapList[0])-1
                #get all vertices that we can "stand" on (non boundary nodes)
                for i in range(0,len(self.mapList)):

                    for j in range(0,len(self.mapList[i])):
                       if(self.mapList[i][j] == 'P'):
                               self.start = count
                               vertexSet.add(count)
                               self.startIndex = "[" + str(i) + "][" + str(j)+ "]"
                       if(self.mapList[i][j] == '.'):
                               self.goal = count
                               self.goalIndex = "[" + str(i) + "][" + str(j) + "]"
                               vertexSet.add(count)
                       if(self.mapList[i][j] == ' '):
                               vertexSet.add(count)
                       if(self.mapList[i][j] !=  '\n'):
                               count = count +1
                               self.coordMap[count] = [i,j]
                    colSize = colSize + 1
                    size = rowSize*(colSize-1)
                self.numNodes = size
                print("Detected rows : \t" + str(rowSize))
                print("Detected columns: \t" + str(colSize-1))
                print("Number of unique nodes: " + str(size))
                #initialize matrix
                matrix = [[0 for x in range(size)] for y in range(size)]
                #for all Non-boundary nodes, add their neighbor 
                for i in range(0, size):
                    tmpList = []
                    if i in vertexSet : 
                          up = i - rowSize 
                          down =  i + rowSize
                          left = i - 1
                          right = i +1
                          if up in vertexSet :
                                matrix[i][up]=1
                                matrix[up][i] =1
                                tmpList.append(up)
                          if down in vertexSet :
                                matrix[i][down]=1
                                matrix[down][i] =1
                                tmpList.append(down)
                          if left in vertexSet :
                                matrix[i][left]=1
                                matrix[left][i] =1
                                tmpList.append(left)
                          if right in vertexSet :
                                matrix[i][right]=1
                                matrix[right][i] =1
                                tmpList.append(right)
                #save reference so we can save the matrix into a file
                          self.list[i] = tmpList                
                self.mat= matrix
                print("len " + str(len(vertexSet)))
                pass
                

        def SaveMatrix(self): 
            original_stdout = sys.stdout # Save a reference to the original standard output

            with open('maze.txt', 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                for i in range(0,len(self.mat)):
                               for j in range(0,len(self.mat[i])):
                                       print(self.mat[i][j], end = " ")
                               print()
                sys.stdout = original_stdout # Reset the standard output to its original value
                pass

        def PlotSolution(self, solution, path):
                # Don't worry about it for now, we may use it foe the next assignment
                pass
      
        def BFS(self):
                queue = []
                visited = set()
                path = []
                queue.insert(0,self.start)
                parents = ({})
                parents[self.start] = self.start

                
                while len(queue) > 0 :
                    curr = queue.pop(len(queue)-1) #Pop from fringe
                    visited.add(curr)
                    print("Size of Q " + str(len(queue)))
                    if(curr == self.goal):
                 #       print(curr)
                        print(len(visited))
                        break
                    for n in self.list[curr]:
                      if n not in visited:
                          parents[n] = curr    
                          queue.insert(0,n)    
                  #  print(curr)
                count = 0
                solution = []
                solPath = []
                curr = self.goal
                nxt = parents[self.goal]
                while(curr != nxt):
                        curr = parents[curr]
                        nxt = parents[curr]
                        solPath.append(curr)
                print( "Visited "  + str(len(visited)))
                print("Path len : " + str(len(solPath)))  
                for i in range(0,len(self.mapList)):
                    tmpLine = []
                    for j in range(0,len(self.mapList[i])):
                        if(count in solPath and self.mapList[i][j] != '\n' and self.mapList[i][j] != '%'and self.mapList[i][j] != 'P'):
                          tmpLine.append(".")
                        else:
                          tmpLine.append(self.mapList[i][j])
                        if(self.mapList[i][j] !=  '\n'): count = count + 1
                    solution.append(tmpLine)
                for line in solution:
                   print(line)
                original_stdout = sys.stdout # Save a reference to the original standard output

                with open('sol.txt', 'w') as f:
                    sys.stdout = f # Change the standard output to the file we created.
                    for i in range(0,len(solution)):
                               for j in range(0,len(solution[i])):
                                       print(solution[i][j],end="")
                sys.stdout = original_stdout # Reset the standard output to its original value
                pass
   
                    

    
        def DFS(self):
                queue = []
                visited = set()
                path = []
                queue.insert(0,self.start)
                parents = ({})
                parents[self.start] = self.start
                while len(queue) > 0 :
                    curr = queue.pop(0)
                    visited.add(curr)
                  #  print("Size of Q " + str(len(queue)))
                    if(curr == self.goal):
                 #       print(curr)
                        print(len(visited))
                        break
                    for n in self.list[curr]:
                      if n not in visited:
                          parents[n] = curr    
                          queue.insert(0,n)    
                  #  print(curr)
                count = 0
                solution = []
                solPath = []
                curr = self.goal
                nxt = parents[self.goal]
                while(curr != nxt):
                        curr = parents[curr]
                        nxt = parents[curr]
                        solPath.append(curr)
                print("Path len : " + str(len(solPath)))           
                print( "Visited "  + str(len(visited)))   
                for i in range(0,len(self.mapList)):
                    tmpLine = []
                    for j in range(0,len(self.mapList[i])):
                        if(count in solPath and self.mapList[i][j] != '\n' and self.mapList[i][j] != '%'and self.mapList[i][j] != 'P'):
                          tmpLine.append(".")
                        else:
                          tmpLine.append(self.mapList[i][j])
                        if(self.mapList[i][j] !=  '\n'): count = count + 1
                    solution.append(tmpLine)
                for line in solution:
                   print(line)
                original_stdout = sys.stdout # Save a reference to the original standard output

                with open('sol.txt', 'w') as f:
                    sys.stdout = f # Change the standard output to the file we created.
                    for i in range(0,len(solution)):
                               for j in range(0,len(solution[i])):
                                       print(solution[i][j],end="")
                sys.stdout = original_stdout # Reset the standard output to its original value
                print(self.coordMap)
                pass
            
        def Astar(self):
                queue = []
                visited = set()
                path = []
                queue.insert(0,self.start)
                parents = ({})
                parents[self.start] = self.start
                node = self.start
                
                while len(queue) > 0 :
                    prevMin = self.manhattan(queue[0],self.goal)
                     
                    for n in queue:
                        if self.manhattan(n,self.goal) <= prevMin :
                            prevMin = self.manhattan(n,self.goal)
                            node = n 
                    queue.remove(node)
                    curr = node
                    visited.add(curr)
                    
                    if(curr == self.goal):
                 #       print(curr)
                        print(len(visited))
                        break
                    for n in self.list[curr]:
                        if n not in visited:
                           parents[n] = curr     
                           queue.append(n)
                     
                      
                count = 0
                solution = []
                solPath = []
                curr = self.goal
                nxt = parents[self.goal]
                print( "Visited "  + str(len(visited)))   
                while(curr != nxt):
                        curr = parents[curr]
                        nxt = parents[curr]
                        solPath.append(curr)
                print("Path len : " + str(len(solPath)))        
                for i in range(0,len(self.mapList)):
                    tmpLine = []
                    for j in range(0,len(self.mapList[i])):
                        if(count in solPath and self.mapList[i][j] != '\n' and self.mapList[i][j] != '%'and self.mapList[i][j] != 'P'):
                          tmpLine.append(".")
                        else:
                          tmpLine.append(self.mapList[i][j])
                        if(self.mapList[i][j] !=  '\n'): count = count + 1
                    solution.append(tmpLine)
                for line in solution:
                   print(line)
                original_stdout = sys.stdout # Save a reference to the original standard output

                with open('sol.txt', 'w') as f:
                    sys.stdout = f # Change the standard output to the file we created.
                    for i in range(0,len(solution)):
                               for j in range(0,len(solution[i])):
                                       print(solution[i][j],end="")
                sys.stdout = original_stdout # Reset the standard output to its original value
                pass
   
                    
   
                    
        def minManhattan(self,n):
               prevMin = self.manhattan(self.start,self.goal)
               for n in self.list[n1]:
                    if self.manhattan(n,self.goal) > prevMin :
                            prevMin = n
               return n             
                       
                       
                                                
        def manhattan(self,n1,n2):
               return abs(self.coordMap[n1][0] -  self.coordMap[n2][0]) + abs(self.coordMap[n1][1] - self.coordMap[n2][1])
           
        #Function to check my solution against sample solution
        def checkBoard(self):
                file = open(r"bigMatrix.txt","r")
                print("Checking solution...")
                line = file.readline()
                mapList = []
                mapList.append(line.split())
                #get lines as list of  lists 
                while line:
                        line = file.readline()
                        mapList.append(line.split())
                count = 0
                colSize = 0
                vertexSet = set()
                rowSize = len(mapList[0])-1
                
                #get all vertices that we can "stand" on (non boundary nodes)
                for i in range(0,len(mapList)):
                    for j in range(0,len(mapList[i])):
                       if(mapList[i][j] == 'P'  and mapList[i][j] != '\t'):
                               vertexSet.add(count)
                       if(mapList[i][j] == '.' and mapList[i][j] != '\t' ):
                               vertexSet.add(count)
                       if(mapList[i][j] == ' '  and mapList[i][j] != '\t' ):
                               vertexSet.add(count)
                       if(mapList[i][j] !=  '\n'  and mapList[i][j] != '\t'):
                               count = count +1
                    colSize = colSize + 1
                size = rowSize*(colSize-1)
            
                for i in range(0,self.numNodes):
                        for j in range(0,self.numNodes):
                              if(int(mapList[i][j]) != int(self.mat[i][j])):
                                      print("Difference found")
                                      break
                            
                
              
       
                 
                
                



#------------------------[End of class Gameboard]----------------------------------------       


try :                 
    #file = open(r"smallMaze.lay", "r")
    file = open(r"bigMaze.lay", "r")
    game_board = GameBoard(file)
    game_board.MazeMatrix_Build()
    game_board.SaveMatrix()
    print("Start node matrix index:" + str(game_board.StartNode()))
    print("Goal node matrix index: " + str(game_board.GoalNode()))
    print("Start node number :\t" + str(game_board.StartNodeNumber()))
    print("Goal node number :\t" + str(game_board.GoalNodeNumber()))
    print("Game board saved succesfully")
    game_board.Astar()
    # game_board.checkBoard()
except:
    print("Game board failed to save : \n")
    traceback.print_exc(file=sys.stdout)


