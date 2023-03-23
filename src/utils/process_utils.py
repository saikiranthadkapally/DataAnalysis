from common.config import(
    NUMERIC_TYPES,
    OBJECT_TYPES,
    NOMINAL_THRESHOLD
)
from common.libs import(
    yp
)

def get_profiling_report(data):
    report = yp.ProfileReport(data)
    reportJson = report.get_description()
    return reportJson


    """
    METHOD 1(Logic): 
    df1 = df.select_dtypes(OBJECT_TYPES) #Here "df1" is our temporary dataframe where "df" is our main dataframe
    cat_features = list(df1.columns)
    Note:
    Here "cat_features" means categorical attributes/features inorder to obtain "cat_features" we need to minus or subtract "numeric_features" from main "df.column"
    Inorder to do that we use "set()" datatype function for minus Bcs we don't have that operation in "list()" calss.like minus(subtract) the one list from another list  
    Note: In set we have that operation which we perform minus operation in "set()" class.

    num_features = list(set(df.columns) - set(cat_features))
    return num_features
    
    #****Note****: Here we are writing it from "Scratch" using Pandas Without taking Or Using "ydata_profiling(which generate "report" for given data)".
    #METHOD 2(Logic)
    cat_features = list(df.select_dtypes(OBJECT_TYPES).columns)
    num_features = list(df.select_dtypes(NUMERIC_TYPES).columns)
    #"assert" which returns the given statement is true or false -- Here "assert" tells or print output stmt and exits or stops the code/program automatically 
    assert len(df.columns) == len(cat_features)+len(num_features),"[ERROR] Splitting features is not proper"
    return num_features,cat_features
    """
    #Here We are using "ydata_profiling" help without writing it from "Scratch"
    '''
    Here we are getting in datatype of "dict_keys".But In our analysis we only needs only Basic datatypes(like lists & tuples etc..)
    Bcs we are more acquaintance with the those basic operations only which we use mostly.So,we need to convert it into list 
    explicitly.
    '''
    #Split the features into numeric and categorical
def split_features(reportJson):
    #Here we written ".keys" after "{k:v for k,v in reportJson["variables"].items() if v["type"] == "Numeric"}" Bcs we intrested in variables only which are "keys"
    num_features = list({k:v for k,v in reportJson["variables"].items() if v["type"] == "Numeric"}.keys())
    cat_features = list({k:v for k,v in reportJson["variables"].items() if v["type"] == "Categorical"}.keys())
    if not len(num_features) + len(cat_features) == reportJson["table"]["n_var"]:
        print("[WARNING] There are some unsupported types, please look into the dataset")
        
    return num_features,cat_features

def split_cat_features(reportJson,cat_features):
    """
    Split the cat features into binary, ordinal and nominal
    """
    #This Ordinal something what which we require it from the Domain Expert
    variables = reportJson["variables"]
    unary_features = []
    binary_features = []
    nominal_features = []
    for feature in cat_features:
        if variables[feature]["n_distinct"] == 1:
            unary_features.append(feature)
        elif variables[feature]["n_distinct"] == 2:
            binary_features.append(feature)
        else:
            nominal_features.append(feature)
    
    return unary_features, binary_features, nominal_features

#Inside "nominal features" some of them are important and some of them are non-important based on the  "Categorical threshold" Or "NOMINAL_THRESHOLD"
#Here we after splitting nominal features into "imp & nonimp" features to provide more feasibility to clients to make decisions on it.
#Before Proceeding to write code in this we need to test it in JUPYTER NOTEBOOK.It is not space environment to test our code.
def split_nominal_features(reportJson,nominal_features):
    #This is the logic which simulated by our model automation similar to human analysis.We are making model to simulate as humans
    no_examples = reportJson["table"]["n"] #Here "n"  is the no.of.rows/examples/instances/observations in a table
    nominal_features_imp = [] #This holds all non-important features in nominal_features
    nominal_features_nonimp = [] #This holds all important features in nominal_features
    variables = reportJson["variables"]
    for feature in nominal_features: 
        if variables[feature]["n_distinct"] == no_examples: #Here "n_distinct" is no.of.distict values in a particular feature 
            nominal_features_nonimp.append(feature)
        elif variables[feature]["n_distinct"] >= NOMINAL_THRESHOLD: #We are doing "off" of the no.of.rows in a table
            nominal_features_nonimp.append(feature)
        else:
            nominal_features_imp.append(feature)

    return nominal_features_imp,nominal_features_nonimp
'''
This is the some Rare case.Suppose,if our "ydata_profiling" providing anything in future by mistakely Or whatever may be at "back-end" logic .We have 
to find that and we have to analyze that and aswell as we have to do this.May be this may also requires some sort of Machine Learning automation model Or 
even by using normal like statistical & thresold and for loop etc..
'''
#We have to do this But we are justing keeping as a To-do list
def find_numeric_cat_features(df,cat_features):
    """
    Finding numerical features in categorical features

    Note:It doesn't seems always be fine.Numerical features are possible to come in Categorical features are very rare.We won't get anytime.
         But "ydata_profiling" gives good result here."ydata_profiling" library/framework correctly classifies the "Numerical variables" from "Categorical variables"
         
   
    """

#"ydata_profiling" is not good in finding "categorical" features from "numerical" features.Here we need to write one more module for this Or We need
# to build an intellegence ML automation model inorder to find "Categorical" features  from "Numerical" features  
def filter_cat_in_numeric_features(df,numeric_features):
    """
    Filter out categorical features from numerical features

    Here we need to apply some intelligence to this.Some other technique called: But this we don't do this in our "Feature Engineering" Module/Project
        Advanced Profiling ---> All the "Data Statistical Information" of that particular column(like "PassengerId" etc..) --> send to intelligence ML model to identify

    """
    pass

"""
 In addition to these Categorical and Numerical We also do as follows:
        --- Is any column has same values
        --- Is any column has zeros
        This is must be reported to the Domain Experts and Data generating teams Bcs In some of the situations the data generation system by any reason that system 
        by default settings or any of the settings it may populate zeroes in all columns which is really undesirable.When we find zero in our result which generated by
        our "Feature Engineering" module or Our automated System when it find the "zero" we immediately send an very high important email or immediately send an email
        to our Clients by saying that "your data generating system populating Zeroes".When wwe encounter such situation completely stop as soon as possible.
        --- In a particular column how many null values are there
"""
def filter_alerts(reportJson):

    zero_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[ZEROS]", reportJson["alerts"]))
    zero_features = list(map(lambda x:str(x).split(" ")[-1], zero_alerts))
    constant_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[CONSTANT]", reportJson["alerts"]))
    constant_features = list(map(lambda x:str(x).split(" ")[-1], constant_alerts))
    nonimpnominal_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[HIGH_CARDINALITY]", reportJson["alerts"]))
    nonimpnominal_features = list(map(lambda x:str(x).split(" ")[-1], nonimpnominal_alerts))
    missing_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[MISSING]", reportJson["alerts"]))
    #Here "missing" features are nothing but "null" values Or "null" features
    missing_features = list(map(lambda x:str(x).split(" ")[-1], missing_alerts))
    uniform_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[UNIFORM]", reportJson["alerts"]))
    uniform_features = list(map(lambda x:str(x).split(" ")[-1], uniform_alerts))
    nonuniform_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[IMBALANCED]", reportJson["alerts"]))
    nonuniform_features = list(map(lambda x:str(x).split(" ")[-1], nonuniform_alerts))
    unsupported_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[UNSUPPORTED]", reportJson["alerts"]))
    unsupported_features = list(map(lambda x:str(x).split(" ")[-1], unsupported_alerts))
    unique_alerts = list(filter(lambda x:str(x).split(" ")[0] == "[UNIQUE]", reportJson["alerts"]))
    unique_features = list(map(lambda x:str(x).split(" ")[-1], unique_alerts))

    return (zero_features, constant_features,
            nonimpnominal_features, missing_features,
            uniform_features, unique_features,
            unsupported_features, nonuniform_features
            )

#TO_DO List(Assignment) 
#Here we can again split the above "alerts" into further "numerical" zero features & "categorical" zero features.
def split_zero_features(zero_features,reportJson):

    """
    return num_zero_features,cat_zero_features
    """

def split_unique_features(unique_features,reportJson):
    """
    return num_unique_features,cat_unique_features
    """

"""
Note:In same way as above We can also do it for "constant_features", " nonimpnominal_features" etc.... Based on our personal Intereset and time we can
     Proceed with it in future.
"""
