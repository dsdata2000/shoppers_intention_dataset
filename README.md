# Contents 
1. [Introduction](README.md#Intro)
2. [Input Sample Cleaning](README.md#cleaning)
3.[Additional Subroutines](README.md#sub)
4. [Solution Approach](README.md#solapp)
5. [Unit Test ](README.md#unit-test )
6. [Full Functionality Test ](README.md#FFT)

# Introduction 
Input data set contains information on prescription drug prescribed by healthcare providers. It contains id, prescriber last and first name, drug name and cost as comma separated items.

# Additional Subroutines
I used two additional subroutines and they are following :
index_list : For a given sub-set of data this subroutine returns the indices from the original data set. 
count_frequency : For a given number, it returns the number of times that number repeats in a given data set. 

# Solution Approach 
./src/pharmacy‑counting-v3.py defines some global variables for running the test since the original input file contains roughly 24 million data points. NODE (number of data entry) variable allows to choose a subset of the input data that would be used for analysis. NOD allows us to choose any percentile of the data say 50%, 10% or 1% of the input data for analysis. 

N_unit_test is another global variable that we can vary to sort out number of top cost drugs that we want to generate for the output. N_unit_test pick a subset of the data for analysis and this subset can be chosen anywhere from the original set. It allows us to choose first N data entry, last N data entry or N data points anywhere from the selected data set; so that we can quickly analyze a subset of the data from any part of the original input data set. 

The main subroutine used for analysis named pharmacy_counting collects all column such as id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost of the txt data in data_c_dn_fn_ln and cost_data collects only the drug cost. Here the header of each column has been deleted.  

In step 2, L46; a subset of the above data was choosen for analysis of various units of the original data set. 

In step 3, L  
 
# Unit Test 
Since the input data set contains over 24 million records from which a list of all drugs be generated as per their cost in descending order along with the number of times the same drug was prescribed by unique individual identified with the same last and first name.   

# Full Functionality Test



