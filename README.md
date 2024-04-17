To run this program the user must have a flask installed. Jinja will download with Flask. As well as have the files in the correct format with the subfolders set up correctly. Refer to the file directory layout section for more information. Flask will run in a virtual environment and require python3 to run, if python3 needs to be installed refer to the python3 documentation. The windows commands I run to set up the project are as follows. If you do not use windows, refer to the correct linux or mac commands: 

> mkdir myproject
	This will create a new project folder, this is where all files should be placed inot
> cd myproject
> py -3 -m venv .venv
	Create a new virtual environment for this project, after this step is completed add the files into the folder 
> .venv\Scripts\activate
$ pip install Flask
	This should run for a sec as pip installs all the files 
$ flask --app flaskr init-db
Initialized the database. Should be the output for this line
$ flask --app flaskr run --debug
	Now open a new tab and go to http://127.0.0.1:5000/home this will bring up the project. If another program is using this port refer to the flask documentation https://flask.palletsprojects.com/en/3.0.x/server/#address-already-in-use

searchInvestor.html
searchKPI.html
searchRelationship.html
Base.html
