import dash


## Set whether authentication is required here
authenticate = False 

if authenticate:
	import dash_auth
	cred_pairs=[
	['datapotential','test']
	]
	app = dash.Dash('auth')
	auth=dash_auth.BasicAuth(
		app,
		cred_pairs)
else:
	app = dash.Dash()

server = app.server
app.config.supress_callback_exceptions = True
