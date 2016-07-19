import pandas as pd

apiBase = "http://api.worldbank.org/indicator/"
apiIndicator = "SI.POV.GINI"    # This can be changed to any other indicator
FILE_NAME = 'gini-index.csv'
source = apiBase+apiIndicator+"?format=csv"


def main ():
    data=pd.read_csv(source)
    data.to_csv('data/cash-surp-def.csv', sep=",", index_col=0, index=False)
