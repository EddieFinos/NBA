#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:58:21 2024

@author: eddiefinos
"""
import pandas as pd

from nba_api.stats.static import players
player_dict = players.get_players()

from nba_api.stats.endpoints import playergamelog
import pandas as pd 

from nba_api.stats.library.parameters import SeasonAll


def player_id(player_name):
    for player in player_dict:
        if player['full_name'] == player_name:
            return player['id']

print(player_id('JamesOn Curry'))




def player_gamelog(player_id):
    player_gamelog = playergamelog.PlayerGameLog(player_id= player_id, season = SeasonAll.all)
    df_player_gamelog = player_gamelog.get_data_frames()[0]
    return df_player_gamelog
df = player_gamelog(201191)




print(player_id('JamesOn Curry'))
df = player_gamelog(201191)
