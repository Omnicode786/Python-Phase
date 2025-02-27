# Question 5
# # Fill in the blanks to complete the “countries” function. This function accepts a dictionary containing a list of continents (keys) and several countries from each continent (values).  For each continent, format a string to print the names of the countries only. The values for each key should appear on their own line.
def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for continent, countries in countries_dict.items():
        # Use a string method to format the required string.
        result += str(countries)+'\n'

    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']
