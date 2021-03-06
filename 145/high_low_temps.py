from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a datetime.date() object.
    The temperatures in the dataset are in tenths of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.
    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day between 2005-2015
       * Extract lowest temperatures for each day between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days
    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015
    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID, Date, Value
    5. From the record breakers in 2015, extract the high/low of all the temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    df = pd.read_csv(DATA_FILE)
    # strip leap dates
    df = df.loc[df.loc[:,'Date'].str.contains('-02-29')==False]
    df['Date'] = pd.to_datetime(df.loc[:,'Date'])

    # Max groups
    maxes = df.loc[df.loc[:,'Element']=='TMAX']
    maxes.rename(columns={'Data_Value':'TMAX','ID':'ID_MAX'}, inplace=True)
    gb_max = maxes.groupby('Date')['TMAX'].idxmax()

    # Min groups
    mins = df.loc[df.loc[:,'Element']=='TMIN']
    mins.rename(columns={'Data_Value':'TMIN','ID':'ID_MIN'}, inplace=True)
    gb_min = mins.groupby('Date')['TMIN'].idxmin()

    min_df = mins.loc[gb_min]
    min_df.drop('Element',axis=1,inplace=True)
    min_df.set_index('Date',inplace=True)

    max_df = maxes.loc[gb_max]
    max_df.drop('Element',axis=1,inplace=True)
    max_df.set_index('Date',inplace=True)

    df_combined = max_df.join(min_df)

    df_combined.reset_index(inplace=True)
    df_0514 = df_combined.loc[df_combined.loc[:,'Date'].dt.year < 2015]
    df_2015 = df_combined.loc[df_combined.loc[:,'Date'].dt.year == 2015]

    dict2015 = {}
    for row in df_2015.itertuples():
        month = str(row.Date.month)
        day = str(row.Date.day)
        dict2015[month+"_"+day] = { 'Date':row.Date.date(), 
                                    'ID_MIN':row.ID_MIN, 
                                    'ID_MAX':row.ID_MAX, 
                                    'TMIN':row.TMIN,
                                    'TMAX':row.TMAX }

    max_val = []
    min_val = []
    for row in df_0514.itertuples():
        month = str(row.Date.month)
        day = str(row.Date.day)
        lookup = dict2015[month+"_"+day]

        if row.TMAX < lookup['TMAX']:
            max_val.append(STATION(ID=lookup['ID_MAX'], Date=lookup['Date'], Value=lookup['TMAX']/10))
        if lookup['TMIN'] < row.TMIN:
            min_val.append(STATION(ID=lookup['ID_MIN'], Date=lookup['Date'], Value=lookup['TMIN']/10))

    max = sorted(max_val,key=lambda x: x.Value,reverse=True)[0]
    min = sorted(min_val,key=lambda x: x.Value)[0]

    return max, min

