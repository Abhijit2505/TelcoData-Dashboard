import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

telco_data = pd.read_csv('telco_customer.csv')
telco_data['TotalCharges']=pd.to_numeric(telco_data['TotalCharges'],errors='coerce')
telco_data['Churn']=telco_data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0 )


fig1 = px.bar(telco_data,x='tenure',y='Churn',title="tenure vs churn", color_discrete_sequence =['red']*len(telco_data))
fig2 = px.bar(telco_data,x='tenure',y='TotalCharges',title="tenure vs TotalCharges", color_discrete_sequence =['blue']*len(telco_data))
fig3 = px.scatter(telco_data,x='MonthlyCharges',y='TotalCharges',title="tenure vs TotalCharges")
app.layout = html.Div(children=[
    html.H1(children='Hello Guys, Abhijit Here'),
    html.Div(children='''
        Here are some vizualization related to Telco Churn Dataset.
    '''),
    dcc.Graph(
        figure=fig1
    ),
    dcc.Graph(
    figure = fig2
    ),dcc.Graph(
    figure = fig3
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
