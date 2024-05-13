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
@app.route("/flights.html", methods=['GET', 'POST'])
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
	if request.method == 'GET':
		# Query the database for all Flights
		flights = Flight.query.all()
		flight = Flight.query.filter_by(id=1).first()

		# Render the template with the flights
		return render_template('flights.html', flights=flights, flight_info=flight)

	return render_template('index.html')

@app.route("/Confirmation.html", methods=['GET', 'POST'])
def confirmation():
	airfare_fee = 120.00
	baggage_fee = 10.00
	security_fee = 20.00
	TAX = .075
	calculated_tax = (airfare_fee + baggage_fee + security_fee) * TAX

	calculated_total = (airfare_fee + baggage_fee + security_fee + calculated_tax)
		
	first_name = "John"
	last_name = "Doe"
	email_address = "joe@gmail.com"

	return render_template('receipt.html', airfare=airfare_fee, baggage=baggage_fee, security=security_fee, 
						tax=calculated_tax, total=calculated_total, firstName=first_name, lastName=last_name, email=email_address)