"""
Rules for Config Variables
   Constants -- CAPITAL CASE with _ as Connector

Relative Path ---from current working directory -- Here the CWD is our "src" folder -- In Projects Mostly We use "Relative Path"  with Docker perspective
Absolute Path --- the path should be defined from root -- It starts from root -- Here "root" path is like "C:/User/savin/..." -- For "root" path we also need to set 
System path also.

Note:Even though It is not "Docker" When we perform it by creating our "environment" then also our relative path will be "src" folder only(In this Project).
So, In our terminal or command prompt we must change our directory to "src" using "cd src" While we setting our 'Relative Path" Suppose if not change in case we get 
"Path not found" or "directory not found" Errors
"""
"""
****Note*******: "DATA_PATH = "./assets/input/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"" can be considered a configuration variable. It is used 
to store the path to a CSV file that contains data for the annual enterprise survey.By using a configuration variable, the path to the file can be easily changed if 
needed, without having to modify the code where it is used. This can make the code more modular and easier to maintain. Additionally, configuration variables can be 
used to store other values that may need to be changed in the future, such as API keys or database connection strings.
"""
"""
********Note********:People Try to use this "config" as a "yaml" files.This "config" file Generally,In real time Industry Most of the proples Uses as a "yaml" format
                     files.If need to change/import any "Dataset" Or anythings What we generally does in "config/yaml" files and We do 
                     changes in this file without changing our Original code.This "config" file acts as a "soft coded".
"""
#Here We are writing "Data path" For our "CSV File" it means where is our Csv file is located in which directory
#Here "DATA_PATH" is a config variable
#Here We can Modify our "DATA_PATH" Based on What dataset we need to perform Operations.Before changing we need to make sure our file is
#in "assets" folder under "input" folder.
DATA_PATH = "./assets/input/train.csv" #--> Here "./" represents our "Relative Path(src)" w.r.t Docker
NUMERIC_TYPES = ["int16","int32","int64","float16","float32","float64"]
OBJECT_TYPES = ["object"]


#Here "(no_examples*0.05)" is a Range or Categorical Threshold as we discussed it is "100" based on rows we can change it.
#Here actually we shouldn't write "Threshold" or "Range" as "(no_examples*0.05)" Bcs it's keeps on changing Based on the Dataset.So, we write this in "config.py".
#Here we can also change "0.05" based on the requirement into "0.25" or "0.1" etc.. Here "0.05" means "5%"
NOMINAL_THRESHOLD = (891*0.05)
