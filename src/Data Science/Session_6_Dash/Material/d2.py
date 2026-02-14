import pandas as pd 
import plotly.express as px  # Changed from 'import plotly as px'
from dash import Dash, dcc, html, Input, Output

# Load data
df = pd.read_csv(r'D:\DEPI-Projects\DEPI_AIS2_ml\AMIT\AI & Data Science\src\Data Science\Session_6_Dash\Dash.csv')

app = Dash(__name__)
app.title = "Interactive Dashboard"

# Get numerical columns
num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("Interactive Dashboard with Pie Chart"),
    html.Label("Select a value to show in the pie chart"),
    dcc.Dropdown(
        id='column-dropdown', 
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0]
    ),
    dcc.Graph(id='pie-chart')
])

@app.callback(
    Output('pie-chart', "figure"),
    Input("column-dropdown", "value")
)
def update_pie(selected_col):
    grouped = df.groupby("Area")[selected_col].sum().reset_index()
    
    fig = px.pie(
        grouped,
        names="Area", 
        values=selected_col, 
        title=f"Distribution of {selected_col} by Area",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    return fig

if __name__ == "__main__":
    app.run(debug=True)