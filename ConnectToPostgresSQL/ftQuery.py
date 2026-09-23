#from getData import get_data
import psycopg2
from ftConfig import load_config

#data = get_data("FXrates","/readCSV?category=FXrates","insert")

#print(data[0])
#print(data[1])

def get_query(database_location,query):
    """ Retrieve data from the vendors table """
    config  = load_config('database.ini',database_location)
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                 query
                )
                #"CREATE OR REPLACE VIEW testview AS SELECT '#title' key, 'fxrates' value UNION SELECT '#descriptions' key, 'au fxrates' value"
                #select * from countries ;
                #select * from staffs order by staffid;
                #select * from vwfxrates ;
                #select series_id::date fx_date ,* from FXrates order by fx_date desc ; 
                #print("The number of parts: ", cur.rowcount)
                #CREATE VIEW {view_name} AS SELECT
                conn.commit()
                rows = cur.fetchall()
                #print(row)

                for i in rows:
                    print(i)
                    i = cur.fetchone()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return (rows)

if __name__ == '__main__':
    get_query()