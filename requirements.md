6 functional requirements implemented: 
1. Choosing a destination (Marlon/Alan) 
2. Showing a calendar (Marlon)
3. Choosing an airline (Alan)
4. Calculating pricing (Pawan/Mihir)
5. Getting passenger/payment information (Mihir)
6. Confirming booking (Pawan)

1. Choosing a Destination (Marlon Burog)
Pre-condition: The user wishes to travel to another destination
Trigger: 
User selects the “Leaving from” search bar (to select the departing airport/location)  
User selects the “Going to” search bar (to select the arrival airport/location)
Primary Sequence:
User clicks on search bar
User types in input for Leaving From and Going To
User clicks “Submit” to search for airlines/flights and dates for that location
Primary Postconditions: The user has selected a departure and an arrival airport. 
Alternate Sequence:
User presses cancel button
Destination choosing is canceled
Redirects back to search area for new destination choice

2. Showing a Calendar (Marlon Burog)
Pre-condition: The user has selected the travel destination
Trigger: The user selects the “Departure Date” or “Return Date” button
Primary Sequence (One-way only):
User selects Departure Date
User hits submit button to confirm departure date
Primary Postconditions: The traveling dates has been chosen by the user
Alternate Sequence (Two-way return):
The user selects the departure date
The user selects the return date
User hits submit button to confirm dates

3. Choosing an airline (Alan)
Pre-condition: The user has chosen the destination and dates to travel, user already has a registered account
Trigger: 
User selects the “Search” button after selecting the desired destination and dates
User selects the preferred airline from the given list
User selects either “Continue as guest” or “Continue as member” button
Primary Sequence:
User searches through the list and selects an airline
The user has a registered account and wishes to login (continues as a member)
System redirects to the login page
User successfully logs in
System redirects to the personal information page
Primary Postconditions: The airline for the flight has been selected by the user
Alternate Sequence (User decides to continue as a guest):
The system redirects to the personal information page

4. Calculating pricing (Pawan/Mihir)
Pre-condition: User has already selected airline, destination, and flight
Trigger: User clicks “Proceed to pricing”
Primary Sequence (For the Calendar):
Calendar displays best budget price on the calendar for each day
Provide options of one way or round trip flight
If round trip, double amount posted on calendar
Primary Postconditions: The final price is calculated
Alternate Sequence (Final price):
The base price is selected
Taxes and fees added to the base price

5. Getting passenger/payment information (Mihir)
Pre-condition: The user has already selected the flight from the budget calendar or regular calendar
Trigger: User clicks on “Payment info”
Primary Sequence:
User types their personal information
User selects payment method and card information
User submits their information to the “Submit” button
Primary Postconditions: The form has been filled out with payment and user’s information

6. Confirming booking (Pawan)
Pre-condition: A ticket has been booked
Trigger: Automatically redirected to the purchase confirmation page after booking a ticket
Primary Sequence:
System redirects to purchase confirmation page
Itinerary is shown for the booked flight 
Primary Postconditions: The itinerary is displayed for the user (confirming the purchase)


