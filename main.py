# In addition to the above requirements, your files must be stored using the convention discussed in the lecture. You will be submitting a ZIP file containing all of your files.


# part 1: creates an empty list
sales_data = []

# part 2: opens up this file (SalesJan2009.csv - you need to download it to your hard drive) and converts the data within it to JSON format. 

import csv, json

sale_type = ["Transaction_date", "Product", "Price", "Payment_Type", "Name", "City", "State", "Country"]

with open("SalesJan2009.csv", "r") as inFile:
  csvReader = csv.reader(inFile)
  # part 3: You will process this line-by-line and create a dictionary of each line. As you create each dictionary, you will append it to the sales_data list. 
  #         You must also clean up extra quote characters from each piece of data you process.
  for line in csvReader:
    dictionary = dict(zip(sale_type, line))
    sales_data.append(dictionary)
    json_object = json.dumps(sales_data, indent = 4) 
    print(json_object)
    

# part 4: At the end of your processing, you will save your sales_data list to a file called "transaction_data.json"
with open("transaction_data.json", 'w') as outFile:
    outFile.write(json_object)