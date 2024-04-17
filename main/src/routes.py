#import call app_obj to establish routing to flask run
from src import app_obj

#import flask libraries
from flask import send_file, render_template, request, redirect, url_for, session, flash
from flask_socketio import send
import codecs

@app_obj.route("/", methods=['GET', 'POST'])
@app_obj.route("/index.html", methods=['GET', 'POST'])
def index():
	return render_template('index.html')
