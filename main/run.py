#this run file will run the application with debug on to allow for development
from src import app

if __name__ == '__main__':
	app.run(debug=True)
