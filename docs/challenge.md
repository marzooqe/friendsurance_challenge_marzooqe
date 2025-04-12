# Data Analyst Challenge

## Objective

As a data analyst, you have been presented with a simulated dataset containing three files, namely **customers.csv, transactions.csv, and exchange_rate.csv**.\
\
Your objective for this evaluation is to demonstrate your proficiency in data analysis and manipulation using Python and/or SQL.\
\
Your task involves examining the given datasets and generating actionable insights that can be used to provide recommendations to business stakeholders.\
\
The assessment will assess your ability to solve analytical problems using data modeling, as well as your proficiency in Python/SQL programming. Additionally, it's crucial that you ensure your code is well-commented and formatted to facilitate code clarity.

### Submission

* You have 4 days to complete the challenge. If you need additional time, please reach out before the deadline.
* Once you are done, please send your solution by email in a .zip file,
* Please provide instructions for how to run the code (dependencies and requirements).
* You are free to make assumptions with tasks that may not be clear.

## Tasks

### Data Modeling

* Design a relational data model to represent the given datasets.
* Explain the modeling approach taken. Is there any alternative to the model chosen(trade-offs, limitations, advantages)?
* Postgres is preferred for the database, but it is not mandatory.

### Python

* Write a python script (**avoid notebooks**) that loads the data into their respective tables
  * Ensure that data is deduplicated.
  * Add at least one python test
  * Add logging to the code to evaluate ingestion performance.
* The code should run without any modification from our side
* Provide any specific versions, dependencies, libraries, etc. that we need to run the code.

### SQL

* Which country has the highest account balance as of today?
* What is the end of the month account balance (in EUR) per country starting for the year 2022 -- Display all Months
* What is the total account balance for the last month of the data, for all countries shown in USD
* Calculate the average transaction amount (in EUR) for each country and transaction type. Show the country, transaction type, and average transaction amount in the result.

### Business Cases

Assume the following business cases below.

Criteria which can influence the presentation:

* External stakeholders logo is blue.
* The Stakeholder in question is a new partner. They want to have a general idea about the product, because they do not have a clear understanding yet.

Business Cases:

* We can see that the exchange ratio between **USD** & **Euro** is fluctuating. Visualize & compare the trend between USD and EUR from last year to this year.
* Management wants to find the different trends and patterns in regard to Age groups in Japan. Your task is to visualize give a recommendation based on the results.

**Good luck!**
