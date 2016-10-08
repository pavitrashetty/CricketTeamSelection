'''
Created on 18-Jun-2016

@author: pavitra-ubuntu
'''
from __builtin__ import True
import math

class Team(object):


    def __init__(self, x, y, z, k):
        self.max = {'TOTAL': k, 'BAT' : x, 'BOWL' : y, 'WK' : z}
        
        self.A = []
        self.A_players = {'TOTAL' : 0, 'BAT' : 0, 'BOWL' : 0, 'WK' : 0}
        self.A_strength = 0

        self.B = []
        self.B_players = {'TOTAL' : 0, 'BAT' : 0, 'BOWL' : 0, 'WK' : 0}
        self.B_strength = 0
        
        self.skill_set = {1 : 'BAT', 2 : 'BOWL', 3 : 'WK'}
        self.skill_prioritize()
        
        
    def skill_prioritize(self):
        if (self.max['WK'] < self.max['BOWL']):
            if (self.max['WK'] < self.max['BAT']):
                self.skill_set[1] = 'WK'
                if (self.max['BAT'] < self.max['BOWL']):
                    self.skill_set[2] = 'BAT'
                    self.skill_set[3] = 'BOWL'
                else:
                    self.skill_set[3] = 'BAT'
                    self.skill_set[2] = 'BOWL'
        elif (self.max['BOWL'] < self.max['WK']):
            if (self.max['BOWL'] < self.max['BAT']):
                self.skill_set[1] = 'BOWL'
                if (self.max['BAT'] < self.max['WK']):
                    self.skill_set[2] = 'BAT'
                    self.skill_set[3] = 'WK'
                else:
                    self.skill_set[3] = 'BAT'
                    self.skill_set[2] = 'WK'
        elif (self.max['WK'] < self.max['BOWL']):
            self.skill_set[3] = 'BOWL'
            self.skill_set[2] = 'WK'          
        
        
        
    def add_player(self, team, player, strength, skill):
        if (team == 'A'):
            self.A.append(player)
            self.A_players['TOTAL'] = self.A_players['TOTAL'] + 1
            self.A_strength = self.A_strength + strength
            self.A_players[skill] = self.A_players[skill] + 1
        else:
            self.B.append(player)
            self.B_players['TOTAL'] = self.B_players['TOTAL'] + 1
            self.B_strength = self.B_strength + strength
            self.B_players[skill] = self.B_players[skill] + 1
            
            
    def print_teams(self):
        print ("Team A players = " + str(self.A))
        print ("Team B players = " + str(self.B))
        print ("Team A strength = " + str(self.A_strength) + "; Team B strength = " + str(self.B_strength))
        print("Team strength difference = " + str(math.fabs(self.A_strength - self.B_strength)))
        
        
        
    def team_needing_players (self):
        team = 'A'
        if (self.B_strength < self.A_strength) or (self.B_players['TOTAL'] < self.A_players['TOTAL']):
            team = 'B'
        return team
    
    
    def done(self):
        if (self.A_players['TOTAL'] == self.max['TOTAL'] and self.B_players['TOTAL'] == self.max['TOTAL']):
            return True
        else:
            return False
        
        
        
    def skill_done(self, skill):
        if (self.A_players[skill] == self.max[skill] and self.B_players[skill] == self.max[skill]):
            return True
        else:
            return False        
        
        
    
    def skill_to_consider (self, available_skills, selected_team):

        if (len(available_skills) == 1):
            skill = available_skills[0]
            if ((selected_team == 'A' and self.A_players[skill] < self.max[skill]) or (self.B_players[skill] < self.max[skill])):
                return skill
            else:
                return ''
            
        # more than 1 skill available, lets go by priority
        for i in range(1,4):
            skill = self.skill_set[i]
            if (selected_team == 'A'):
                if (skill in available_skills and self.A_players[skill] < self.B_players[skill]):
                    return skill
            else:
                if (skill in available_skills and self.B_players[skill] < self.A_players[skill]):
                    return skill
            
        # for available skills, selected team can right now take no more players as compared to other team
        # hence, check against max number of players for selected team
        for i in range(1,4):
            skill = self.skill_set[i]
            if (selected_team == 'A'):
                if (skill in available_skills and self.A_players[skill] < self.max[skill]):
                    return skill
            else:
                if (skill in available_skills and self.B_players[skill] < self.max[skill]):
                    return skill
                
        # selected team can take no players of available skills currently. Sad.
        return ''

 
    
        
        
        
        