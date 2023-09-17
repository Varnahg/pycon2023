from dash import register_page, html


import dash_mantine_components as dmc

register_page(__name__)

AboutMeText = ("Passionate Software Developer with a proven track record of designing and "
               "implementing end-to-end solutions to meet diverse customer needs. I pride "
               "myself on being a fast learner, "
               "continually striving to master new technologies."
               "Open for collaboration and opportunities where I can bring my skills and learn something new, "
               "while helping to create impactful software solutions. Let's connect!")
layout = dmc.Grid(
    style={
        "margin": "0 auto",  # This will center the grid horizontally
    },
    children=[
        dmc.Col(dmc.Text(AboutMeText), span=6),
        dmc.Col(dmc.Image(src="/assets/me.jpg", width="200px", height="200px"), span=6)
    ]
)

