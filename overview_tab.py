import pandas as pd
import numpy as np
import plotly.express as px
from shiny import reactive, render, module
from shiny import App, ui
from shinywidgets import output_widget, render_widget
from data_container import df

@module.ui
def overview_tab_ui():
    return ui.page_fluid(
        output_widget("teleop_v_auto_points"),
    )

@module.server
def overview_tab_server(input, output, server):

    @render_widget
    def teleop_v_auto_points():
        # print("Hello world")
        avg_team = df.groupby("Team Number").mean(numeric_only=True)
        x = avg_team["Auto Points Scored"]
        y = avg_team["Teleop Points Scored"]

        fig = px.scatter(x=x, y=y, text=avg_team.index, labels={'x': "Avg Points Auto", 'y': "Avg Points Teleop"},
                         title="teleop v. auto by point")
        fig.update_traces(textposition="middle left")

        return fig
