#import call app_obj to establish routing to flask run
from src import app
from src.forms import LoginForm

#import flask libraries
from flask import send_file, render_template, request, redirect, url_for, session, flash
import random

from src.models import db, Flight_Booking, Flight, Passenger_Info  # Import your SQLAlchemy model

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

# booking page for the calendar dates and location input
@app.route("/booking", methods=['GET', 'POST'])
@app.route("/booking.html", methods=['GET', 'POST'])
def booking():
	if request.method == 'POST':
		form_origin = request.form.get('origin')
		form_destination = request.form.get('destination')
		form_passenger_count = request.form.get('passengers')
		form_departure = request.form.get('start-date')
		form_arrival = request.form.get('end-date')
		form_trip_type = request.form.get('trip-type')
		new_booking = Flight_Booking(
			origin = form_origin,
			destination = form_destination,
			passenger_count = form_passenger_count,
			departure = form_departure,
			arrival = form_arrival,
			trip_type = form_trip_type
		)
		# add new_booking to table in session
		db.session.add(new_booking)

		# commit the changes to the database
		db.session.commit()

		# flash a success message
		flash('Booking inserted successfully!')

		# redirect to a different route with session information
		session['booking_id'] = new_booking.id

		print(f'info: {request.form}')

		flash('Booking made successfully!')
		return redirect(url_for('flights'))
	else:
		return render_template('booking.html')
	
# booking confirmation
@app.route("/confirm", methods=['GET', 'POST'])
@app.route("/confirm.html", methods=['GET', 'POST'])
def confirm():
	booking_id = session.get('booking_id')
	booking = Flight_Booking.query.get(booking_id)
	return render_template('confirm.html', book_info=booking)

# login
@app.route("/login.html", methods=['GET', 'POST'])
def login():
	current_form = LoginForm()
	if current_form.validate_on_submit():
		flash(f'GOOD username {current_form.username.data}')
		flash(f'GOOD password {current_form.password.data}')
		return redirect('/')
	return render_template('login.html', form=current_form)

# purchasing rendering and processing
@app.route("/purchasing", methods=['GET', 'POST'])
@app.route("/purchasing.html", methods=['GET', 'POST'])
def purchasing():
	booking_id = session.get('booking_id')
	booking = Flight_Booking.query.get(booking_id)
	passenger_count = booking.passenger_count
	trip_type_string = ""

	trip_type = booking.trip_type

	if request.method == 'POST':
    	#calculate costs
		str1 = "One Way"
		str2 = "Round Trip"

		airfare_fee = 0

		if(trip_type == 1):
			airfare_fee = random.randint(120, 500)
			trip_type_string = str1
			trip_type_int = 1

		if(trip_type == 2):
			airfare_fee = random.randint(120, 500) * 2
			trip_type_string = str2
			trip_type_int = 2

		combined_airfare = airfare_fee * passenger_count
		baggage_fee = 10.00
		security_fee = 20.00
		TAX = .075
		calculated_tax = round(((combined_airfare + baggage_fee + security_fee) * TAX), 2)
		calculated_total = round((combined_airfare + baggage_fee + security_fee + calculated_tax), 2)

		#store for receipt usage
		new_purchase = Passenger_Info(
			#Personal Info
			first_name=request.form['first_name'],
			last_name=request.form['last_name'],
			email=request.form['email'],
			address=request.form['address'],

			#card info
			card_name=request.form['card_name'],
			card_number=request.form['card_number'],
			expiration_date=request.form['card_date'],
			cvv_number=request.form['card_cvv'],

			#Payment After Calculation
			airefare_cost=airfare_fee,
			baggage_cost = baggage_fee,
			security_cost = security_fee,
			tax_cost = TAX,
			total_cost = calculated_total,

			#Trip Information
			trip = trip_type_string,
			trip_int = trip_type_int,
			passengers = passenger_count 
		)
		db.session.add(new_purchase)
		db.session.commit()

		# redirect to a different route with session information
		session['purchase_id'] = new_purchase.id
		print(f'info: {request.form}')

		return redirect(url_for('confirmation'))
	else:
		booking = Flight_Booking.query.get(booking_id)
		flight_id = session.get('flight_id')
		flight = Flight.query.get(flight_id)
		airline_name = flight.airline

		trip_type = booking.trip_type
		if(trip_type == 1):
			trip_type_string = "One Way"
		if(trip_type == 2):
			trip_type_string = "Round Trip"
		return render_template('purchasing.html', trip=trip_type_string, airline=airline_name)

# list out flights in a table
@app.route("/flights", methods=['GET', 'POST'])
@app.route("/flights.html", methods=['GET', 'POST'])
def flights():
	if request.method == 'POST':
		new_flight = Flight(
			airline = request.form['airline']
		)
		db.session.add(new_flight)
		db.session.commit()

		session['flight_id'] = new_flight.id

		print(f'info: {request.form}')

		return redirect(url_for('purchasing'))
	return render_template('flights.html')

@app.route("/confirmation", methods=['GET', 'POST'])
@app.route("/confirmation.html", methods=['GET', 'POST'])
def confirmation():
	purchase_id = session.get('purchase_id')
	passenger_information = Passenger_Info.query.get(purchase_id)

	booking_id = session.get('booking_id')
	booking = Flight_Booking.query.get(booking_id)
	origin_db = booking.origin
	destination_db = booking.destination
	departure_db = booking.departure
	arrival_db = booking.arrival

	flight_id = session.get('flight_id')
	flight = Flight.query.get(flight_id)
	airline_name = flight.airline

	return render_template('receipt.html', origin=origin_db, destination=destination_db, passenger_info=passenger_information, airline=airline_name, departure_date=departure_db, arrival_date=arrival_db)