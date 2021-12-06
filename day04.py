#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advent of code day 4, problem 1 & 2

# import pandas as pd
import numpy as np
test ={'draws' : [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1,],
        'boards' : [[22, 13, 17, 11, 0],
                    [ 8,  2, 23,  4, 24],
                    [21, 9, 14, 16,  7],
                    [6, 10,  3, 18, 5],
                    [1, 12, 20, 15, 19], 
                    [ 3 ,15,  0,  2, 22],
                    [ 9, 18, 13, 17, 5],
                    [19,  8,  7, 25, 23],
                    [20, 11, 10, 24, 4],
                    [14, 21, 16, 12, 6],
                    [14, 21, 17, 24,  4],
                    [10, 16, 15,  9, 19],
                    [18,  8, 23, 26, 20],
                    [22, 11, 13,  6,  5],
                    [ 2,  0, 12,  3,  7]]}

def check_board(slice):
    '''Check if individual board is a winner'''
    all_rows = np.asarray([slice[ r, :].all() for r in range(slice.shape[0])])
    all_cols = np.asarray([slice[:, c].all() for c in range(slice.shape[1])])

    if (all_rows).any() or (all_cols).any():
        return True
    else:
        return False

def identify_winner(draws, boards):
    '''Idetifying winning board that matches draws
    
        Returns:
            draw : int
                The winning draw
            widx : int
                The index of the winning board
            bid : array
                The boolean array representing drawn values
    '''

    bidx = np.zeros(shape = boards.shape, dtype='bool')

    # winner = False,
    count = 0
    # while not winner and count < draws.shape[0]:
    while count < len(draws):
        # print('in while...')
        draw = draws.pop(0)

        idx = np.where(boards == draw)
        bidx [idx] = True

        if 5 <= count:
            # print('in if1...')
            board_status = np.asarray([check_board(bidx[b, :, :]) for b in range(boards.shape[0])])
            
            if board_status.any():
                winner = True
                widx =  np.where(board_status==True)[0] 

                # return (np.sum(boards[widx, :, :]))
                return(draw, widx[0], bidx[widx,:,:][0])

        count += 1

def identify_all_winners(draws, boards):
    '''Idetifying data for all winning boards  
    
        Returns:
            winners : dict with:
                draw : int
                    The winning draw
                widx : int
                    The index of the winning board
            bidx : array
                The boolean array representing drawn values
    '''

    bidx = np.zeros(shape = boards.shape, dtype='bool')

    # winner = False,
    count = 0
    winners={}
    # while not winner and count < draws.shape[0]:
    # while (count < len(draws)) and (boards.shape[0] >= 0):
    while (0 < len(draws)) :
        # print('in while...')
        draw = draws.pop(0)

        idx = np.where(boards == draw)
        bidx [idx] = True

        if 5 <= count:
            # print('in if1...')
            board_status = np.asarray([check_board(bidx[b, :, :]) for b in range(boards.shape[0])])
            
            if board_status.any():
                # winner = True
                widx =  np.where(board_status==True)[0]

                # winners[str(draw)] = {widx[0]: bidx[widx,:,:][0] }
                winners[str(draw)] = draw * boards[widx[0],~bidx[widx,:,:][0]].sum()

                boards = np.delete(boards, widx[0], axis = 0)
                bidx = np.delete(bidx, widx[0], axis = 0 )

                # for w in list(widx):
                #     if w not in winners.values():
                #         winners[str(draw)] = w              
        count += 1

    return (winners)

with open('./data/day04.txt', 'r') as src:
    data = [l for l in (line.strip() for line in src) if l]

# get draws, then figure out how to deal with board
draws = list(np.fromstring(data[0],int, sep=','))
data.pop(0)

boards = [np.fromstring(d, int, sep=' ' ) for d in data]
boards = np.asarray(boards).ravel().reshape((100, 5,5))
  
draw, widx, bidx = identify_winner(draws, boards)

final_score = draw * boards[widx,~bidx].sum()      
print('final score is: {}'.format(final_score))


# part 2
# function identify_all_winners didn't procue
with open('./data/day04.txt', 'r') as src:
    data = [l for l in (line.strip() for line in src) if l]

# get draws, then figure out how to deal with board
draws = list(np.fromstring(data[0],int, sep=','))
data.pop(0)

boards = [np.fromstring(d, int, sep=' ' ) for d in data]
boards = np.asarray(boards).ravel().reshape((100, 5,5))

wins =  identify_all_winners(draws, boards)

# last win with non-0 score is draw 75, with score of 2475
# which is not correct


