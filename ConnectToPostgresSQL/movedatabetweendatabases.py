from ftQuery import get_query
import psycopg2
from ftConfig import load_config

table = 'interestrate'

output = get_query('postgresql_HP','select Series_ID, FIRMMCRT,FIRMMCRI,FIRMMCRIHM, '\
'FIRMMCRILM, FIRMMCRIVM, FIRMMCRINM, FIRMMBAB30,	'\
'FIRMMBAB90, FIRMMBAB180, FIRMMOIS1, FIRMMOIS3, '\
'FIRMMOIS6, FIRMMTN1, FIRMMTN3,FIRMMTN6 from '+table+';')
input = get_query('postgresql_Lenovo','select Series_ID, FIRMMCRT,FIRMMCRI,FIRMMCRIHM, '\
'FIRMMCRILM, FIRMMCRIVM, FIRMMCRINM, FIRMMBAB30,	'\
'FIRMMBAB90, FIRMMBAB180, FIRMMOIS1, FIRMMOIS3, '\
'FIRMMOIS6, FIRMMTN1, FIRMMTN3,FIRMMTN6 from '+table+';')

print("source: {0} \n target: {1}".format(output,input))

config = load_config('database.ini','postgresql_Lenovo')

length = len(output[0])
columns_insert = ""
for i in range(length):
    columns_insert = columns_insert+"%s"+","

columns_insert = columns_insert[:len(columns_insert)-1]
# print(columns_insert)

try:
    with  psycopg2.connect(**config) as conn:
        with  conn.cursor() as cur:
            # execute the INSERT statement
            print("Executing SQL query...")
            cur.execute("TRUNCATE TABLE "+table+";")
            cur.executemany("insert into "+table+" ( Series_ID, FIRMMCRT,FIRMMCRI,FIRMMCRIHM, "\
                            "FIRMMCRILM, FIRMMCRIVM, FIRMMCRINM, FIRMMBAB30,	"\
                            "FIRMMBAB90, FIRMMBAB180, FIRMMOIS1, FIRMMOIS3, "\
                            "FIRMMOIS6, FIRMMTN1, FIRMMTN3,FIRMMTN6) values ("+columns_insert+") returning *;",output) #sql, value
            #INSERT INTO "+table_name+" ("+table_columns+") VALUES ("+columns_insert+") RETURNING *;
            # commit the changes to the database
            print("Committing changes...")
            conn.commit()
            print("Commit Successful!")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)