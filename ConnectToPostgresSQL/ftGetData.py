import json
import requests
import pandas as pd

def get_data(table_name, url_variant, query_type):
    
    # Define the URL of your Spring Boot API endpoint
    option = url_variant #"/readCSV?Record=StaffRecord"
    url = "http://localhost:8080"+option  # Replace with your actual endpoint

        # Make a GET request
    response = requests.get(url)
        # Check the response status and content
    if response.status_code == 200:
        #print("Success!")
        user_data = response.text
        cell_data = json.loads(user_data)
        df = pd.DataFrame(cell_data.items())
        firstrow = df[1][0]
        column = list(firstrow.keys())
            #print(column) #get column
        data = []

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

        table_columns = ""
        columns_insert = ""
        for i in column:
            j = i.replace(" ","_")
            if query_type == "insert":
                table_columns = table_columns + j + ","
            else: 
                if query_type == "create":
                    table_columns = table_columns + j + " varchar(100),"
                else:
                    break
            columns_insert = columns_insert+"%s"+","
            #print(table_columns)
        table_columns = table_columns[:len(table_columns)-1]
        columns_insert = columns_insert[:len(columns_insert)-1]
        #print(table_columns)
        #print(columns_insert)
        if query_type == "insert":
            sql = "INSERT INTO "+table_name+" ("+table_columns+") VALUES ("+columns_insert+") RETURNING *;"
        else: 
            if query_type == "create":
                sql = "CREATE TABLE "+table_name+" ("+table_columns+");"
            else:
                sql = ""

                
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    
    return (table_name,sql,data)

if __name__ == '__main__':
    get_data()