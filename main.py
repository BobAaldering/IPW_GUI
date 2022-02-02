# Information:
# For every eduction within Saxion, you can also do various small projects after the initial questions.
# The projects for every education are:
# * Applied Computer Science: small programming exercise in C++ (simple 'hello world' program - think about some IDE within an HTML frame).
# * Electrical Electronic Engineering: design a small PCB (deployment within an HTML frame - think about some kind of game).
# * Mechatronics: implement a robot with C++ (deployment within an HTML frame - think about some kind of game).
# * Industrial Product Design: design a simple case for a Raspberry Pi (deployment within an HTML frame - thing about some kind of game).
# Python is used for creating this webpages, due to the powerful aspects this programming language has.


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
        html.H1(
            "🏠 Home 🏠"
        ),

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
        html.H1(
            "🔴 Initial choice of your study 🔴!"
        ),

        html.P(
            "In order to generate a better choice, we would like to know which study program you are interested in. This allows you to make a choice in the menu below, to continue next."
        ),

        html.Div(
            children=[
                html.Div(
                    id="Initial study choice:",
                    className="menu-title",
                ),

                dcc.Dropdown(
                    id="initial_high_school_filter",  # This identification can be used within a callback function (see 'CALLBACK_SECTION' within this script).
                    options=[
                        # All the values, the second one within this pair is used for recognition.
                        {"label": "Applied Computer Science", "value": "ACS_SAX"},
                        {"label": "Electrical Electronic Engineering", "value": "EEE_SAX"},
                        {"label": "Mechatronics", "value": "MT_SAX"},
                        {"label": "Software Engineering", "value": "ICT_SAX"},
                        {"label": "Industrial Product Design", "value": "IPO_SAX"}
                    ],
                    placeholder="Select education...",
                    clearable=False,
                    className="dropdown",
                ),
            ],
        ),

        html.P(
            id="dropdown_high_school_text_notification",
            className="user_text_notify",
        ),

        html.A(
            html.Button(
                    "Continue",
                    id="dropdown_high_school_notification",
                    className="button",
                ),
            href="/page-2",
        ),
    ],
    className="menu",
)

page_2_layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    "ℹ️️ Explanation of the game you'll play ℹ️!"
                ),

                html.Div(
                    html.P(
                        "In order to introduce you to the different courses within the Saxion in a playful and informative way, you will first have to deal with a small game. You use a marble that you can send in different directions, depending on the question that is being asked. To move the marble, different buttons are given below in the picture, so it can be moved to the left or to the right. After these questions have been answered, the courses that best match the given answers will be shown. This is followed by the second phase of this tool."
                    )
                ),
                html.A(
                    html.Button(
                        "Continue",
                        className="button",
                    ),
                    href="/page-3",
                ),
            ],
        )
    ],
    className="menu",
)

page_3_layout = html.Div(
    children=[
        html.H1(
            "🎮 Let's play the marble game 🎮!"
        ),

        html.Img(
            src=app.get_asset_url("MARBLE_GAME_IMG.png"),
            width="700",
            height="600",
        ),

        html.Div(
            children=[
                html.A(
                    html.Button(
                        "Stop the game",
                        className="button",
                    ),
                    href="/page-index",
                ),
                html.A(
                    html.Button(
                        "Continue",
                        className="button",
                    ),
                    href="/page-4"
                ),
            ],
        ),
    ],
    className="menu",
)

# This section contains hard coded data, normally it will be collected through our little marble game.
dataframe = pd.DataFrame({
    "Education": ["Electrical Engineering", "Applied Computer Science", "Mechatronics", "Software Engineering", "Industrial Product Design"],
    "Score (in %)": [70, 95, 60, 80, 70]
})

fig_of_data = px.bar(dataframe, x="Education", y="Score (in %)", barmode="group", color="Education", title="Best fit for education")

page_4_layout = html.Div(
    children=[
        html.H1(
            "📊 Result of the little marble game 📊!"
        ),

        html.P(
            "Thanks for playing the game! We now have an idea of which field of study you really like. Based on this, in the next step you will carry out a small project related to your chosen study program."
        ),

        html.Div(
            dcc.Graph(
                id="Graph_{}".format(dataframe),
                figure=fig_of_data.update_layout(title_text="Best fit for your education", title_x=0.5),
                config={"displayModeBar": False, "responsive": False},
                # Use this to configurate the top-bar from 'Dash' for each graph.
            ),
        ),

        html.P(
            "You now have a general impression of which training suits you best. In this case it is {}, to which by pressing the next button you start a small simple project that introduces you further to this training.".format("Applied Computer Science")  # You see that this is hard coded, must change in definitive version.
        ),

        html.A(
            html.Button(
                "Continue",
                className="button",
            ),
            href="/page-5",
        ),
    ],
    className="menu"
)

# ACS (introduction)
page_9_layout = html.Div(
    children=[
        html.H1(
            "ℹ️ Explanation for the project (Applied Computer Science) ℹ️!"
        ),

        html.P(
            "Everyone should start programming at some point. For this reason, the C++ programming language is often used at Saxion University of Applied Sciences, because it is applied to many embedded systems. For this reason, you are going to make a small computer program that every programmer at Saxion will start with! Your job is to say 'Hello Saxion!' on the computer screen."
        ),

        html.P(
            "To run your program, press the 'Run' button on the next screen. You will then see the result of the program. If it doesn't work right away, don't worry! Modify the program until it runs."
        ),

        html.A(
            html.Button(
                "Start the small project",
                className="button",
            ),
            href="/page-6",
        ),
    ],
    className="menu",
)

# Game ACS
page_10_layout = html.Div(
    html.Div(
        children=[
            html.H1(
                "Project Applied Computer Science"
            ),

            html.P(
                "It looks like you want to learn more about what Applied Computer Science has to offer. Here you are now dealing with a simple project that delves further into the topic.",
            ),

            html.Div(
                children=[
                    html.A(
                        html.Button(
                            "Run",
                            id="run_program_button",
                            className="code_run_button",
                            n_clicks=0,
                        ),
                    ),

                    html.Div(
                        children=[
                            dcc.Textarea(
                                id="input_box_coding",
                                value="#include <iostream>\n\nint main() {\n\t// Add some code here! Remove the '//' to put your code there.\n\treturn 0;\n}",  # The initial value for the small project.
                                className="code_input_box",
                            ),

                            html.P(
                                id="input_coding_text_area",
                                className="user_text_notify",
                            ),

                            html.P(
                                "Do you have any questions? Don't worry! You can ask them within the 'IntoSaxion' environment to real students for this education. How nice is that!"
                            ),
                        ],
                    ),
                ],
            ),

            html.A(
                html.Button(
                    "To other project",
                    className="button",
                ),
                href="/page-index",
            ),
        ],
    ),
    className="menu",
)


# -------- CALLBACKS -------- #


@app.callback(dash.dependencies.Output("page-1-content", "children"),
              [dash.dependencies.Input("page-1-content", "value")])
@app.callback(dash.dependencies.Output("page-2-content", "children"),
              [dash.dependencies.Input("page-2-content", "value")])
@app.callback(dash.dependencies.Output("page-3-content", "children"),
              [dash.dependencies.Input("page-3-content", "value")])
@app.callback(dash.dependencies.Output("page-4-content", "children"),
              [dash.dependencies.Input("page-4-content", "value")])
@app.callback(dash.dependencies.Output("page-5-content", "children"),
              [dash.dependencies.Input("page-5-content", "value")])
@app.callback(dash.dependencies.Output("page-6-content", "children"),
              [dash.dependencies.Input("page-6-content", "value")])
@app.callback(dash.dependencies.Output("page-7-content", "children"),
              [dash.dependencies.Input("page-7-content", "value")])
@app.callback(dash.dependencies.Output("page-8-content", "children"),
              [dash.dependencies.Input("page-8-content", "value")])
@app.callback(dash.dependencies.Output("page-9-content", "children"),
              [dash.dependencies.Input("page-9-content", "value")])
@app.callback(dash.dependencies.Output("page-10-content", "children"),
              [dash.dependencies.Input("page-10-content", "value")])
@app.callback(dash.dependencies.Output("page-11-content", "children"),
              [dash.dependencies.Input("page-11-content", "value")])
@app.callback(dash.dependencies.Output("page-12-content", "children"),
              [dash.dependencies.Input("page-12-content", "value")])
@app.callback(dash.dependencies.Output("page-13-content", "children"),
              [dash.dependencies.Input("page-13-content", "value")])
@app.callback(dash.dependencies.Output("page-14-content", "children"),
              [dash.dependencies.Input("page-14-content", "value")])
@app.callback(dash.dependencies.Output("page-15-content", "children"),
              [dash.dependencies.Input("page-15-content", "value")])
@app.callback(dash.dependencies.Output("page-16-content", "children"),
              [dash.dependencies.Input("page-16-content", "value")])
@app.callback(dash.dependencies.Output("page-17-content", "children"),
              [dash.dependencies.Input("page-17-content", "value")])
@app.callback(dash.dependencies.Output("page-18-content", "children"),
              [dash.dependencies.Input("page-18-content", "value")])
@app.callback(dash.dependencies.Output("container", "children"),
              [dash.dependencies.Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == "/page-2":
        return page_2_layout
    elif pathname == "/page-3":
        return page_3_layout
    elif pathname == "/page-4":
        return page_4_layout
    elif pathname == "/page-5":
        return page_5_layout
    elif pathname == "/page-6":
        return page_6_layout
    elif pathname == "/page-7":
        return page_7_layout
    elif pathname == "/page-8":
        return page_8_layout
    elif pathname == "/page-9":
        return page_9_layout
    elif pathname == "/page-10":
        return page_10_layout
    elif pathname == "/page-11":
        return page_11_layout
    elif pathname == "/page-12":
        return page_12_layout
    elif pathname == "/page-13":
        return page_13_layout
    elif pathname == "/page-14":
        return page_14_layout
    elif pathname == "/page-15":
        return page_15_layout
    elif pathname == "/page-16":
        return page_16_layout
    elif pathname == "/page-17":
        return page_17_layout
    elif pathname == "/page-18":
        return page_18_layout
    else:
        return page_index


@app.callback(dash.dependencies.Output("dropdown_notification", "disabled"),
              [dash.dependencies.Input("initial_study_filter", "value")])
def notify_user_saxion_education_dropdown(value):
    if value is None:
        return True
    else:
        return False


@app.callback(dash.dependencies.Output("dropdown_high_school_notification", "disabled"),
              [dash.dependencies.Input("initial_high_school_filter", "value")])
def notify_user_high_school_dropdown(value):
    if value is None:
        return True
    else:
        return False


@app.callback(dash.dependencies.Output("dropdown_high_school_text_notification", "children"),
              [dash.dependencies.Input("initial_high_school_filter", "value")])
def notify_user_dropdown(value):
    match value:
        case "HAVO_SAX":
            return "Your choice: {}.".format("HAVO")
        case "VWO_SAX":
            return "Your choice: {}.".format("VWO")
        case "MBO_SAX":
            return "Your choice: {}.".format("MBO")
        case _:
            return "No choice made! Button disabled, please select an education."


@app.callback(dash.dependencies.Output("dropdown_text_notification", "children"),
              [dash.dependencies.Input("initial_study_filter", "value")])
def notify_user_dropdown(value):
    match value:
        case "ACS_SAX":
            return "Programmable choice! Your choice: {}.".format("Applied Computer Science")  # Best education, and the most interesting in the world! :-)
        case "EEE_SAX":
            return "Electrical choice! Your choice: {}.".format("Electrical Electronic Engineering")
        case "MT_SAX":
            return "Let's go mechatronics! Your choice: {}.".format("Mechatronics")
        case "ICT_SAX":
            return "Software is your thing! Your choice: {}.".format("Software Engineering")
        case "IPO_SAX":
            return "Let's design something! Your choice: {}.".format("Industrial Product Design")
        case "NONE_SAX":
            return "Let's go for some more questions! ".format("No preference")
        case _:
            return "No choice made! Button disabled, please select an education."


@app.callback(dash.dependencies.Output("input_coding_text_area", "children"),
              [dash.dependencies.Input("input_box_coding", "value"),
               dash.dependencies.Input("run_program_button", "n_clicks")])
def validate_code(value, n_clicks):
    # Check for button presses, will be greater than one after a click. Could be improved, but just as a prototype (compare strings).
    if n_clicks >= 1:
        if "std::cout << \"Hello, Saxion!\" << std::endl;" in value:
            return "Good job 🥳! Output of your program: \"Hello, Saxion!\""
        elif "std::cout" in value:
            return "Almost there! Compilation error: std::cout <-- missing argument."
        elif "std::cout << \"\"" in value:
            return "Almost there! Compilation error: std::cout <-- missing ';' at the end of the line."
        elif "std::cout << \"\" << std::endl;" in value:
            return "Almost there! Compilation error: std::cout << \"\" << std::endl; <-- missing message within 'std::cout'"
        else:
            return "There are some compilation errors 😕! Try again!"
    else:
        return "Let's go coding! Enter your code within this little IDE (Integrated Developers Environment, a tool that programmers always use)."


@app.callback(dash.dependencies.Output("input_coding_text_area_software_engineering", "children"),
              [dash.dependencies.Input("input_box_coding_software_engineering", "value"),
               dash.dependencies.Input("run_program_button_software_engineering", "n_clicks")])
def validate_code(value, n_clicks):
    # Check for button presses, will be greater than one after a click. Could be improved, but just as a prototype (compare strings).
    if n_clicks >= 1:
        if "print(\"Hello, Saxion!\")" in value:
            return "Good job 🥳! Output of your program: \"Hello, Saxion!\""
        elif "print" in value:
            return "Almost there! Compilation error: print <-- missing argument."
        elif "print(\"\")" in value:
            return "Almost there! Compilation error: print <-- missing the message"
        else:
            return "There are some compilation errors 😕! Try again!"
    else:
        return "Let's go coding! Enter your code within this little IDE (Integrated Developers Environment, a tool that programmers always use)."


# -------- APPLICATION BOILERPLATE -------- #


if __name__ == '__main__':
    app.run_server(debug=False)  # Start our server, it is from now on possible to show our website.
