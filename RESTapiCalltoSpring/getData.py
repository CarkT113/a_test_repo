import json
import requests
import pandas as pd

# Define the URL of your Spring Boot API endpoint
#requestCategory = "country/allcountries"
#requestCategory = "readCSV?category=Country"
#requestCategory = "readCSV?category=StaffRecord"
requestCategory = "readCSV?category=FXrates"
url = "http://localhost:8080/"+requestCategory  # Replace with your actual endpoint

# Define request parameters or data (if needed)
#params = {"param1": "value1"}
#data = {"key": "value"}

# Make a GET request
response = requests.get(url)

# Make a POST request
#response = requests.post(url, json=data)

# Check the response status and content
if response.status_code == 200:
    print("Success!")
    requestCategory_data = response.text
    cell_data = json.loads(requestCategory_data)
    df = pd.DataFrame(cell_data.items())
    firstrow = df[1][0]
    column = list(firstrow.keys())
    #print(column) #get column
    data = []
    table_columns = ""
    columns_insert = ""
    for i in column:
        #print(i)
        table_columns = table_columns + i + ","
        columns_insert = columns_insert+"%s"+","
        print(table_columns)
    table_columns = table_columns[:len(table_columns)-1]
    columns_insert = columns_insert[:len(columns_insert)-1]
    #print(table_columns)
    #print(columns_insert)
    sql = "INSERT INTO STAFF ("+table_columns+") VALUES ("+columns_insert+") RETURNING *"
    print(sql)

    for i in df[1]: # object
        #print(i)    #row object
        series = pd.Series(i)
        #print(series)
        row_value = ()      #row values as a tuple
        for j in series:    #item in each column
            #print(j)
            y = list(row_value) #convert tuple into a list to use append for 
            y.append(j)         #inserting row values
            #print(row_value)
            # insert into a column list
            # row.append()
            row_value = tuple(y)
        #print(row_value)
        data.append(row_value)
    
    #print(data)
            
else:
    print(f"Error: {response.status_code}")
    print(response.text)