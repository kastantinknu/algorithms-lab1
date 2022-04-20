# -*- coding: cp1251 -*-
#from LDFS.LDFS import LDFS
from RBFS.RBFS import RBFS
import random
import time

#chessbpards generator
def generate_chessboards(number):
    result = []
    for _ in range(number):
        board = []
        for j in range(8):
            is_added = False
            while not is_added:
                queen = [random.randint(0, 7), j]
                if queen not in board:
                    board.append(queen)
                    is_added = True
        result.append(board)
    return result

#hardcod chessboard
chessboards = [
    [[7, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]]
    #,
    #[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]],
    #[[1, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[3, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [5, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [9, 7]],
    #[[4, 0], [0, 1], [7, 2], [3, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [2, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [0, 7]],
    #[[4, 0], [0, 1], [0, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [6, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [0, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [5, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [6, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [8, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [5, 7]],
    #[[4, 0], [6, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [9, 5], [1, 6], [3, 7]],
    #[[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [9, 7]],
    #[[4, 0], [0, 1], [3, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]]
]

#result printer
print('------RBFS------')
#print for all chessboard
for chessboard in chessboards:
    #time stamp 
    start_time = time.time()

    #initialize class object and load chessboard to Recursive Best-First Search algorithm 
    rbfs = RBFS(chessboard)

    #print original chessboard
    print('Input chessboard = ' + str(chessboard))

    #run method - Recursive Best-First Search algorithm
    rbfs.recursive_best_first_search()

    #run method - Recursive Best-First Search answer
    print(rbfs.answer)

    #run method - Recursive Best-First Search calculate state number
    print('states number = ' + str(rbfs.states_number))

    #run method - Recursive Best-First Search calculate iteration number
    print('iterations = ' + str(rbfs.iterations))

    #
    print('dead ends = ' + str(rbfs.dead_ends))

    #calculate time difference

    print("%s seconds" % (time.time() - start_time))
    #print final chessboard 
    print("")

line = ['X - - - - - - -'
       ,'- X - - - - - -'
       ,'- - X - - - - -'
       ,'- - - X - - - -'
       ,'- - - - X - - -'
       ,'- - - - - X - -'
       ,'- - - - - - X -'
       ,'- - - - - - - X']

i = 0
j = 0
while i < 8:
    while j < 8:
        if 7-i == chessboard[j][0]:
            print(line[j])
        j += 1
    j = 0
    i += 1





















#number_col = 0
#iterator = 0
#print('------chessboard------')
#while iterator < 8:
#    for chessboard in chessboards:
#        while number_col < 8:
#            if chessboard[number_col][0]==7:
#                print(line[number_col])
#        number_col += 1
#    print(number_col)
#iterator += 1



#number_col = 0
#iterator = 0
#print('------chessboard------')
#while iterator < 8:
#  while number_col < 8:
#     print(iterator)
#     number_col += 1
#print(number_col)
#iterator += 1



#number = 0
#while number < 8:
#    print(number)
#    number += 1
#iterator = 0
#row = 0
#col = 0
#while iterator < 8:
#    while row < 8:
#        for chessboard in chessboards:
#            if chessboard[col][0]==7:
#                print(line[col]) 
#        while col < 8:
#            print(col, row, iterator)
#            if chessboard[col][0]==7:
#              print(line[col]) 
#            row += 1
#            col += 1
#            iterator += 1
#      #print(col, row, iterator)
#        row += 1
#        iterator =0
#        col =0


#print(chessboards[0])



#i = 0
#j = 0
#while i < 8:
#    while j < 8:
#        if j == chessboard[j][1]:
#            if i == chessboard[j][0]:
#                print(line[chessboard[j][0]])
#        ##print(i, j, end="\t")
#        #if chessboard[j][0]==7:
#        #    print(line[0])
#        #elif chessboard[j][0]==6:
#        #    print(line[1])
#        #elif chessboard[j][0]==5:
#        #    print(line[2])
#        #elif chessboard[j][0]==4:
#        #    print(line[3])
#        #elif chessboard[j][0]==3:
#        #    print(line[4])
#        #elif chessboard[j][0]==2:
#        #    print(line[5])
#        #elif chessboard[j][0]==1:
#        #    print(line[6])
#        #elif chessboard[j][0]==0:
#        #    print(line[7])
#        j += 1

#    j = 0
#    i += 1

#i = 0
#j = 0
#while i < 8:
#    while j < 8:
#        print(i, j, end="\t")
#        j += 1
#    print("\n")
#    j = 0
#    i += 1








#for chessboard in chessboards:
#    if chessboard[number_col][0]==7:
#        print(line[number_col])
#print(number_col)
#number_col += 1




#    elif chessboard[1][0]==7:
#        print('- X - - - - - -')
#    elif chessboard[2][0]==7:
#        print('- - X - - - - -')
#    elif chessboard[3][0]==7:
#        print('- - - X - - - -')
#    elif chessboard[4][0]==7:
#        print('- - - - X - - -')
#    elif chessboard[5][0]==7:
#        print('- - - - - X - -')
#    elif chessboard[6][0]==7:
#        print('- - - - - - X -')
#    elif chessboard[7][0]==7:
#        print('- - - - - - - X')
#    else:
#        print('')

#number = 1
 
#while number < 5:
#    print(number)
#    number += 1



    #print(chessboard[0][0]
    #      , chessboard[1][0]
    #      , chessboard[2][0]
    #      , chessboard[3][0]
    #      , chessboard[4][0]
    #      , chessboard[5][0]
    #      , chessboard[6][0]
    #      , chessboard[7][0])
    #print('-')
#print()

#for chessboard in chessboards:
#    for chess in chessboard:
#        print('-')


#print(chessboards[0][0], chessboards[0][1])

#, print(),
#print(chessboards[0][2])
#,print(chessboards[1])
     #print(chessboard[2]),
     #print(chessboard[3]),
     #print(chessboard[4])

        #if chess[1]==0:
    #        print('X')
    #    else:
    #        print('--')
    #if chessboard[0] == 0:
    #    print(line[0])
    #elif chess[0] == 1:
    #    print(line[1])
    #elif chess[0] == 2:
    #    print(line[2])
    #elif chess[0] == 3:
    #    print(line[3])
    #elif chess[0] == 4:
    #    print(line[4])
    #elif chess[0] == 5:
    #    print(line[5])
    #elif chess[0] == 6:
    #    print(line[6])
    #elif chess[0] == 7:
    #    print(line[7])
    #else:
    #for chess in chessboard:
    #    #print(chess[0])
    #    if chess[0] == 0:
    #        print(line[0])
    #    elif chess[0] == 1:
    #        print(line[1])
    #    elif chess[0] == 2:
    #        print(line[2])
    #    elif chess[0] == 3:
    #        print(line[3])
    #    elif chess[0] == 4:
    #        print(line[4])
    #    elif chess[0] == 5:
    #        print(line[5])
    #    elif chess[0] == 6:
    #        print(line[6])
    #    elif chess[0] == 7:
    #        print(line[7])
    #    else:
    #        print('- - - - - - - -')


#print(chess[1])


#print('------RBFS------')
#for chessboard in generate_chessboards(20):
#    start_time = time.time()
#    rbfs = RBFS(chessboard)
#    print('Input chessboard = ' + str(chessboard))
#    rbfs.recursive_best_first_search()
#    print(rbfs.answer)
#    print('states number = ' + str(rbfs.states_number))
#    print('iterations = ' + str(rbfs.iterations))
#    print('dead ends = ' + str(rbfs.dead_ends))
#    print("%s seconds" % (time.time() - start_time))
#    print()

#print('------LDFS------')
#for chessboard in chessboards:
#    start_time = time.time()
#    ldfs = LDFS(chessboard, 10)
#    print('Input chessboard = ' + str(chessboard))
#    ldfs.depth_limited_search()
#    print(ldfs.answer)
#    print('states number = ' + str(ldfs.states_number))
#    print('iterations = ' + str(ldfs.iterations))
#    print('dead ends = ' + str(ldfs.dead_ends))
#    print("%s seconds" % (time.time() - start_time))
#    print()
