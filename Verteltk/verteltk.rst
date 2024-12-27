=================================
VERTELTK DATA ENTRY PROGRAM SPEC
=================================

Description
-----------
This program is a simple data entry program that allows the user to enter a prefix and get the country of origin of that prefix. The program will also suggest the country if the prefix is not found in the database.
The user must enter a prefix and a number, and the program will return the country of origin of that prefix.
If the prefix is not found in the database, the program will terminate and the user must restart the program.
Otherwise the user will see the country of origin of the prefix and the program will terminate.

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
Users must check one prefix per time, no multiple checks.

Limitations
-----------

The program must:
    * Return the correct country,
    * Give correct suggestions,
    * Be efficiently operable by keyboard-only users.

These are all the values that the program can check: 
+-----------+------------+---------+--------------------------------------------------------------------------+----------------------------+
|Field      | Type       |Unit     |Valid Values                                                              |Description                 |
+===========+============+=========+==========================================================================+============================+
|Prefisso   | Int        |         | 1-7-20-27-30-31-32-33-34-36-37-39-40-41-43-44-45-46-47-48-49-51-52-53-54 |International subscriber    |
|           |            |         | 55-56-57-58-60-61-62-63-64-65-66-81-82-84-90-91-92-93-94-95-98-210-21-212|dialing codes               |
|           |            |         | 213-214-215-216-217-218-219-220-221-222-223-224-225-226-227-228-229-230  |                            | 
|           |            |         | 231-232-233-234-235-236-237-238-239-240-241-242-243-244-245-246-247-248  |                            |
|           |            |         | 249-250-251-252-253-254-255-256-257-258-259-260-261-262-263-264-265-266  |                            |
|           |            |         | 267-268-269-270-271-272-273-274-275-276-277-278-279-280-281-282-283-284  |                            |
|           |            |         | 285-286-287-288-289-290-291-292-293-294-295-296-297-298-299-350-351-352  |                            |
|           |            |         | 353-354-355-356-357-358-359-371-372-373-374-375-376-377-378-379-380-381  |                            |
|           |            |         | 382-383-384-385-386-387-388-389-420-421-423-500-501-502-503-504-505-506  |                            |
|           |            |         | 507-508-509-590-591-592-593-594-595-596-597-598-670-671-672-673-674-675  |                            |
|           |            |         | 676-677-678-679-680-681-682-683-684-685-686-687-688-689-690-691-692-800  |                            |
|           |            |         | 808-850-852-853-855-856-870-871-872-873-874-875-876-877-878-879-880-881  |                            |
|           |            |         | 882-883-886-888-960-961-962-963-964-965-966-967-968-969-970-971-972-973  |                            |
|           |            |         | 974-975-976-977-978-979-991-992-993-994-995-996-997-998-1242-1246-1264   |                            |
|           |            |         | 1268-1284-1340-1345-1441-1473-1649-1658-1664-1670-1671-1684-1721-1758    |                            |
|           |            |         | 1767-1784-1787-1809-1829-1849-1868-1869-1876-5993-5994-5995-5997-5998    |                            |
|           |            |         | 5999-                                                                    |                            |