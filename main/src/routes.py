#import call app_obj to establish routing to flask run
from src import app
from src.forms import LoginForm

#import flask libraries
from flask import send_file, render_template, request, redirect, url_for, session, flash

from src.models import db, Flight  # Import your SQLAlchemy model

@app.route("/", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

# login
@app.route("/login.html", methods=['GET', 'POST'])
def login():
	current_form = LoginForm()
	if current_form.validate_on_submit():
		flash(f'GOOD username {current_form.username.data}')
		flash(f'GOOD password {current_form.password.data}')
		return redirect('/')
	return render_template('login.html', form=current_form)

# list out flights in table
@app.route("/flights.html", methods=['GET', 'POSTz'])
def flights():
	if request.method == 'POST':
		# Create a new instance of Flights with the data from the request
		new_flight = Flight(
			# Assign values to the columns of Flights
			origin=request.form['origin'],
			destination=request.form['destination'],
			departure_time=request.form['departure_time'],
			# Add more columns and values as needed
		)

		# Add the new_flight to the session
		db.session.add(new_flight)

		# Commit the changes to the database
		db.session.commit()

		# Optionally, you can flash a success message
		flash('Flight inserted successfully!')

		# Redirect to a different route or render a template
		return redirect(url_for('index'))

	return render_template('index.html')