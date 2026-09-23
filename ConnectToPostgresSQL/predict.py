import psycopg2
from ftConfig import load_config
from ftQuery import get_query
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.linear_model import LinearRegression,ElasticNet

    #"CREATE OR REPLACE VIEW testview AS SELECT '#title' key, 'fxrates' value UNION SELECT '#descriptions' key, 'au fxrates' value"
    #select * from countries ;
    #select * from staffs order by staffid;
    #select * from vwfxrates ;
    #select * from vwucinterestratesevenyrs ;
    #select series_id::date fx_date ,* from FXrates order by fx_date desc ; 
    #print("The number of parts: ", cur.rowcount)
    #current_date - 30

dataset = get_query("postgresql_Lenovo","select fxrusd,fxreur,fxrhkd,to_date(series_id,'DD-Mon-YYYY') seriesid from fxrates where (to_date(series_id,'DD-Mon-YYYY') >= current_date - 180) order by seriesid asc;")
main = pd.DataFrame(dataset, columns=['fxrusd','fxreur','fxrhkd','Date'])
#print(main)
X = main['Date'].astype('datetime64[s]')
y_usd = main['fxrusd'].values.astype(float)
y_eur = main['fxreur'].values.astype(float)
y_hkd = main['fxrhkd'].values.astype(float)

#print(X)
#======================================================
model_LR = LinearRegression()
usd_model_LR = model_LR.fit(X.values.reshape(-1,1),y_usd.reshape(-1,1))
model_LR = LinearRegression()
eur_model_LR = model_LR.fit(X.values.reshape(-1,1),y_eur.reshape(-1,1))
model_LR = LinearRegression()
hkd_model_LR = model_LR.fit(X.values.reshape(-1,1),y_hkd.reshape(-1,1))
#======================================================
today = max(X)
forecastDateAray = np.array([])
print(today)

for i in range(14):
    d = i+1
    nextday = today + dt.timedelta(days=d)
    forecastDateAray = np.append(forecastDateAray, nextday)

forecastDataset = pd.DataFrame(forecastDateAray, columns=['Date_Forecast'])
X_forecast = forecastDataset['Date_Forecast'].astype('datetime64[s]')
print(X_forecast)
#======================================================
y_pred_usd = usd_model_LR.predict(X_forecast.values.astype(int).reshape(-1,1))
y_pred_eur = eur_model_LR.predict(X_forecast.values.astype(int).reshape(-1,1))
y_pred_hkd = hkd_model_LR.predict(X_forecast.values.astype(int).reshape(-1,1))

forecastDataset['usd_prediction'] = y_pred_usd
forecastDataset['usd_prediction'] = forecastDataset['usd_prediction'].round(5)
forecastDataset['eur_prediction'] = y_pred_eur
forecastDataset['eur_prediction'] = forecastDataset['eur_prediction'].round(5)
forecastDataset['hkd_prediction'] = y_pred_hkd
forecastDataset['hkd_prediction'] = forecastDataset['hkd_prediction'].round(5)
forecastDataset['Date_Forecast'] = pd.to_datetime(forecastDataset['Date_Forecast'].values, format="%d-%b-%Y")
print(forecastDataset)

import_data = []
for i in forecastDataset.values:
    series = pd.Series(i)
    
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
    import_data.append(row_value)
#======================================================
#insert predicted values into table fxratesForecast
config  = load_config('database.ini','postgresql_Lenovo')
try:
    with  psycopg2.connect(**config) as conn:
        with  conn.cursor() as cur:
            # execute the INSERT statement
            print("Executing SQL query...")
            cur.execute("TRUNCATE TABLE fxratesForecast ;")
            cur.executemany("INSERT INTO fxratesForecast (Date_Forecast, fxrusdPrediction, fxreurPrediction, fxrhkdPrediction) VALUES (%s,%s,%s,%s) RETURNING *;",import_data) #sql, value
            # commit the changes to the database
            print("Committing changes...")
            conn.commit()
            print("Commit Successful!")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)