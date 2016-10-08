'''
Created on 18-Jun-2016

@author: pavitra-ubuntu
'''
import TeamMgmt, PlayerPool


if __name__ == '__main__':
    
    # These inputs could be read from user, but I am too lazy to do that now.
    
    #pool = PlayerPool.PlayerPool(10, [1,2,3], [4,5,6], [7,8,9,10], [1,1,3,1,1,3,2,2,3,4])
    #teams = TeamMgmt.Team(1,1,1,3)
    pool = PlayerPool.PlayerPool(20, ['a','b','c','d','e','f'], \
                                 ['g','h','i','j','k','l'], \
                                 ['m','n','o','p','q','r','s','t'], \
                                 [1,1,2,2,2,3,1,1,1,2,3,3,1,1,2,2,3,3,3,4])
    teams = TeamMgmt.Team(3,2,1,6)
    
    
    while (not teams.done()):
        
        skill_to_add = ''
        player_to_add = 0
        team_to_add = teams.team_needing_players()
        level = 1
        
        while (True):
            current_players_to_consider = pool.get_strongest_players(level)
            available_skills = current_players_to_consider.keys()
            skill_to_add = teams.skill_to_consider(available_skills, team_to_add)
            if (skill_to_add == ''):
                level = level + 1
            else:
                player_to_add = current_players_to_consider[skill_to_add][0]
                break
            
        strength = pool.get_player_strength(player_to_add)            
        teams.add_player(team_to_add, player_to_add, strength, skill_to_add)
        pool.remove_player(player_to_add)
        
        #for optimization
        if (teams.skill_done(skill_to_add)):
            pool.remove_skill(skill_to_add)
            
    teams.print_teams()
    
