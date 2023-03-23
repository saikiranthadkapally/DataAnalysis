'''
In this we write our main business logic code.In this the businees logic for our "DATAANALYSIS Or Feature Engineering" will be Written.
'''
'''
Note:Our module/project/program/software will work for "Agnostic" dataset.Also We again Recheck or Analyze the data which was given as an Output and 
also we need to approach towards the domain expert inorder to take any decisions.
'''
#Before Main logic starts we have to get the data path from config
from common.config import(
    DATA_PATH
)
from utils.read_utils import(
    read_data
)
from utils.process_utils import(
    get_profiling_report,
    split_features,
    split_cat_features,
    split_nominal_features,
    filter_alerts
)
def main():
    data = read_data(dataPath=DATA_PATH)
    reportJson = get_profiling_report(data)
    #After generating report we have to segregate the "num_features" & "cat_features"
    num_features,cat_feature = split_features(reportJson)
    unary_features,binary_features,nominal_features = split_cat_features(reportJson,cat_feature)
    nominal_features_imp,nominal_features_nonimp = split_nominal_features(reportJson,nominal_features)
    (zero_features, constant_features,
            nonimpnominal_features, missing_features,
            uniform_features, unique_features,
            unsupported_features, nonuniform_features) = filter_alerts(reportJson)
    
    print("Num Features: ",num_features)
    print("Cat Features: ",cat_feature)
    print("Unary Features: ",unary_features)
    print("Binary Features: ",binary_features)
    print("Nominal Features: ",nominal_features)
    print("NonImp Nominal Features: ",nominal_features_nonimp)
    print("Imp Nominal Features: ",nominal_features_imp)
    print("Zero Features: ",zero_features)
    print("Constant Features: ",constant_features)
    print("High Cardinality: ",nonimpnominal_features)
    print("Missing Features: ",missing_features)
    print("Uniform Features: ",uniform_features)
    print("Unique Features: ",unique_features)
    print("Unsupported Features: ",unsupported_features)
    print("Imbalanced Features: ",nonuniform_features)

"""
*******************************************************************Note***********************************************************************************************

Note: Upto here we have completed "Data Preprocessing" and "Feature Engineering" Prerequisites

***********************************************************************************************************************************************************************
"""

if __name__== "__main__":
    main()