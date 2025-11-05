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
        output_widget("team_v_total_points")
    )
@module.server
def general_match_server(input,output,session):
    @render_widget
    def team_v_total_points():
        all_teams = [3333, 6666, 11111, 4444]
        new_df = df.loc[df["Team Number"].isin(all_teams)]
        fig = px.box(new_df, x="Team Number", y="Total Points Scored")
        return fig