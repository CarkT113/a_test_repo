import psycopg2
from config import load_config

def get_vendors():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                 "select * from vwucinterestratesevenyrs ;"
                )
                #"CREATE OR REPLACE VIEW testview AS SELECT '#title' key, 'fxrates' value UNION SELECT '#descriptions' key, 'au fxrates' value"
                #select * from countries ;
                #select * from staffs order by staffid;
                #select * from vwfxrates ;
                #select series_id::date fx_date ,* from FXrates order by fx_date desc ; 
                #print("The number of parts: ", cur.rowcount)
                #CREATE VIEW {view_name} AS SELECT
                row = cur.fetchone()
                #print(row)

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_vendors()