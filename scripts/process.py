#!/usr/bin/python
import csv, os, sys
import pandas as pd
import numpy as np

apiBase = "http://api.worldbank.org/indicator/"
apiIndicator = "GC.BAL.CASH.GD.ZS"    # This can be changed to any other indicator
FILE_NAME = 'gini-index.csv'
source = apiBase+apiIndicator+"?format=csv"


def main():
    data=pd.read_csv(source)
    data.to_csv('archive/cash-surp-def.csv', sep=",", index_col=0, index=False)
    print ('Successly retrieve data.')

    
    # Python is printing "Country Name", thus getting some erros in the end
    df = pd.read_csv("archive/cash-surp-def.csv")
    
    # Data comes with several special characters and spaces
    df.columns.values[0] = 'Country Name'
    
    df = pd.melt(df, id_vars=['Country Name', 'Country Code'], var_name="Year", value_name="Value")
    df = df.sort_values(by=['Country Name', 'Year'], ascending=[True, True])
    
    df['Country Name'] = df['Country Name'].replace(' |\.|"|,|\'|:|-|\(|\)', '', regex=True)
    df['Country Name'] = df['Country Name'].replace('&', 'AND', regex=True)

    df.dropna().to_csv('data/cash-surp-def.csv', sep=",", index=False)
    
    print ("File Saved.")

if __name__ == '__main__':
    main()
