from common.libs import (
    pd,np,plt
)

def read_data(dataPath): # "dataPath" is input variable & positional argument.it is an input string 
    #Here type of "data" is dataframe.Here "dataPath" is a "relative Path"."read_csv" is a functopn in Pandas
    df = pd.read_csv(dataPath) #"read_csv" is a function it reads file from directory & convert into dataframe and puts into memory(RAM)
    return df

