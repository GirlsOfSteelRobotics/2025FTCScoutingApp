import pandas as pd
import numpy as np
import plotly.express as px
from shiny import reactive, render, module
from shiny import App, ui
from shinywidgets import output_widget, render_widget
from data_container import df, match_schedule

@module.ui
def plots_by_team_ui():
    return ui.page_fluid(
        ui.layout_sidebar(
            ui.sidebar(
                ui.output_ui("team_number_combobox"),

            ),
            output_widget("total_points_v_match"),
        )
    )

@module.server
def plots_by_team_server(input, output, server):

    @render_widget
    def total_points_v_match():
        xxx = df["Team Number"] == input.team_numbers()
        quals1_data = df[xxx]
        quals1_data
        fig = px.scatter(quals1_data, x="Match Number", y="Total Points Scored", title="Total Points Scored per Match")
        return fig

    @render.ui
    def team_number_combobox():
        team_numbers = ["15206", "27153", "25912"]
        return (
            ui.input_select(
                "team_numbers",
                "Team Number:",
                choices=team_numbers
            )
        )
    # output_widget("team_v_total_points"),
    # output_widget("avg_combined_pattern_count"),
    # output_widget("endgame_position_distribution"),
    # output_widget("endgame_points_distribution"),
    # output_widget("classifier_overflow_number_auto"),
    # output_widget("shooting_depot_teleop"),
    # output_widget("classifier_overflow_points_auto"),
    # output_widget("avg_auto_pattern_count"),
    # output_widget("avg_teleop_pattern_count"),
