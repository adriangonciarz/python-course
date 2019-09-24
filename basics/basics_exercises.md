## Basics - exercises
### Exercise 1 - string formatiign
Define variables:

    * firstname (string)
    * lastname (string)
    * age (integer)
    * phone (string)
    * height (float)
Print a string that takes variables and formats it to the following sentence:

```
My name is $firstname $lastname. I'm $age years old and my height is $heigh meters. Here is my phone number: $phone.
```

In two ways: using `f-string` and `format()`

Use the following values:

    * firstname - Patty
    * lastname - Smith
    * age - 27
    * phone - +421112223344
    * height - 1.73

### Exercise 2 - Lists and dictionaries
Create a list containing car companies:
```
cars = ['Audi', 'Honda']
```
Add some other car companies to the list (3 items)
Now find a way to replace first and last element in the list

Create dictionary containing user data:
```
{
    'first_name': 'mike',
    'last_name': 'skinner',
    'email': 'mikey@example.com'
}
```
Add new key/value pair to the dictionary: `'city': 'London'`

Print all keys in the dictionary. Make the values for `firstname, lastname and city` capitalized.

### Exercise 3 - loops
Having given the following arrays of data:
```
firstnames = ['Adam', 'Katy', 'Mike', 'Jenna', 'Jim', 'Patty']
lastnames = ['Smith', 'Connor', 'Tyler', 'Bonham', 'McCreddy', 'Jameson']
```
Loop 10 times to prepare an array of dictionaries with 10 elements. Each dictionary have to contain the following:
    * `firstname` -> random element from the list `firstnames`
    * `lastname` -> random element from the list `lastnames`
    * `email` -> of the form `firstname.lastname@example.com`
Afterwards, print all emails in the list.

### Exercise 4 - if/else clause
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

### Exercise 5 - List comprehension
Using list comprehension:
1. Create a new list that contains positive numbers of the following list `numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]`
2. Create a new list containing the character count of all the words in the sentence `sentence = "the quick brown fox jumps over the lazy dog"` except for the word `the`