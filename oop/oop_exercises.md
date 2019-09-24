## Object Oriented Programming - Exercises
### Exercise 1 - methods
Create a new file called `toolkit.py`
Create the following methods:
* `list_sum(provided_list)` to sum all the numbers in a provided list
* `reverso(some_string)` to reverse provided string
* `calculate_upper(sentence)` - a function that accepts a string and calculate the number of upper case letters and lower case letters, then returns both numbers

### Exercise 2 - Complex functions
Let's use functions to calculate your trip's costs:

Define a function called `hotel_cost` with one argument nights as input. The hotel costs 140PLN per night. So, the function `hotel_cost` should return `140 * nights`.
Define a function called `plane_ride_cost` that takes a string, city, as input. The function should return a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.
```
"Cracow": 183
"Wroclaw": 220
"Warsaw": 222
"London": 475
```
Below your existing code, define a function called `rental_car_cost` with an argument called `days`. Calculate the cost of renting the car: Every day you rent the car costs `90PLN`.(`cost=90*days`) if you rent the car for 7 or more days, you get 50PLN off your total(`cost-=50`). Alternatively (`elif`), if you rent the car for 3 or more days, you get `20` off your total. You cannot get both of the above discounts. Return that cost.
Then, define a function called trip_cost that takes two arguments, city and days. Like the example above, have your function return the sum of calling the `rental_car_cost(days)`, `hotel_cost(days)`, and `plane_ride_cost(city)` functions.
Modify your `trip_cost` function definition. Add a third argument, `spending_money`. Modify what the `trip_cost` function does. Add the variable `spending_money` to the sum that it returns.

### Exercise 3 - simple class
