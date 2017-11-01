from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import os 

from app import app
from app_globals import *

## this is the Flask app that we can pass to mod_wsgi 

server=app.server 

## Layout is set by callback from either the url or the dropdown selection 

app.layout = html.Div([
   	nav_bar('all_apps_dropdown'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content') 
])

home_layout = html.Div([
	html.Div([
    	header('Welcome to Learnt!','Your conceptual learning playground.'),
    	html.P('Select a concept from the list below to get started.'),
		#html.Button(id='go',
    	],
    	style = {
    		'textAlign' : 'center'
    		})
			,
		], style={
			'marginTop' : margins['top'],
			'marginBottom' : margins['bottom'],
			'marginLeft' : margins['left'],
			'marginRight' : margins['right']
			}
			)

## Delivering page based on change in dropdown or url 
@app.callback(Output('page-content', 'children'),
               [Input('all_apps_dropdown','value'),
               Input('url', 'pathname')])

def display_page(dropdown_value,url):
## maybe a way to do this by iterating through the files in the 
## apps directory?? 
	if ((dropdown_value == 'app1') | (url=='/app1')):
		from apps import app1
		return app1.layout
	if ((dropdown_value == 'app2') | (url=='/app2')):
		from apps import app2
		return app2.layout
	else:
		return home_layout
		
## Setting dropdown value based on url
@app.callback(Output('all_apps_dropdown', 'value'),
               [Input('url', 'pathname')])
def change_dropdown_value(url):
	if url is None:
		return url
	else:
		return url.strip('/')
		
## css (can only be loaded from external source at the moment) 

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True)
