=================================
luhnalgorithm DATA ENTRY PROGRAM SPEC
=================================

Description
-----------
This program checks the verify digit of a given credit card, using the Luhn Algorithm. 
The program will prompt the user to enter the credit card number, and then will return the result of the check.
Every digit in even position will be multiplied by 2, and if the result is greater than 9, the result digit will be the difference between the result and 9.
If the digit is in an odd position, the digit will be added to the sum.
The sum of all the digits will be divided by 10, and the rest will be divided by 10. If the rest and the check digit are equal, the credit card is valid.
Otherwise, the algorithm will return "Invalid" and the program will restart.

Requirements
--------------------
Functional requirements:
    * Allow all relevant, valid data to be entered, as per the data dictionary.
    * The program only shows one answer per request, after each request must terminate the program.

Non-functional requirements:
    * Provide a smooth and efficient workflow.
    * Provide a correct answer for each request, no wrong answers.

Functionality Not Required:
---------------------------

The program does not need to:
    * Allow editing of data.
    * Allow deletion of data.
Users must check one credit card at a time. If the user wants to check another credit card, they must restart the program.

Limitations
-----------

The program must:
    * Return the string "Valid" if the credit card check digit is equal to the sum of all the digits in the credit card number module 10.
    * Restart if the user enters an invalid credit card number, an invalid character (not a number) or the two digits are not equal;
    * Be efficiently operable by keyboard-only users.