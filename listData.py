from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db

bp = Blueprint('listData', __name__)

#Create the page and query for all Investors
@bp.route('/allInvestor')
def allInvestor():

    db = get_db()
    result = db.execute(
        'SELECT * FROM investor WHERE pipelineLocation = ?', ['Investor']
    ).fetchall()

    return render_template('listData/investors.html', posts=result)

#Create the page and query for all investment
@bp.route('/allInvestment')
def allInvestment():

    db = get_db()
    resultInvestment =  db.execute(
        'SELECT * FROM investment WHERE pipelineLocation = ?', ['Investment']
    ).fetchall() 

    return render_template('listData/investment.html', posts=resultInvestment)

#Create the page and query for all relatinships 
@bp.route('/allRelationship')
def allRelationship():

    db = get_db()
    resultRelationship =  db.execute(
       'SELECT * FROM investRelationship'
    ).fetchall() 

    return render_template('listData/relationship.html', posts=resultRelationship)

#Create the page and query for all KPI
@bp.route('/allKPI')
def allKPI():

    db = get_db()
    resultKPI =  db.execute(
        'SELECT * FROM kpi'
    ).fetchall() 

    return render_template('listData/kpi.html', posts=resultKPI)