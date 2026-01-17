from dash import Dash, html, dcc
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
                html.Button("Submit", id= "numbers"),
                dcc.Input(placeholder="Enter a valid number",
                          id= "Data",
                          type="number"),
                html.H1(id="Results")])


@app.callback(Output("Results","childern"),
              Input("numbers","n_clicks"))

def data_play(n,data):
    if n:
        return f"You Enter: {data}"

app.run(debug= True)