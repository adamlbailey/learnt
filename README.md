![alt text](https://github.com/adamlbailey/learnt/blob/master/static/learnt_logo.png)

### Learnt is a conceptual learning playground that can be found [here](http://learnt.world) .  

## Table of Contents 

[Architecture](#architecture-section)

[Deployment](#deployment-section)

<a name="architecture-section"></a>
## Architecture

learnt is built on the incredible [dash framework!](https://plot.ly/products/dash/)

### High level overview 

learnt is launched by executing the `index.py` script which can then call all other dash app instances in the `/apps/` directory. Navigation is either by url suffix or by dropdown selection in the main heading. url suffix pattern matches the name of the dash app script (sans .py suffix) in `/apps/` directory. At the moment, adding an additional dash app script to the `/appps/` directory requires hardcoding its name in `index.displaypage(dropdownvalue,url)` for the heading dropdown and url routing to respond. 

`index.py` calls `app.py` which contains initiation of the dash app object. The `app.py` script conditionally returns the plotly dash object requisite of simple html authentication or not. 

### "Global" app attributes 

The `app_globals.py` file contains several functions that can be imported into the rest of the dash app. In theory, these functions are objects or features that are intended to be used multiple times and/or on multiple pages throughout the app. Examples include the header for each page (`app_globals.nav_bar`) and a function for serving static images (`app_globals.embed_image`). 

<a name="deployment-section"></a>
## Deployment

Learnt is deployed with apache2 and mod_wsgi in a virtual environment 

As dash is built on the Flask framework, this guide was invaluable in initiating a hello world example: https://www.jakowicz.com/flask-apache-wsgi/

Once that was working as described, the following changes were made so apache served the dash app instead of the flask app used in the example:

Add this to the .wsgi script to activate the virtual environment and thus expose the dependencies:

```
activate_this = '/var/www/learnt/learnt/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(),dict(__file__=activate_this))
```
  
With the dash app itself, in this case `index.py`, I exposed the Flask server with this line `server = app.server` then imported that in the .wsgi script as 'application' which is the name of the object mod_wsgi is expecting.

Some more useful sources I'll leave here: 

* dash official docs on deployment: https://plot.ly/dash/deployment

* flask docs on implementing mod_wsgi: http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/

  









