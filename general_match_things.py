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
        output_widget("avg_combined_pattern_count"),
        output_widget("endgame_position_distribution"),
        output_widget("endgame_points_distribution"),
        output_widget("classifier_overflow_number"),
        output_widget("shooting_depot_teleop"),
        output_widget("classifier_overflow_points"),
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

    @render_widget
    def endgame_position_distribution():
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        endgame_df = new_df.groupby("Team Number")["End Position(Endgame)"].value_counts().unstack(
            fill_value=0).reset_index()
        endgame_df["Hh Points"] = endgame_df["Hh"] * 20
        endgame_df["P Points"] = endgame_df["P"] * 5
        endgame_df["Sc Points"] = endgame_df["Sc"] * 10

        custom_colors = ["#D4A49C", "#8F6779", "#5C3028"]

        fig_endgame_position_distrib = px.bar(endgame_df, x="Team Number", y=["Hh", "P", "Sc"],
                                              title="Endgame Position Distribution by Teams",
                                              color_discrete_sequence=custom_colors)
        fig_endgame_position_distrib.update_layout(
            yaxis_title="Position"
        )
        return fig_endgame_position_distrib

    @render_widget
    def endgame_points_distribution():
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        endgame_df = new_df.groupby("Team Number")["End Position(Endgame)"].value_counts().unstack(
            fill_value=0).reset_index()
        endgame_df["Hh Points"] = endgame_df["Hh"] * 20
        endgame_df["P Points"] = endgame_df["P"] * 5
        endgame_df["Sc Points"] = endgame_df["Sc"] * 10

        custom_colors = ["#D4A49C", "#8F6779", "#5C3028"]

        fig_endgame_point_distrib = px.bar(endgame_df, x="Team Number", y=["Hh Points", "P Points", "Sc Points"],
                                           title="Endgame Point Distribution by Teams",
                                           color_discrete_sequence=custom_colors)
        fig_endgame_point_distrib.update_layout(
            yaxis_title="Points"
        )

        return fig_endgame_point_distrib


    @render_widget
    def classifier_overflow_number():
        avg_team = get_teams_in_match().groupby("Team Number").mean(numeric_only=True)
        print(avg_team.keys())
        fig = px.bar(avg_team, y=["Classifier Scored(Auto)", "Overflow Scored(Auto)"],
                     title="Classifier v. Overflow Scored (Auto)")
        return fig

    @render_widget
    def classifier_overflow_points():
        avg_team = get_teams_in_match().groupby("Team Number").mean(numeric_only=True)
        print(avg_team.keys())
        fig = px.bar(avg_team, y=["Classifier Points Scored(Auto)", "Overflow Points Scored(Auto)"],
                     title="Classifier v. Overflow Points Scored (Auto)")
        return fig


    @render_widget
    def shooting_depot_teleop():
        avg_team = get_teams_in_match().groupby("Team Number").mean(numeric_only=True)
        print(avg_team.keys())
        fig = px.scatter(avg_team, x="Depot Scored(Teleop)", y="Shooting Points Scored", text=avg_team.index,
                         title="Depot v. Shooting Scored (Teleop) per Team")
        fig.update_traces(marker=dict(
            symbol='circle', size=10),
            textposition="middle left")
        return fig