from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db

bp = Blueprint('searchData', __name__)

#Create the page and query for a specifc investor
@bp.route('/OneInvestor', methods=('GET', 'POST') )
def OneInvestor():

    #Take the info from user, query, and return search results with investors.html
    if request.method == 'POST':    
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required.'   #If entry box not filled, flash error

        if error is not None:
            flash(error)

        else:
            db = get_db()               #Query data based upon user input and return the search   
            result = db.execute(
                'SELECT * FROM investor WHERE name = ?', [name]
            ).fetchall()
            return render_template('listData/investors.html', posts=result)

    return render_template('searchData/searchInvestor.html')

#Create the page and query for a specifc investment
@bp.route('/OneInvestment', methods=('GET', 'POST') )
def OneInvestment():

     #Take the info from user, query, and return search results with investment.html
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:      #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()           #Query data based upon user input and return the search
            result = db.execute(
                'SELECT * FROM investment WHERE companyName = ?', [name]
            ).fetchall()
            return render_template('listData/investment.html', posts=result)

    return render_template('searchData/searchInvestment.html')

#Create the page and query for a specifc relationship
@bp.route('/OneRelationship', methods=('GET', 'POST') )
def OneRelationship():

     #Take the info from user, query, and return search results with irelationship.html
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required.'   

        if error is not None:               #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()               #Query data based upon user input and return the search
            result = db.execute(
                'SELECT * FROM investRelationship WHERE investorOrFundUUID = ?', [name]
            ).fetchall()
            return render_template('listData/relationship.html', posts=result)

    return render_template('searchData/searchRelationship.html')

#Create the page and query for a specifc KPI
@bp.route('/OneKPI', methods=('GET', 'POST') )
def OneKPI():

    #Take the info from user, query, and return search results with kpi.html
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required.'  

        if error is not None:           #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()               #Query data based upon user input and return the search
            result = db.execute(
                'SELECT * FROM kpi WHERE kpiUUID = ?', [name]
            ).fetchall()
            return render_template('listData/kpi.html', posts=result)

    return render_template('searchData/searchKPI.html')