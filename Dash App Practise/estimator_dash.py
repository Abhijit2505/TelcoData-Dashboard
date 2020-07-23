import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from plotly.tools import mpl_to_plotly
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from lifelines import NelsonAalenFitter
import plotly.tools as tls
import chart_studio.plotly as py
from plotly.offline import iplot
from lifelines import KaplanMeierFitter



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

telco_data = pd.read_csv('telco_customer.csv')
telco_data['TotalCharges']=pd.to_numeric(telco_data['TotalCharges'],errors='coerce')
telco_data['Churn']=telco_data['Churn'].apply(lambda x: 1 if x == 'Yes' else 0 )

T = telco_data['tenure']
C = telco_data['Churn']

def pyplot(fig, ci=True, legend=True):
    # Convert mpl fig obj to plotly fig obj, resize to plotly's default
    py_fig = tls.mpl_to_plotly(fig, resize=True)

    # Send updated figure object to Plotly, show result in notebook
    return iplot(py_fig)

def NelsonAelan_dash(T,C):
    naf = NelsonAalenFitter()
    naf.fit(T, event_observed=C)
    naf.plot(title='Nelson-Aalen Estimate')
    naf.plot(ci_force_lines=True, title='Nelson-Aalen Estimate')
    py_p = plt.gcf()
    pyplot(py_p, legend=False)

def KaplanMeier_dash(T,C):
    kmf = KaplanMeierFitter()
    kmf.fit(T, event_observed=C)
    kmf.plot(title='Kaplan Meier fitter')
    kmf.plot(ci_force_lines=True, title='Kaplan Meier fitter')
    kmf1 = plt.gcf()
    pyplot(kmf1, legend=False)

NelsonAelan_dash(T,C)
KaplanMeier_dash(T,C)

app.layout = html.Div(children=[
    html.H1(children='Hello Guys, Abhijit Here'),
    html.Div(children='''
        Here are some vizualization related to Telco Churn Dataset.
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)
