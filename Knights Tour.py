# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:19:08 2020

@author: Alyssa
"""
def removeVertex(p, adjacent):
    '''
    Parameters
    ----------
    adjacent : dictionary
            Based off of graph, keys contain vertex numbers, 
            value contains list of adjacent vertices
    p : tuple
        Vertex to be removed, 3d coordinates

    Returns
    -------
    None, alters input dict
    '''
    # make a copy of the dict to iterate through as you alter the original
    adjCopy = adjacent.copy()
    for k, v in adjCopy.items():
        for i in v:
            if i == p:
                adjacent[k].remove(i)
        if len(v) == 0:
            del adjacent[k]
        if k == p:
            del adjacent[k]
                
def KnightsTour(adjacent, p):
    '''
    Parameters
    ----------
    adjacent : dictionary
            Based off of graph, keys contain vertex numbers, 
            value contains list of adjacent vertices
    p : int
        Starting position, refers to vertex

    Returns
    -------
    movesMade : dictionary
            Keys refer to move number, values refer to corresponding vertex
    '''
    movesMade = {}
    # keep counter for moves to be used in movesMade
    moves = 1
    # set the starting position as move 1 in dict
    movesMade[moves] = p
    # make a copy of the current position's adjacent dict as p must be deleted
    pCopy = adjacent[p][:]
    
    removeVertex(p, adjacent)
    
    try:
        while len(adjacent) > 0:
                moves += 1
                Min = 25 # keep it at 10, for lattice change to 25
                # find the position that has the least adjacent edges
                for position in pCopy:
                    if len(adjacent[position]) < Min:
                        Min = len(adjacent[position])
                        p = position
                # add the new position as the next move and remove it as a possible position
                movesMade[moves] = p
                pCopy = adjacent[p][:]
                removeVertex(p, adjacent)
    except:
        print(movesMade)
        return "no possible tours"
    else:
        return movesMade
    
# ---------------------------------------------------------
# ICOSAHEDRAL VERTICES:
        
# p = (0, 1, phi)
# moves = KnightsTour(adjac, p)
# # works for first, third subdivision
        
# for k,v in moves.items():
#     ax.text(v[0],v[1],v[2], '%s' % (str(k)), size = 6, zorder = 1, color = 'k')

# ---------------------------------------------------------
# FIB LATTICE
        
# p = coordinates[0]

# moves = KnightsTour(adj, p)
        
# for k,v in moves.items():
#     ax.text(v[0],v[1],v[2], '%s' % (str(k)), size = 6, zorder = 1, color = 'k')

# ---------------------------------------------------------
