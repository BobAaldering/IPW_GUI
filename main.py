# Imports for 'dash':
import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px

# -------- APPLICATION STYLESHEET -------- #


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# -------- APPLICATION SETUP -------- #


app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
server_run = app.server
app.title = "Saxion - Get ready for a smart world!"

app.layout = html.Div(children=[
    html.Div(
        # Create a header for the application.
        children=[
            dcc.Location(id="url", refresh=False),
            html.Div(id="page-content"),

            html.P(children="📚", className="header-emoji"),
            html.H1(
                children="StudyCheckinator 900", className="header-title"
            ),
            html.P(
                children=[
                    html.P(
                        "Welcome to Saxion University of Applied Sciences!"
                    ),
                    html.P(
                        "- 🎒 💻 ⚙ ✏️-"
                    ),
                ],
                className="header-description",
            ),
        ],
        className="header",
    ),

    html.Div(
        children=[
            html.Div(
                id="container"
            ),
        ],
        className="wrapper",
    ),

    # Create a footer.
    html.Footer(
        children=[
            html.P(
                "©️ 2022 Saxion University of Applied Sciences (all rights reserved)"
            ),
        ],
        className="footer",
    ),
])

page_index = html.Div(
    children=[
        html.Div(
            html.P(
                "You are probably faced with a difficult choice. Choosing a new education. But this gadget is guaranteed to help you further! It asks you a number of questions, and as a result of these questions you get small projects that have to do with different courses within Saxion."
            ),
        ),

        html.Div(
            html.P(
                "So: do you want to know whether Applied Computer Science, Electrical and Electronic Engineering, Software Engineering, Mechatronics or Industrial Product Designing. Start the gadget now!"
            ),
        ),

        html.A(
            html.Button(
                "Start the gadget!",
                className="button",
            ),
            href="/page-1",
        ),
    ],
    className="menu",
)

page_1_layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    html.P(
                        "In order to introduce you to the different courses within the Saxion in a playful and informative way, you will first have to deal with a small game. You use a marble that you can send in different directions, depending on the question that is being asked. To move the marble, different buttons are given below in the picture, so it can be moved to the left or to the right. After these questions have been answered, the courses that best match the given answers will be shown. This is followed by the second phase of this tool."
                    )
                ),
                html.A(
                    html.Button(
                        "Start the little marble game!",
                        className="button",
                    ),
                    href="/page-2",
                ),
            ],
        )
    ],
    className="menu",
)

# This section contains hard coded data, normally it will be collected through our little marble game.
dataframe = pd.DataFrame({
    "Education": ["Electrical Engineering", "Applied Computer Science", "Mechatronics", "Software Engineering", "Industrial Product Design"],
    "Score (in %)": [70, 95, 60, 80, 70]
})

fig_of_data = px.bar(dataframe, x="Education", y="Score (in %)", barmode="group", color="Education", title="Best fit for education")

page_2_layout = html.Div(
    children=[
        html.P(
            "Thanks for playing the game! We now have an idea of which field of study you really like. Based on this, in the next step you will carry out a small project related to your chosen study program."
        ),

        html.Div(
            dcc.Graph(
                id="Graph_{}".format(dataframe),
                figure=fig_of_data.update_layout(title_text="Best fit for your education", title_x=0.5),
                config={"displayModeBar": False},  # Use this to configurate the top-bar from 'Dash' for each graph.
            ),
        ),

        html.P(
            "You now have a general impression of which training suits you best. In this case it is {}, to which by pressing the next button you start a small simple project that introduces you further to this training.".format("Applied Computer Science")  # You see that this is hard coded, must change in definitive version.
        ),

        html.A(
            html.Button(
                "Go to the small project for you education",
                className="button",
            ),
            href="/page-2",
        ),
    ],
    className="menu"
)


# -------- CALLBACKS -------- #


@app.callback(dash.dependencies.Output("page-1-content", "children"),
              [dash.dependencies.Input("page-1-content", "value")])
@app.callback(dash.dependencies.Output("page-2-content", "children"),
              [dash.dependencies.Input("page-2-content", "value")])
@app.callback(dash.dependencies.Output("container", "children"),
              [dash.dependencies.Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == "/page-2":
        return page_2_layout
    else:
        return page_index

# -------- APPLICATION BOILERPLATE -------- #


if __name__ == '__main__':
    app.run_server(debug=True)  # Start our server, it is from now on possible to show our website.
