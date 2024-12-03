import pandas as pd
import sys
from scipy.stats import pearsonr
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

def six_year_lebron_output():
    lebron_id = player_id('LeBron James')
    lebron_gamelog = player_gamelog(lebron_id)
    lebron_data = []
    for year in range(2019, 2025):
        lebron_pts = average_points_season(lebron_gamelog, str(year))
        lebron_rbs = average_rebounds_season(lebron_gamelog, str(year))
        lebron_ast = average_assists_season(lebron_gamelog, str(year))
        lebron_data.append({'Year': year, 'PTS': lebron_pts, 'REB': lebron_rbs, 'AST': lebron_ast})
    lebron_df = pd.DataFrame(lebron_data)
    return lebron_df

lebron_df = six_year_lebron_output()
print(lebron_df)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(lebron_df['PTS'], "g", label='PTS')
ax.plot(lebron_df['REB'], "r", label='REB')
ax.plot(lebron_df['AST'], "b", label='AST')
fig.suptitle("LeBron 6 Year Average", fontsize=16);
ax.set_xlabel('Last 6 years')
ax.set_ylabel('Average # (PTS, REB, AST)')
ax.legend()
plt.show()

correlation_pts_ast, p_value_pts_ast = pearsonr(lebron_df['PTS'], lebron_df['AST'])
correlation_pts_reb, p_value_pts_reb = pearsonr(lebron_df['PTS'], lebron_df['REB'])
correlation_reb_ast, p_value_reb_ast = pearsonr(lebron_df['REB'], lebron_df['AST'])

print(f"Correlation between PTS and AST: {correlation_pts_ast}, P-value: {p_value_pts_ast}")
print(f"Correlation between PTS and REB: {correlation_pts_reb}, P-value: {p_value_pts_reb}")
print(f"Correlation between REB and AST: {correlation_reb_ast}, P-value: {p_value_reb_ast}")
print ("Using an alpha of 0.05 you can tell that the only significant corrleation would be between average points and average asists in the last 6 years. That correlation of -0.8127 means that it is a strong negative correlation between the two variables. That means that if lebrons points goes up in a year that means his assists usually decrease. That is very interesting becuase that could be because if he is scoring a lot of points that also means he is probably not passing the ball to get assists so it makes sense.")
