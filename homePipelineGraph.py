from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db
from bokeh.embed import components
from bokeh.plotting import figure
import random

bp = Blueprint('homePipelineGraph', __name__)

#Home page, returns the home page which contains the links to all the pages
'''Basic home page, this will'''
@bp.route('/home')
def home():
    return render_template('homePipelineGraph/home.html')

#Pipeline page for investor, quries data tables and returns all where pipelineLocation = investor
@bp.route('/pipelineInvestor')
def pipelineInvestor():

    db = get_db()
    result = db.execute(
        'SELECT * FROM investor WHERE NOT pipelineLocation = ?', ['Investor']
    ).fetchall()

    return render_template('homePipelineGraph/pipelineInvestor.html', posts=result)

#Pipeline page for investment, quries data tables and returns all where pipelineLocation = investment
@bp.route('/pipelineInvestment')
def pipelineInvestment():

    db = get_db()
    result = db.execute(
        'SELECT * FROM investment WHERE NOT pipelineLocation = ?', ['Investment']
    ).fetchall()

    return render_template('homePipelineGraph/pipelineInvestment.html', posts=result)

#Pregraphing page, this sets up and then sends the user the graph
@bp.route('/graphsSetUp', methods=('GET', 'POST'))
def graphsSetUp():

    if request.method == 'POST':   #If user press graph on the UI 
        #print(True)
        dataType = request.form['dataType']
        investmentUUID = request.form['investmentUUID']
        error = None

        if error is not None:      #If entry box not filled, flash error
            flash(error)

        db = get_db()           #Get database and run SQL query 
        result = db.execute(
            'SELECT * FROM kpi WHERE investmentUUID = ?', [investmentUUID]      
        ).fetchall()

        dates = []
        data = []
        whatColumn = 0

        #Based upon the string the user entered, figure out what data they want to graph
        if dataType == 'headcount' or dataType == 'head count':
            whatColumn = 0

        elif dataType == 'epitda' or dataType == 'EPITDA':
            whatColumn = 1

        elif dataType == 'grossprofit' or dataType == 'gross profit':
            whatColumn = 2

        elif dataType == 'num locations' or dataType == 'numlocations':
            whatColumn = 3

        elif dataType == 'roi' or dataType == 'ROI':
            whatColumn = 4
        
        elif dataType == 'totalvalue' or dataType == 'total value':
            whatColumn = 5

        #Get the data the user wants to graph
        for row in result:
            data.append(row[whatColumn])
            dates.append( 'Quarter ' + str(row[6]) + ', ' + str(row[7]))
    
        # Return the components to the HTML template, and send user the graph page with the queried graph 
        return render_template(
            template_name_or_list='homePipelineGraph/graphs.html',
            data=data,
            labels=dates,
        )

    return render_template('homePipelineGraph/graphsSetUp.html')     #Return user pre-graphing page