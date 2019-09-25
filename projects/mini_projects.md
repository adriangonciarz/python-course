### Project 1 - API communication
1. Create new file `api_project.py`
1. Install and import library `requests`
1. Access the resources under provided endpoint
1. Get all the items, read it as JSON
1. Create a new dictionary and use it to serialize JSON and send POST request

### Project 2 - Generating CSV data
1. Create file `reading_csv.py`. Import `csv`
1. Read the file `players.csv` using `csv.reader()`
1. Convert list of rows into list of player dictionaries
1. Find the name of the oldest player
1. Find the position of Kenny Lofton
1. Which team has the most Outfielders?

### Project 3 - Cart Items
Come up with an idea of a simple Product Cart for an online store. 
You should design two classes: `Cart` and `Product`. 
#### Product
Product should have `name` (string) and `price` (float).
#### Cart
The initial state of the cart is empty. Max number of products in cart is 10. Trying to add more than 10 items should throw error.
One should be able to add an item to cart (single or multiple).
One should be able to get all the names of items in cart.
One should be able to apply a special discount to cart: -20% if they provide a code `'XYZ123'`. If the code is invalid - an error should be raised.
One should be able to get the total price of cart by calculating sum of all prices of items in cart. Discount should be included if applied properly



 