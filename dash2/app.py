from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime

from db import DatabaseConfigurationRepository 
dcr = DatabaseConfigurationRepository() 


server = Flask(__name__)

app = dash.Dash(name='Plotly Flask App',url_base_pathname='/dash2/',
                server=server)

# all configurations
db_configs = dcr.get()
# get object by configuration key
db_config = dcr.find('test1')

server.logger.error(db_config) 
if db_config != None:
    server.logger.error(db_config['value'])

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Project Dashboard - B '+ str(datetime.datetime.now()),
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
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montral'},
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
    gunicorn_logger = logging.getLogger('gunicorn.error')
    server.logger.handlers = gunicorn_logger.handlers
    server.logger.setLevel(gunicorn_logger.level)    
    app.run_server(debug=True)
