#this run file will run the application with debug on to allow for development
from src import app_obj

if __name__ == '__main__':
	app_obj.run(debug=True)
