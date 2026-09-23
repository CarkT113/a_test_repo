import psycopg2
from ftConfig import load_config
from ftGetData import get_data

def insert_table():

    #"countries","/readCSV?category=Country","insert"
    #"FXrates","/readCSV?category=FXrates","insert"
    #"InterestRate","/readCSV?category=InterestRate"
    data = get_data("FXrates","/readCSV?category=FXrates","insert") #table_name, url_variant, query_type
    config = load_config('database.ini','postgresql_Lenovo')
    
    sql = data[1]
    print(sql)
    print(data[2])
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                print("Executing SQL query...")
                cur.execute("TRUNCATE TABLE "+data[0]+";")
                cur.executemany(sql,data[2]) #sql, value
                # commit the changes to the database
                print("Committing changes...")
                conn.commit()
                print("Commit Successful!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    insert_table()