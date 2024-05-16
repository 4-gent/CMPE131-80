# Functional Requirements

We have implemented 6 functional requirements:

1. **Choosing a Destination** (Marlon/Alan)
2. **Showing a Calendar** (Marlon)
3. **Choosing an Airline** (Alan)
4. **Calculating Pricing** (Pawan/Mihir)
5. **Getting Passenger/Payment Information** (Mihir)
6. **Confirming Booking** (Pawan)

## Choosing a Destination (Marlon Burog)

**Pre-condition:** The user wishes to travel to another destination  
**Trigger:**  
User selects the “Leaving from” search bar (to select the departing airport/location)  
User selects the “Going to” search bar (to select the arrival airport/location)  

**Primary Sequence:**
1. User clicks on search bar
2. User types in input for Leaving From and Going To
3. User clicks “Submit” to search for airlines/flights and dates for that location  

**Primary Postconditions:** The user has selected a departure and an arrival airport.

**Alternate Sequence:**
- User presses cancel button
- Destination choosing is canceled
- Redirects back to search area for new destination choice

## Showing a Calendar (Marlon Burog)

**Pre-condition:** The user has selected the travel destination  
**Trigger:** The user selects the “Departure Date” or “Return Date” button  

**Primary Sequence (One-way only):**
1. User selects Departure Date
2. User hits submit button to confirm departure date  

**Primary Postconditions:** The traveling dates have been chosen by the user

**Alternate Sequence (Two-way return):**
1. The user selects the departure date
2. The user selects the return date
3. User hits submit button to confirm dates

## Choosing an Airline (Alan)

**Pre-condition:** The user has chosen the destination and dates to travel, user already has a registered account  
**Trigger:**  
User selects the “Search” button after selecting the desired destination and dates  
User selects the preferred airline from the given list  
User selects either “Continue as guest” or “Continue as member” button  

**Primary Sequence:**
1. User searches through the list and selects an airline
2. The user has a registered account and wishes to login (continues as a member)
3. System redirects to the login page
4. User successfully logs in
5. System redirects to the personal information page  

**Primary Postconditions:** The airline for the flight has been selected by the user

**Alternate Sequence (User decides to continue as a guest):**
- The system redirects to the personal information page

## Calculating Pricing (Pawan/Mihir)

**Pre-condition:** User has already selected airline, destination, and flight  
**Trigger:** User clicks “Proceed to pricing”  

**Primary Sequence (For the Calendar):**
- Calendar displays best budget price on the calendar for each day
- Provide options of one way or round trip flight
- If round trip, double amount posted on calendar  

**Primary Postconditions:** The final price is calculated

**Alternate Sequence (Final price):**
- The base price is selected
- Taxes and fees added to the base price

## Getting Passenger/Payment Information (Mihir)

**Pre-condition:** The user has already selected the flight from the budget calendar or regular calendar  
**Trigger:** User clicks on “Payment info”  

**Primary Sequence:**
1. User types their personal information
2. User selects payment method and card information
3. User submits their information to the “Submit” button  

**Primary Postconditions:** The form has been filled out with payment and user’s information

## Confirming Booking (Pawan)

**Pre-condition:** A ticket has been booked  
**Trigger:** Automatically redirected to the purchase confirmation page after booking a ticket  

**Primary Sequence:**
1. System redirects to purchase confirmation page
2. Itinerary is shown for the booked flight  

**Primary Postconditions:** The itinerary is displayed for the user (confirming the purchase)
