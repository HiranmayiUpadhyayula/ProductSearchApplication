# ProductSearchApplication
A simple Django application that takes UPC, EAN, ISBN or REFERENCEID,
makes a call to an eBay API "findItemsByProduct" and displays the Item Title, Price and related information 
from the response in a readable format.  

NOTE: More information regarding the API on the eBay Developer site (http://go.developer.ebay.com/). 
Refer to the Finding API and in particular, the findItemsByProduct call.
The documentation contains all the information to make the call.

*DISCLAIMER* 
This was tested on a LINUX based machine (Ubuntu).

Instructions:
1. Run a pip install -r requirements.txt
2. After navigating into this folder, do a python manage.py runserver 
3. Copy the url from the terminal and run it on your browser along after adding /product to the url.
4. Some test cases to verify:
  - ReferenceID = 53039031
  - UPC = 753759077600
  
