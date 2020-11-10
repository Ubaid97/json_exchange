# JSON currency exchange task
**Steps**
- Create a new json file called exchange_rates.json
- copy and paste the data from trello board
- Create a python file to implement code
- ```import json``` module to use json methods
- open the json file containing exchange rate data:
```python
with open("exchange_rates.json") as jsonfile: # file aliased as jsonfile
    c_rates = json.load(jsonfile) # load() copies the data and stores it into a variable
    print(c_rates) # prints the contents of the json file
```
- Task is to print out the countries and their rates
- the rates are contained in a dictionary within the c_rates dictionary
- use a for loop to iterate over the contents of the rates dictionary and print out its contents:
```python
for country, rate in c_rates["rates"].items(): # c_rates["rates"] is a dictionary within c_rates
    # every key and value (ie country and exchange rate) is printed in the format:
    print(f"Country: {country} - Rate: {rate}")
```