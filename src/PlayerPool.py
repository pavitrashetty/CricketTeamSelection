'''
Created on 18-Jun-2016

@author: pavitra-ubuntu
'''

import copy

class PlayerPool(object):
    

    def __init__(self, N, a, b, c, S):
        self.N = N
        self.batsmen = a
        self.bowlers = b
        self.wkeepers = c
        self.all_players = a + b + c
        self.m = len(a)
        self.o = len(b)
        self.p = len(c)
        self.S = S
        self.PL = copy.deepcopy(self.all_players)
        
        
    def get_strongest_players(self, level):
        result  = {}
        sorted_S = sorted(self.S)
        max_value = sorted_S[level * -1]
        for player in self.PL:
            if (self.S[self.all_players.index(player)] == max_value):
                if (player in self.batsmen):
                    if 'BAT' not in result:
                        result['BAT'] = [player]
                    else:
                        result['BAT'].append(player)
                elif (player in self.wkeepers):
                    if 'WK' not in result:
                        result['WK'] = [player]
                    else:
                        result['WK'].append(player)
                elif (player in self.bowlers):
                    if 'BOWL' not in result:
                        result['BOWL'] = [player]
                    else:
                        result['BOWL'].append(player)
        return result
    
    
    
    def get_player_strength(self, player):
        return self.S[self.all_players.index(player)]        
    
    
    
    def remove_player(self, player):
        self.PL.remove(player)
        
        
    
    def remove_skill(self, skill):
        if (skill == 'BAT'):
            self.PL = [x for x in self.PL if x not in self.batsmen]
        if (skill == 'BOWL'):
            self.PL = [x for x in self.PL if x not in self.bowlers]
        if (skill == 'WK'):
            self.PL = [x for x in self.PL if x not in self.wkeepers]
            
            
              
        
        
         
               
        