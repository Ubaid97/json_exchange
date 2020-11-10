# importing json module to use built-in json functions
import json

# opening previously created json file containing the currency exchange rates of different countries
with open("exchange_rates.json") as jsonfile: # file aliased as jsonfile
    c_rates = json.load(jsonfile) # load() copies the data and stores it into a variable
    print(c_rates) # prints the contents of the json file

# for loop that iterates over the items of the rates dictionary
for country, rate in c_rates["rates"].items(): # c_rates["rates"] is a dictionary within c_rates
    # every key and value (ie country and exchange rate) is printed in the format:
    print(f"Country: {country} - Rate: {rate}")