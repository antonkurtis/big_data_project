import mysql.connector  
import pandas as pd


def get_data():
    conn = mysql.connector.connect(
        user='arhimag', 
        password='password57',                
        host='84.201.152.135',
        database='hse'
        )

    query_disc = 'select * from avg_discount_price'
    df_disc = pd.read_sql(query_disc, con=conn)

    query_reg = 'select * from avg_regular_price'
    df_reg = pd.read_sql(query_reg, con=conn)

    query_salary = 'select * from avg_salary'
    df_salary = pd.read_sql(query_salary, con=conn)

    conn.close()

    df_disc.to_csv('data/df_disc.csv', index=False)
    df_reg.to_csv('data/df_reg.csv', index=False)
    df_salary.to_csv('data/avg_salary.csv', index=False)
