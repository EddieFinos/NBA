#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:58:21 2024

@author: eddiefinos
"""
import pandas as pd

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

player_dict = players.get_players()

def player_id(player_name):
    for player in player_dict:
        if player['full_name'] == player_name:
            return player['id']

def player_gamelog(player_id):
    player_gamelog = playergamelog.PlayerGameLog(player_id= player_id, season = SeasonAll.all)
    df_player_gamelog = player_gamelog.get_data_frames()[0]
    return df_player_gamelog


def average_points_all(gamelog):
    total_points = 0
    total_games = 0
    for _, game in gamelog.iterrows():
        if game['MIN'] > 0:
            total_games += 1
            total_points += game['PTS']
    average = total_points / total_games if total_games > 0 else 0
    return average

def average_points_season(gamelog, season):
    total_points = 0
    total_games = 0
    for _, game in gamelog.iterrows():
        if game['MIN'] > 0 and game['SEASON_ID'].endswith(season):
            total_games += 1
            total_points += game['PTS']
    average = total_points / total_games if total_games > 0 else 0
    return average

def average_rebounds_season(gamelog, season):
    total_rebounds = 0
    total_games = 0
    for _, game in gamelog.iterrows():
        if game['MIN'] > 0 and game['SEASON_ID'].endswith(season):
            total_games += 1
            total_rebounds += game['REB']
    average = total_rebounds / total_games if total_games > 0 else 0
    return average

def average_assists_season(gamelog, season):
    total_assists = 0
    total_games = 0
    for _, game in gamelog.iterrows():
        if game['MIN'] > 0 and game['SEASON_ID'].endswith(season):
            total_games += 1
            total_assists += game['AST']
    average = total_assists / total_games if total_games > 0 else 0
    return average



player = player_id('LeBron James')
player_gamelog = player_gamelog(player)
average_pts_all = average_points_all(player_gamelog)
average_pts_season = average_points_season(player_gamelog, '22024')
average_reb_season = average_rebounds_season(player_gamelog, '22024')
average_ast_season = average_assists_season(player_gamelog, '22024')




dslkafj;dslkfj
