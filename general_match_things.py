import pandas as pd
import numpy as np
import plotly.express as px
from shiny import reactive, render, module
from shiny import App, ui
from shinywidgets import output_widget, render_widget
from data_container import df

@module.ui
def general_match_ui():
    return ui.page_fluid(
        output_widget("team_v_total_points"),
        output_widget("avg_auto_pattern_count"),
        output_widget("avg_teleop_pattern_count"),
        output_widget("avg_combined_pattern_count")
    )
@module.server
def general_match_server(input,output,session):

    def get_teams_in_match():
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        return new_df

    @render_widget
    def team_v_total_points():
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        fig = px.box(new_df, x="Team Number", y="Total Points Scored")
        return fig

    @render_widget
    def avg_auto_pattern_count():
        avg_team = get_teams_in_match().groupby("Team Number").mean(numeric_only=True)
        fig_auto_pattern_count = px.bar(avg_team, y="Pattern Correct(Auto)",
                                        title="Average Pattern Correct by Team in Autonomous")
        return fig_auto_pattern_count

    @render_widget
    def avg_teleop_pattern_count():
        avg_team = get_teams_in_match().groupby("Team Number").mean(numeric_only=True)
        fig_teleop_pattern_count = px.bar(avg_team, y = "Pattern Correct(Teleop)",
                                          title = "Average Pattern Correct by Team in Teleop")
        return fig_teleop_pattern_count

    @render_widget
    def avg_combined_pattern_count():
        avg_team = get_teams_in_match().groupby("Team Number").mean(numeric_only=True)
        fig_general_pattern_count = px.bar(avg_team, y=["Pattern Correct(Auto)", "Pattern Correct(Teleop)"],
                                           title="Average Pattern Correct by Team in Teleop and Auto")
        return fig_general_pattern_count

    @render_widget
    def classified_v_overflow_v_depot_scored():
        # add colors, figure out the line separation thing, team thing
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        fig = px.bar(new_df, x="Team Number", y=["Classifier Scored(Teleop)", "Overflow Scored(Teleop)", "Depot Scored(Teleop)"], title="Classifier v. Overflow v. Depot Scored(Teleop)")
        return fig
    @render_widget
    def classified_v_overflow_v_depot_points():
        # add colors, figure out the line separation thing, team thing
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        fig = px.bar(new_df, x="Team Number",
                     y=["Classifier Scored POINTS(Teleop)", "Overflow Scored POINTS(Teleop)", "Depot Scored(Teleop)"],
                     title="Classifier v. Overflow v. Depot Scored POINTS(Teleop)")
        return fig