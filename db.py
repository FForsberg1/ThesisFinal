import sqlite3

import click
from flask import current_app, g

#I got this file from the flask documentation, I added things in for my project purposes
#The orginal can be found here
#https://flask.palletsprojects.com/en/3.0.x/tutorial/database/


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row       #Return as a row object, iterate through to acess contnet of tables       

    return g.db

#checks if a connection was created by checking if g.db was set. If the connection exists, it is closed. 
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

#Create the database and run the sql code so that I create a sql file
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:       #Where I am getting the db, change this if the sql file is not called schema.sql
        db.executescript(f.read().decode('utf8'))

#Method to reset the database, use through command line
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)