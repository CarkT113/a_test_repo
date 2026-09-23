import psycopg2
from config import load_config
from getData import get_data

def create_tables():
    #Create tables in the PostgreSQL database
    #data = get_data("FXrates","/readCSV?category=FXrates","create")
    #command = data[1]
    #"CREATE OR REPLACE VIEW testview AS SELECT '#title' key, 'fxrates' value UNION SELECT '#descriptions' key, 'au fxrates' value;"
    #"InterestRate","/readCSV?category=InterestRate"
    #"FXrates","/readCSV?category=FXrates"
    data = get_data("InterestRate","/readCSV?category=InterestRate","create") #table_name, url_variant, query_type
    command = ";"

    config = load_config()
    
    sql = data[1]
    print(sql)
    print(data[2])
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                print("Executing SQL query...")
                if sql == "" :
                    print(command)
                    cur.execute(command)
                else:
                    print(sql)
                    cur.execute(sql)
                print("Committing changes...")
                conn.commit()
                print("Commit Successful!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()