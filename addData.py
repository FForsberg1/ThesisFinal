from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db

bp = Blueprint('addData', __name__)

#Add a new Investor to the database
@bp.route('/addInvestor', methods=('GET', 'POST') )
def addInvestor():

    #Get data from user, add to datatable
    if request.method == 'POST':
        currentTotalCash = request.form['currentTotalCash']
        totalCashInvested = request.form['totalCashInvested']
        name = request.form['name']
        email = request.form['email']
        thesis = request.form['thesis']
        uuid = request.form['uuid']
        pipelineLocation = request.form['pipelineLocation']
        error = None

        if error is not None:       #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()           #Insert new value into database
            db.execute(
                'INSERT INTO investor ('
                'currentTotalCash,'
                'totalCashInvested,' 
                'name,'
                'email,' 
                'thesis,' 
                'uuid,' 
                'pipelineLocation) VALUES (?,?,?,?,?,?,?)',
                (currentTotalCash,totalCashInvested,name,email,thesis,uuid,pipelineLocation)
            )
            db.commit()

            result = db.execute(            #Get all investors so we can see that it was added
                'SELECT * FROM investor'
            ).fetchall()
            return render_template('listData/investors.html', posts=result)


    return render_template('addData/addInvestor.html')


#Add a new investment to the database
@bp.route('/addInvestment', methods=('GET', 'POST') )
def addInvestment():

    #Query data based upon user input and return the search
    if request.method == 'POST':
        companyName = request.form['companyName']
        companyEmail = request.form['companyEmail']
        website = request.form['website']
        contactName = request.form['contactName']
        bio = request.form['bio']
        dateJoinNetwork = request.form['dateJoinNetwork']
        percentCompanyOwned = request.form['percentCompanyOwned']
        uuid = request.form['uuid']
        pipelineLocation = request.form['pipelineLocation']
        error = None

        if error is not None:       #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()       #Insert new value into database
            db.execute(
                'INSERT INTO investment ('
                'companyName,'
                'companyEmail,' 
                'website,'
                'contactName,' 
                'bio,' 
                'dateJoinNetwork,' 
                'percentCompanyOwned,'
                'uuid,'
                'pipelineLocation) VALUES (?,?,?,?,?,?,?,?,?)',
                (companyName,companyEmail,website,contactName,bio,dateJoinNetwork,percentCompanyOwned,uuid,pipelineLocation)
            )
            db.commit()

            result = db.execute(                 #Get all investment so we can see that it was added
                'SELECT * FROM investment'
            ).fetchall()
            return render_template('listData/investment.html', posts=result)


    return render_template('addData/addInvestment.html')


#Add a new KPI to the database
@bp.route('/addKPI', methods=('GET', 'POST') )
def addKPI():

    #Query data based upon user input and return the search
    if request.method == 'POST':
        headcount = request.form['headcount']
        epitda = request.form['epitda']
        grossProfit = request.form['grossProfit']
        numLocations = request.form['numLocations']
        roi = request.form['roi']
        totalValueOfCompany = request.form['totalValueOfCompany']
        quarter = request.form['quarter']
        year = request.form['year']
        kpiUUID = request.form['kpiUUID']
        investmentUUID = request.form['investmentUUID']
        error = None

        if error is not None:       #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()            #Insert new value into database
            db.execute(
                'INSERT INTO kpi ('
                'headcount,'
                'epitda,' 
                'grossProfit,'
                'numLocations,' 
                'roi,' 
                'totalValueOfCompany,' 
                'quarter,'
                'year,'
                'kpiUUID,'
                'investmentUUID) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (headcount,epitda,grossProfit,numLocations,roi,totalValueOfCompany,quarter,year,kpiUUID,investmentUUID)
            )
            db.commit()

            result = db.execute(             #Get all KPI so we can see that it was added
                'SELECT * FROM kpi'
            ).fetchall()
            return render_template('listData/kpi.html', posts=result)


    return render_template('addData/addKPI.html')


#Add anew Relationship
@bp.route('/addRelationship', methods=('GET', 'POST') )
def addRelationship():

    #Query data based upon user input and return the search
    if request.method == 'POST':
        investmentAmount = request.form['investmentAmount']
        investmentDate = request.form['investmentDate']
        percentOfCompany = request.form['percentOfCompany']
        investorOrFundUUID = request.form['investorOrFundUUID']
        investmentUUID = request.form['investmentUUID']
        error = None

        if error is not None:       #If entry box not filled, flash error
            flash(error)

        else:
            db = get_db()        #Insert new value into database
            db.execute(
                'INSERT INTO investRelationship ('
                'investmentAmount,'
                'investmentDate,' 
                'percentOfCompany,'
                'investorOrFundUUID,' 
                'investmentUUID) VALUES (?,?,?,?,?)',
                (investmentAmount,investmentDate,percentOfCompany,investorOrFundUUID,investmentUUID)
            )
            db.commit()

            result = db.execute(                         #Get all relationship so we can see that it was added
                'SELECT * FROM investRelationship'
            ).fetchall()
            return render_template('listData/relationship.html', posts=result)


    return render_template('addData/addRelationship.html')