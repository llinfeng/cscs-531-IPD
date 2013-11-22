'''
Simple PD game model.
'''

# Numpy imports
import numpy.random


class SimpleGame(object):
    # Payoff matrix; we didn't use Numpy here.  
    payoff_matrix = [[(3, 3), (0, 5)],
                    [(5, 0), (1, 1)]]

    # Game history
    game_history = []

    def __init__(self, player_list):
        self.players = player_list
        self.player1 = self.players[0]
        self.player2 = self.players[1]

    def payoff(self):
        move1 = self.player1.move() 
        move2 = self.player2.move()
        return self.payoff_matrix[move1][move2]

    def run(self):
        '''
        Run method to run an actua9
        You will need to do the following:
            1. Ask players for their moves
            2. Score the moves to determine their payoffs
            3. Update their scores
            4. Record their histories
        '''
        moves = [self.players[0].move(),self.players[1].move()]
        score = self.payoff()
        self.game_history.append([moves[0], moves[1]])
        self.player1.record(moves,score)
        self.player2.record(moves,score)
        return [score]

'''
Given the current rule of payoff assignment, I can only come up with the following two-player-class 
structure to keep track of game history.

'''

class RandomPlayer1(object):
    probability_defect = 0.5
    score = 0.0
    history = []
    outcome = []
    def __init__(self, probability_defect):
        '''
        Constructor for the player; takes a probability
        of defection as input.

        You will need to set the class variable from the argument.
        '''
        self.probability_defect = probability_defect

    def move(self):
        if numpy.random.random() <= self.probability_defect:
            return 0 # this is playing C; if rand < probability_defect, not sufficient to defect. 
        else:
            return 1

    def record(self,outcome,score):
        self.outcome.append(score[0])
        if self.move() < 0.5: 
            self.history.append('C')
        else:
            self.history.append('D')

class RandomPlayer2(object):
    probability_defect = 0.5
    score = 0.0
    history = []
    outcome = []
    def __init__(self, probability_defect):
        '''
        Constructor for the player; takes a probability
        of defection as input.

        You will need to set the class variable from the argument.
        '''
        self.probability_defect = probability_defect

    def move(self):
        if numpy.random.random() <= self.probability_defect:
            return 0 # this is playing C; if rand < probability_defect, not sufficient to defect. 
        else:
            return 1

    def record(self,outcome,score):
        self.outcome.append(score[1])
        if self.move() < 0.5: 
            self.history.append('C')
        else:
            self.history.append('D')





player_1 = RandomPlayer1(0.5)
player_2 = RandomPlayer2(0.25)
print player_2.move()
playerlist = [player_1, player_2]

# Create game
SG = SimpleGame(playerlist)
result = SG.run()
print result


print 'player 1 played ' + str(SG.player1.history) + "and got" + str(SG.player1.outcome)
print SG.player1.move() 

print 'player 2 played ' + str(SG.player2.history) + "and got" + str(SG.player2.outcome)
print SG.player2.move()


'''
Remark after setting up the code

    1. Accessing the game history: to access the history/record of a single SG, need access 
    through the mother class. 

    2. Using the generating player will yield another random draw, and therefore the strategy
    returned may not necessarily be the one played by the players in the game. 

    3. Use self.XXX when referring to class instance, or else python don't take XXX as a globle name 
    and won't be notified what it is. 

    To conclude: it took me 3 hours to figure all the above, sadly. The usage of "outcome" and "history" and 
    "score" are confusing. It would be better to layout a specs explaining what each variable does. 

    
'''