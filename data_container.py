import pandas as pd
import numpy as np
import plotly.express as px
df=pd.read_csv('data/2526-FIM-TEQ/scouted_data.tsv', sep='\t')



position = df["End Position(Endgame)"]
df["Auto Points Scored"] = df["Classifier Scored(Auto)"]*3 + df["Overflow Scored(Auto)"]*1 + df["Pattern Correct(Auto)"]*2
df["Teleop Points Scored"] = df["Classifier Scored(Teleop)"]*3 + df["Overflow Scored(Teleop)"]*1 + df["Depot Scored(Teleop)"]*1 + df["Pattern Correct(Teleop)"]*2
df["Endgame Points Scored"] = np.where(position == "No", 0, np.where(position == "P", 5, np.where(position == "Sc", 10, np.where(position == "Hh", 20, 0))))
df["Total Points Scored"] = df["Auto Points Scored"] + df["Teleop Points Scored"] + df["Endgame Points Scored"]
df["Shooting Points Scored"] = df["Classifier Scored(Teleop)"]*3 + df["Overflow Scored(Teleop)"]*1 + df["Pattern Correct(Teleop)"]*2
df["Classifier Points Scored(Auto)"] = df["Classifier Scored(Auto)"]*3
df["Overflow Points Scored(Auto)"] = df["Overflow Scored(Auto)"]*1
df["Classifier Scored POINTS(Teleop)"] = df["Classifier Scored(Teleop)"] * 3
df["Overflow Scored POINTS(Teleop)"] = df["Overflow Scored(Teleop)"] * 1
df["Depot Scored POINTS(Teleop)"] = df["Depot Scored(Teleop)"] * 1
df["Team Number"] = df["Team Number"].astype(str)