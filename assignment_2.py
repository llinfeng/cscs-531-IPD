'''
More advanced PD game model, using either:
    1. two-dimensional grid
    2. random network
to drive the interactions of players.
'''

'''
Useful links: 
http://networkx.github.io/documentation/latest/reference/functions.html#module-networkx.classes.function

'''

# Required imports
import numpy as np
import itertools
import random
import math
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
from collections import defaultdict


class Grid2D(object):
    '''
    The Grid2D class represents a simple two-dimensional grid.
    '''
    # Dimensions of the grid
    num_rows = 0
    num_cols = 0
    radius = 3 # Neighborhood radius

    def __init__(self, num_rows, num_cols):
        '''
        Constructor that initializes the grid based on a number of rows
        and columns.

        Your task is to create either:
            1. A list of lists; this is comma seperated;
            2. A numpy.array; this would be a vector like stuff.
        '''
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid, self.grid = np.mgrid[0:num_rows,0:num_cols] # The last entry in the list\
                                            # would be (num_rows-1, num_cols-1)


    def put(self, row, col, obj):
        '''
        The put method places an object in a given row/col.

        You should do this by assigning a value to your list-of-lists or
        numpy.array with the proper index.
        '''
        self.grid[row-1,col-1] = obju

    def get(self, row, col):
        '''
        The get method returns an object in a given row/col.

        You should do this by returning the value from your list-of-lists or
        numpy.array with the proper index.
        '''
        return self.grid(row-1,col-1)

    def get_neighbors(self, row, col):
        '''
        The get_neighbors method returns the list of objects/players
        in neighboring cells for the given row/column.

        For extra challenge, add an argument that allows either von Neumann
        or Moore neighborhoods.
        '''
        self.get(row,col).neighbors = []
        for i in range(num_rows):
            for j in range(num_cols):
                if (i-row)**2 + (j-col)**2 < radius**2:
                    self.get(row,col).neighbors.append([i,j])

        return self.get(row,col).neighbors



class RandomNetwork(object):
    '''
    The RandomNetwork class represents a random network that defines
    PD player interactions.
    '''

    # Dimensions of the grid
    num_nodes = 0
    num_edges = 0

    def __init__(self, num_nodes, num_edges):
        '''
        Constructor that initializes the network based on a number of
        nodes and edges.

        Your task is to use networkx to create the graph.  Please see these
        pages:
            * http://networkx.github.io/documentation/latest/tutorial/index.html
            * http://networkx.github.io/documentation/latest/reference/generators.html
        '''
        self.RN = gnm_random_graph(num_nodes,num_edges)

    def put(self, node_id, obj):
        '''
        The put method places an object in a given node_id.

        Node_id starts from 0;
        '''
        self.RN.nodes()[node_id].append(obj)


    def get(self, node_id):
        '''
        The get method returns an object in a given node_id.
        '''
        return self.RN

    def get_neighbors(self, node_id):
        '''
        The get_neighbors method returns the list of adjacent nodes for
        a given node_id.
        '''
        return nx.set_node_attributes(RN,self.RN.neighbors(node_id),bb)


class RandomPlayer(object):
    '''
    RandomPlayer class is a simple PD player who
    has a constant probability of defecting per game.

    Hint: use your answer to assignment_1!
    '''

    # Default probability of defection
    probability_defect = 0.5

    # Score
    score = 0.0

    # History
    history = []

    def __init__(self, probability_defect):
        '''
        Constructor for the player; takes a probability
        of defection as input.

        You will need to set the class variable from the argument.
        '''
        self.probability_defect = probability_defect

    def move(self):
        '''
        The move method returns the player's move based on a
        random draw and their constant probability.

        You will need to:
            1. Draw a random variate from numpy.random.random()
            2. Transform the value into an action
        '''
        if numpy.random.random() <= self.probability_defect:
            return 0 # this is playing C; if rand < probability_defect, not sufficient to defect. 
        else:
            return 1

    def record(self, outcome, score):
        '''
        The record method allows the player to update their score
        and history values if desired.

        I don't see what exactly "outcome" and "score" means. Should the player keep track of his opponents' strategy and score?
        '''
        pass



def gnm_random_graph(n, m, seed=None, directed=False):
    """Return the random graph G_{n,m}.

    Produces a graph picked randomly out of the set of all graphs
    with n nodes and m edges.

    Parameters
    ----------
    n : int
        The number of nodes.
    m : int
        The number of edges.
    seed : int, optional
        Seed for random number generator (default=None).
    directed : bool, optional (default=False)
        If True return a directed graph
    """
    if directed:
        G=nx.DiGraph()
    else:
        G=nx.Graph()
    G.add_nodes_from(range(n))
    G.name="gnm_random_graph(%s,%s)"%(n,m)

    if seed is not None:
        random.seed(seed)

    if n==1:
        return G
    max_edges=n*(n-1)
    if not directed:
        max_edges/=2.0
    if m>=max_edges:
        return complete_graph(n,create_using=G)

    nlist=G.nodes()
    edge_count=0
    while edge_count < m:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)
        if u==v or G.has_edge(u,v):
            continue
        else:
            G.add_edge(u,v)
            edge_count=edge_count+1
    return G
