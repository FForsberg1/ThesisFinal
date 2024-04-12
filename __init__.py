import os
import random

from flask import Flask

#I got this file from the flask documentation, I added things in for my project purposes
#The orginal can be found here
#https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Simple page that says hello, this is not used in the final project. I mainly used this for debugging purposes and to have an easy page to access when I start the program
    @app.route('/hello')
    def hello():
        return 'Hello, World! Welcome to the project'
    
    from . import db      #Add in the database
    db.init_app(app)

    #All the creation of the blueprints can be found in the file that is called

    from . import listData                  #Add in the blueprint for the list all the different datas 
    app.register_blueprint(listData.bp)

    from . import searchData                  #Add in the blueprint for the search all the different datas
    app.register_blueprint(searchData.bp)

    from . import addData                  #Add in the blueprint to add all the different datas
    app.register_blueprint(addData.bp)

    from . import homePipelineGraph                 #Add in the blueprint to access the home page, pipeline, and graph
    app.register_blueprint(homePipelineGraph.bp)

    return app