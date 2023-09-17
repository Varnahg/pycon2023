import dash_mantine_components as dmc
from dash import Dash, html

from utils import nerespoznivny_navigacny_panel

app = Dash(__name__, use_pages=True)

links = {
    "aboutme": {"label": "About Me"},
    "experience": {"label": "Experience"},
    "contracts": {"label": "Contracts"},
    "projects": {"label": "Projects"},
    "add": {"label": "add"},
}

app.layout = html.Div([
    nerespoznivny_navigacny_panel(links, logo="tabler:square-rounded-letter-v"),
    html.Div(style={"margin": "48px"}),  # corrected this line
    html.Div(id="page-content")
])

if __name__ == "__main__":
    app.run_server(debug=True)
