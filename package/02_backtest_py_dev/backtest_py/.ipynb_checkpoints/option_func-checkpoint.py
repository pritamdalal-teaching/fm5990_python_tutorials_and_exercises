import numpy as np
import pandas as pd
import mysql.connector



def option_chain(trade_date, underlying, expiration, exclude_zero_bid=False):
    """returns an option chain for a particular trade-date"""
    
    
    # putting together the sql query from the inputs
    str_sql = \
    """
    SELECT * 
    FROM delta_neutral.option_price 
    WHERE DataDate='{}' 
    AND UnderlyingSymbol='{}'
    AND Expiration='{}';"
    """.format(trade_date, underlying, expiration)
    
    # calling the function that queries the database
    df_mysql = db_option(str_sql, exclude_zero_bid) 
    
    return(df_mysql)



def option_underlying(trade_date, underlying, exclude_zero_bid=False):
    """
    returns all options for an underlying on a
    particular trade-date
    """
    
    # putting together the sql query from the inputs
    str_sql = \
    """
    SELECT * 
    FROM delta_neutral.option_price 
    WHERE DataDate='{}' 
    AND UnderlyingSymbol='{}';"
    """.format(trade_date, underlying)
    
    # calling the function that queries the database
    df_mysql = db_option(str_sql, exclude_zero_bid)
    
    return(df_mysql)


def option_all(trade_date, underlying, exclude_zero_bid=False):
    """
    returns all options from particular trade-date
    """
    
    # putting together the sql query from the inputs
    str_sql = \
    """
    SELECT * 
    FROM delta_neutral.option_price 
    WHERE DataDate='{}';"
    """.format(trade_date)
    
    # calling the function that queries the database
    df_mysql = db_option(str_sql, exclude_zero_bid)
    
    return(df_mysql)




def db_option(str_sql, exclude_zero_bid=False):
    
    # opening database connection
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password"
    )
    
    # executing query and putting results into a DataFrame
    df_mysql = pd.read_sql(str_sql, con=mydb) 
    
    
    # adding the Mid column
    df_mysql['Mid'] = (df_mysql['Bid'] + df_mysql['Ask']) / 2
    
    # columns to keep, and rearranging
    lst_col = ['UnderlyingSymbol', 'UnderlyingPrice', 'Type', 'Expiration'
                , 'DataDate', 'Strike', 'Bid' , 'Ask', 'Mid', 'Volume'
               , 'OpenInterest', 'T1OpenInterest', 'IVMean']
    df_mysql = df_mysql[lst_col]
    
    
    # renaming columns
    dct_rename = {'UnderlyingSymbol':'underlying_symbol'
                  , 'UnderlyingPrice':'underlying_price'
                  , 'Type':'type', 'Expiration':'expiration'
                  , 'DataDate':'data_date', 'Strike':'strike'
                  , 'Bid':'bid', 'Ask':'ask', 'Mid':'mid'
                  , 'Volume':'volume', 'OpenInterest':'open_interest'
                  , 'T1OpenInterest': 't1_open_interest'
                  , 'IVMean':'iv_mean'}
    df_mysql.rename(columns=dct_rename, inplace=True)
    
    
    # excluding zero bids
    if exclude_zero_bid:
        df_mysql = df_mysql[df_mysql['bid'] > 0]
    
    # closing the database connection
    mydb.close()
    
    return(df_mysql)