# Soaring Eagle

## Overview

Our project is about implementing an airline reservation website. The goals were to allow the user to choose a destination, access our calendar system, choose an airline, view pricing (including taxes and fees), input their personal information, input their payment information, and confirm their booking. Having these features gives users a clear, efficient route to place a booking. Our information inputting system allows for quick, easy access to general data and price comparison. Having an online reservation system lessens workload of staff and other services. It also reduces chances for errors whether it’s regarding availability or bookings.

## Functional Requirements

We have implemented 6 functional requirements:

1. **Choosing a destination** (Marlon/Alan)
2. **Showing a calendar** (Marlon)
3. **Choosing an airline** (Alan/Marlon)
4. **Calculating pricing** (Pawan/Mihir/Marlon)
5. **Getting passenger/payment information** (Mihir/Marlon)
6. **Confirming booking** (Pawan/Marlon)

## Installation

To install our libraries:

1. Open command terminal
2. Type `git clone https://github.com/4-gent/SoaringEagle.git`
3. Navigate to `/pathto/SoaringEagle/main/`
4. Then to install our requirements, type `pip3 install -r Requirements.txt`
5. Run `run.py` in the `/pathto/SoaringEagle/main/` directory by typing `python3 run.py`
6. To access the webpage, either copy/paste the URL provided after running the previous command in a browser or type `localhost:5000/` to access our homepage.

## Pages

Our pages included:

- Homepage
- Flight options
- Purchasing (pre-booking)
- Purchase confirmation

## Technologies Used

The technologies used include libraries. These span web frameworks, database, web forms, utilities, data visualization, and SocketIO dependencies. Their respective uses were:

- Flask-SQLAlchemy
- flask_wtf
- werkzeug/MarkupSafe/itsdangerous
- matplotlib
- Pillow
