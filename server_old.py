# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:43:39 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:43:39 2021

@author: User
"""

import flask
app = flask.Flask(__name__)

@app.route('/')
def home_page():
    return flask.render_template("index.html")
@app.route('/index.html')
def index_page():
    return flask.render_template("index.html")    
    
@app.route('/about.html')
def about_page():
    return flask.render_template("about.html")
@app.route('/components.html')
def components_page():
    return flask.render_template("components.html")
@app.route('/works.html')
def works_page():
    return flask.render_template("works.html")

@app.route('/contact.html')
def contact_page():
    return flask.render_template("contact.html")

