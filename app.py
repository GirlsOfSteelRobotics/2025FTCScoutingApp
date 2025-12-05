import pandas as pd
from shiny import App, ui

from overview_tab import overview_tab_ui, overview_tab_server

from general_match_things import general_match_ui, general_match_server
from plots_by_team import plots_by_team_server, plots_by_team_ui

app_ui = ui.page_navbar(
    ui.nav_panel("Overview", overview_tab_ui("overview")),
    ui.nav_panel("General Match Things", general_match_ui("general_match")),
    ui.nav_panel("Plots by Team", plots_by_team_ui("plots_team")),
)

def server(input, output, session):
    overview_tab_server("overview")
    general_match_server("general_match")
    plots_by_team_server("plots_team")


app = App(app_ui, server)