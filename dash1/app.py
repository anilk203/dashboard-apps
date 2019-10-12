from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime

server = Flask(__name__)

app = dash.Dash(name='Plotly Flask App',url_base_pathname='/dash1/',
                server=server)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Project Dashboard - A '+ str(datetime.datetime.now()),
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.'+str(datetime.datetime.now()), style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'images': [
                    {
                        'source':"light.png",
                        'xref':"paper",
                        'yref':"paper",
                        'x':1,
                        'y':1.05,
                        'sizex':0.2,
                        'sizey':0.2,
                        'xanchor':"right",
                        'yanchor':"bottom"
                }],
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
