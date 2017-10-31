from app import app
import flask
import glob 
import os 

from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc


## serving static images 

base_dir = os.path.dirname(os.path.realpath(__file__))
static_dir = os.path.join(base_dir,'static/')
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(static_dir))]
static_image_route='/static/'

def embed_image(image_name):
	return html.Img(src = os.path.join(static_image_route,image_name))   
	
@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_image(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(static_dir, image_name)

## High level reusable html items 

## General layout of all apps

margins = {
	'top' : 20, 
	'bottom' : 50,
	'left' : 20,
	'right' : 20
	}

## Logo header for each page 
def header(title, subtitle):
	return html.Div([
		embed_image('learnt_logo.png'),
		html.H3(title),
		html.P(subtitle)],
		)

## Lists all apps in the /apps/ directory 
app_list=[os.path.basename(x) for x in glob.glob('{}[!_]*.py'.format(os.path.join(base_dir,'apps/')))]
## cut the .py suffix for printing
app_list_print=[i.strip('.py') for i in app_list]

## Nav bar for all pages  
def nav_bar(id_name,which='all'):
	if which == 'all':
		return html.Div([
					html.Div(
						html.Button(dcc.Link('HOME',href='/'),id='go_home')
						,style={'display':'inline-block','width':'9%'}),
					html.Div(
						dcc.Dropdown(
						id='{}'.format(id_name),
						options=[{'label':i,'value':i} for i in app_list_print],
						value='home'
						),style={'float':'right','display':'inline-block','width':'89%'})	
				])	




	