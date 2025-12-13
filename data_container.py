import pandas as pd
import numpy as np
import plotly.express as px
import json

EVENT_CODE = "2526-PA-GIS1"


def load_data():
    df=pd.read_csv(f'data/{EVENT_CODE}/scouted_data.tsv', sep='\t')



    position = df["End Position(Endgame)"]
    df["Auto Points Scored"] = df["Classifier Scored(Auto)"]*3 + df["Overflow Scored(Auto)"]*1 + df["Pattern Correct(Auto)"]*2
    df["Teleop Points Scored"] = df["Classifier Scored(Teleop)"]*3 + df["Overflow Scored(Teleop)"]*1 + df["Depot Scored(Teleop)"]*1 + df["Pattern Correct(Teleop)"]*2
    df["Endgame Points Scored"] = np.where(df["End Position(Endgame)"] == "N", 5,
                                            np.where(df["End Position(Endgame)"] == "P", 10, 0))
    df["Total Points Scored"] = df["Auto Points Scored"] + df["Teleop Points Scored"] + df["Endgame Points Scored"]
    df["Shooting Points Scored"] = df["Classifier Scored(Teleop)"]*3 + df["Overflow Scored(Teleop)"]*1 + df["Pattern Correct(Teleop)"]*2
    df["Classifier Points Scored(Auto)"] = df["Classifier Scored(Auto)"]*3
    df["Overflow Points Scored(Auto)"] = df["Overflow Scored(Auto)"]*1
    df["Classifier Scored POINTS(Teleop)"] = df["Classifier Scored(Teleop)"] * 3
    df["Overflow Scored POINTS(Teleop)"] = df["Overflow Scored(Teleop)"] * 1
    df["Depot Scored POINTS(Teleop)"] = df["Depot Scored(Teleop)"] * 1
    df["Team Number"] = df["Team Number"].astype(str)
    df["Auto Number Scored"] = df["Classifier Scored(Auto)"] + df["Overflow Scored(Auto)"] + df["Pattern Correct(Auto)"]
    df["Teleop Number Scored"] = df["Classifier Scored(Teleop)"] + df["Overflow Scored(Teleop)"] + df["Depot Scored(Teleop)"]

    # Match Name -> [teams in match]
    match_schedule = {}

    with open(f"data/{EVENT_CODE}/toa_matches.json", 'r') as f:
        match_schedule_json = json.load(f)
        for match_json in match_schedule_json:
            teams_in_match = []
            for participants in match_json["participants"]:
                teams_in_match.append(participants["team_key"])

            match_number = match_json["match_name"]
            match_schedule[match_number] = teams_in_match


    with open(f"data/{EVENT_CODE}/toa_teams.json", 'r') as f:
        team_key_json = json.load(f)
        teams_all = []
        for team_json in team_key_json:
            teams_all.append(team_json["team_key"])

    return df, match_schedule, teams_all


df, match_schedule, teams_all = load_data()