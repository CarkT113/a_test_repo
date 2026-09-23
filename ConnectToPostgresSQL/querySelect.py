import psycopg2
from config import load_config
from query import get_vendors
from ftQuery import get_query

# get_vendors("select fxrusd,fxreur,fxrhkd,to_date(series_id,'DD-Mon-YYYY') seriesid from fxrates where (to_date(series_id,'DD-Mon-YYYY') >= current_date - 180) order by seriesid asc;")

data = get_query('postgresql_Lenovo','select * from fxrates;')

#print("results: {0}".format(data[0]))
#print("results: {0}".format(len(data[0])))
length = len(data[0])

columns_insert = ""
for i in range(length):
    columns_insert = columns_insert+"%s"+","

columns_insert = columns_insert[:len(columns_insert)-1]
print(columns_insert)