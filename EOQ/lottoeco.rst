EOQ CONTROL DATA ENTRY PROGRAM SPEC
====================================

// Description
// -----------
This program has a specific purpose: helping users find the optimal quantification of products to buy.
The program will prompt the user to enter the annual demand, the monthly setup cost and the annual holding cost.
The user must insert values equal to or greater than zero, even values with a maximum of 2 decimal places.
If the user enters a negative value, the program will ask to reinsert the value.
The program will then calculate the optimal order quantity using the EOQ formula and display the result;
It will also create an excel file with the product and the optimal order quantity.
After the calculation, the program will terminate.

// Requirements
// ------------
*** Functional requirements: ***
Allow all relevant, valid data to be entered, as per the data dictionary.
the program must show only one answer per execution and then terminate.
For the first run ever, the program creates an excel file with the product and the optimal order quantity. 
For the next runs, the program will append the new product and the optimal order quantity to the existing file.

*** Non-functional requirements: ***
Provide a smooth and efficient workflow.
Provide a correct answer for each request — no wrong answers. 
The program must be able to handle large amounts of data and perform calculations quickly.
The program must be used by a single user at a time, in order to avoid data corruption on the excel file.
The program can be used on various operating systems, including Windows, MacOS and Linux.
The program must be able to run on various versions of Python, including Python 3.6 and above.
It also requires the presence of Microsoft Excel on the user's computer.

// Functionality Not Required
// --------------------------
The program does not need to:
- Allow editing of data.
- Allow deletion of data.
Users must check **one product at a time**, no multiple checks allowed.

// Limitations
// -----------  
The program must:
- Return the correct optimal order quantity.
- Give correct suggestions.
- Be efficiently operable by keyboard-only users.
- Be able to handle large amounts of data and perform calculations quickly.
- Be used on various operating systems, including Windows, MacOS and Linux.
- Be able to run on various versions of Python, including Python 3.6 and above.
- Require the presence of Microsoft Excel on the user's computer.
- Not require any additional libraries or software to run.
- Require special permissions or access rights to run.

// Valid Inputs
// --------------
The program accepts the following inputs:
- Annual demand: a positive integer or float, with a maximum of 2 decimal places.
- Monthly setup cost: a positive integer or float, with a maximum of 2 decimal places.
- Annual holding cost: a positive integer or float, with a maximum of 2 decimal places.

// Invalid Inputs
// --------------
- The program will not accept negative values or invalid characters (non-numeric).
- The program will also not accept values with more than 2 decimal places.

// Modules
// --------
def calculate_eoq(annual_demand, monthly_setup_cost, annual_holding_cost): Calculate the Economic Order Quantity (EOQ) using the EOQ formula.
def create_excel_file(product, optimal_order_quantity): Create an Excel file with the product and the optimal order quantity.
