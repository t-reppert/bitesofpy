from os import path
from urllib.request import urlretrieve
from datetime import datetime
import pandas as pd
import numpy as np

EXCEL = path.join('/tmp', 'order_data.xlsx')
if not path.isfile(EXCEL):
    urlretrieve('https://bit.ly/2JpniQ2', EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(excel, sheetname='SalesOrders')


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df['Year'] = df['OrderDate'].apply(lambda x: int(datetime.strftime(x,'%Y')))
    grouped = df.groupby(['Year','Region'])
    return grouped['Total'].agg(np.sum)

def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    grouprep = df.groupby(['Rep']).sum().sort_values('Total',ascending=False).iloc[0]
    return grouprep.name, grouprep.Total



def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    groupbyitem = df.groupby(['Item']).sum().sort_values('Units',ascending=False).iloc[0]
    return groupbyitem.name, groupbyitem.Units