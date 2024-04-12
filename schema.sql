DROP TABLE IF EXISTS investment;
DROP TABLE IF EXISTS investor;
DROP TABLE IF EXISTS investRelationship;
DROP TABLE IF EXISTS kpi;

CREATE TABLE IF NOT EXISTS investment (
    companyName TEXT, 
    companyEmail TEXT, 
    website TEXT, 
    contactName TEXT, 
    bio TEXT, 
    dateJoinNetwork TEXT, 
    percentCompanyOwned FLOAT, 
    uuid TEXT PRIMARY KEY, 
    pipelineLocation TEXT);

CREATE TABLE IF NOT EXISTS investor (
    currentTotalCash FLOAT, 
    totalCashInvested FLOAT, 
    name TEXT, 
    email TEXT, 
    thesis TEXT, 
    uuid TEXT PRIMARY KEY, 
    pipelineLocation TEXT);

CREATE TABLE IF NOT EXISTS investRelationship (
    investmentAmount FLOAT, 
    investmentDate TEXT,
    percentOfCompany FLOAT, 
    investorOrFundUUID TEXT, 
    investmentUUID TEXT);

CREATE TABLE IF NOT EXISTS kpi (
    headcount INTEGER, 
    epitda FLOAT, 
    grossProfit FLOAT, 
    numLocations INTEGER, 
    roi FLOAT, 
    totalValueOfCompany FLOAT, 
    quarter INTEGER, 
    year INTEGER, 
    kpiUUID TEXT, 
    investmentUUID TEXT);


INSERT INTO investor (
  currentTotalCash, 
  totalCashInvested, 
  name, 
  email, 
  thesis, 
  uuid, 
  pipelineLocation) VALUES (
    '1350',
    '10500',
    'Fund',
    'Fund@mail.com',
    'This is the fund entity we run the investment network',
    '0',
    'Investor');

INSERT INTO investor (
  currentTotalCash, 
  totalCashInvested, 
  name, 
  email, 
  thesis, 
  uuid, 
  pipelineLocation) VALUES (
    '150',
    '1000',
    'Grace',
    'Grace@mail.com',
    'Red Pandas',
    '1',
    'Investor');

INSERT INTO investor (
  currentTotalCash, 
  totalCashInvested, 
  name, 
  email, 
  thesis, 
  uuid, 
  pipelineLocation) VALUES (
    '333',
    '0',
    'Fremont',
    'Fremont@mail.com',
    'I am a broke college student you think I have money to invest?',
    '2',
    'Lead');

INSERT INTO investor (
  currentTotalCash, 
  totalCashInvested, 
  name, 
  email, 
  thesis, 
  uuid, 
  pipelineLocation) VALUES (
    '23.67',
    '0.45',
    'Cory',
    'Cory@mail.com',
    'I want to invest in companies that have Machine learning',
    '3',
    'Warm Lead');

INSERT INTO investor (
  currentTotalCash, 
  totalCashInvested, 
  name, 
  email, 
  thesis, 
  uuid, 
  pipelineLocation) VALUES (
    '0',
    '100',
    'Blake',
    'Blake@mail.com',
    'ROBOTS',
    '4',
    'Invested');

INSERT INTO investor (
  currentTotalCash, 
  totalCashInvested, 
  name, 
  email, 
  thesis, 
  uuid, 
  pipelineLocation) VALUES (
    '0',
    '0',
    'Antartica',
    'AntarticaICE@mail.com',
    'Ice',
    '5',
    'No Interest');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'Groove Capital',
    'Groove@mail.com',
    'www.GrooveCapital.com',
    'Groove',
    'Angel Investing Company',
    '11/30/2023',
    '0.2',
    '100',
    'Investment');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'Colorado College',
    'CC@mail.com',
    'www.ColoradoCollege.com',
    'L. Song Richardson',
    'Liberal Arts College located in Colorado Springs',
    '1/1/1874',
    '1.0',
    '101',
    'Investment');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'In-and-Out',
    'In-and-Out@mail.com',
    'www.In-and-Out.com',
    'John Smith',
    'Fast Food',
    '12/10/2023',
    '0',
    '102',
    'Lead');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'Rasta Pasta',
    'Rasta Pasta@mail.com',
    'www.RastaPasta.com',
    'Jane Doe',
    'Resturant',
    '12/10/2023',
    '0',
    '103',
    'Warm Lead');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'Azada',
    'Azada@mail.com',
    'www.Azada.com',
    'Leo McClendon',
    'Resturant',
    '12/10/2023',
    '0',
    '104',
    'Assigned Rep');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'NPR',
    'NPR@mail.com',
    'www.NPR.com',
    'Sally Ellzey',
    'News station',
    '12/10/2023',
    '0',
    '105',
    'Applied');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'The New York Times',
    'NewYorkTimes@mail.com',
    'www.NewYorkTimes.com',
    'Pamela Goss',
    'News Paper',
    '12/10/2023',
    '0',
    '106',
    'Rejected');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'Bath and Body works',
    'BathBody@mail.com',
    'www.BathBody.com',
    'Denise Bohn',
    'Body Care',
    '12/10/2023',
    '0',
    '107',
    'Accepted');

INSERT INTO investment (
    companyName, 
    companyEmail, 
    website, 
    contactName, 
    bio, 
    dateJoinNetwork, 
    percentCompanyOwned, 
    uuid, 
    pipelineLocation) VALUES (
    'Sperry',
    'Sperry@mail.com',
    'www.Sperry.com',
    'Will Miller',
    'Shoe Company',
    '12/10/2023',
    '0',
    '108',
    'Invested');

INSERT INTO investRelationship (
    investmentAmount, 
    investmentDate,
    percentOfCompany, 
    investorOrFundUUID, 
    investmentUUID) VALUES (
      '5500',
      '12/6/2023',
      '0.2',
      '0',
      '100'
    );


INSERT INTO investRelationship (
    investmentAmount, 
    investmentDate,
    percentOfCompany, 
    investorOrFundUUID, 
    investmentUUID) VALUES (
      '2500',
      '12/6/2023',
      '0.5',
      '0',
      '101'
    );

INSERT INTO investRelationship (
    investmentAmount, 
    investmentDate,
    percentOfCompany, 
    investorOrFundUUID, 
    investmentUUID) VALUES (
      '2500',
      '12/10/2023',
      '0.5',
      '0',
      '101'
    );

INSERT INTO investRelationship (
    investmentAmount, 
    investmentDate,
    percentOfCompany, 
    investorOrFundUUID, 
    investmentUUID) VALUES (
      '2500',
      '12/10/2023',
      '0.5',
      '1',
      '100'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '87',
      '123.456',
      '7',
      '15',
      '1.1',
      '3500',
      '4',
      '2023',
      '1000',
      '100'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '87',
      '140.5',
      '7',
      '15',
      '1.2',
      '3505',
      '1',
      '2024',
      '1001',
      '100'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '87',
      '139',
      '8',
      '15',
      '1.2',
      '3503',
      '2',
      '2024',
      '1002',
      '100'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '88',
      '145',
      '10',
      '14',
      '1.0',
      '3000',
      '3',
      '2024',
      '1003',
      '100'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '4',
      '-40',
      '20',
      '1',
      '-3',
      '23',
      '4',
      '2023',
      '1010',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '5',
      '-30',
      '20',
      '1',
      '-2',
      '23',
      '1',
      '2024',
      '1011',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '5',
      '0',
      '22',
      '2',
      '0',
      '23',
      '2',
      '2024',
      '1012',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '6',
      '10',
      '23',
      '3',
      '-1',
      '24',
      '3',
      '2024',
      '1013',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '7',
      '20',
      '23',
      '4',
      '-1.5',
      '25',
      '4',
      '2024',
      '1014',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '8',
      '35',
      '24',
      '5',
      '-1',
      '26',
      '1',
      '2025',
      '1015',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '9',
      '40',
      '24',
      '6',
      '0',
      '26',
      '2',
      '2025',
      '1016',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '10',
      '45',
      '25',
      '7',
      '0',
      '27',
      '3',
      '2025',
      '1017',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '11',
      '50',
      '25',
      '8',
      '0.5',
      '27',
      '4',
      '2025',
      '1018',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '12',
      '55',
      '26',
      '9',
      '1',
      '28',
      '1',
      '2026',
      '1019',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '13',
      '60',
      '26',
      '9',
      '0.5',
      '29',
      '2',
      '2026',
      '10110',
      '101'
    );

INSERT INTO kpi (
    headcount, 
    epitda,
    grossProfit, 
    numLocations, 
    roi, 
    totalValueOfCompany, 
    quarter, 
    year, 
    kpiUUID, 
    investmentUUID) VALUES (
      '14',
      '65',
      '27',
      '10',
      '1',
      '30',
      '3',
      '2026',
      '10111',
      '101'
    );