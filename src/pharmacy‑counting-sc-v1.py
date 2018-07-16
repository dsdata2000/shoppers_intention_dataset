   
# N_of_data_entry  = 24525860 (NODE)
NODE = int(round(5))
N_unit_test = 3
N_start = int(round(0))   #  24525860/2, 24520000
N = N_start + N_unit_test

def index_list(list1,sorted_list):
    #print len(list1), len(sorted_list)
    index = []
    for i in range(len(sorted_list)) :
        ind = list1.index(sorted_list[i])
        index.append(ind)
    return index

def count_frequency( list1, item1 ) :
    s = 0
    for i in range(len(list1)) :
        if item1 == list1[i] :
            s += 1
    return s

def pharmacy_counting():
    # step 1 :
    data_c_dn_fn_ln = []  # list for cost-drug name - first name - last name
    cost_data = []
    data = open('./input/itcont.txt','r')
    for i in range(NODE) :
        line = data.readline()
        lins_sp = line.split(',')
        cost_data.append(lins_sp[4])
        data_c_dn_fn_ln.append(line)  # checked for all records
    data.close()
    data_c_dn_fn_ln.pop(0)
    cost_data.pop(0)
    #print data_c_dn_fn_ln[24525860-2]

    # since the input data set is large with 24 million entries, so unit test
    # can be carried on by choosing a smaller unit say 5000 entries by picking
    # then from the start, end, in the middle or anywhere from the 24 million
    # entries

    # N_unit_test = 500
    # N_start = int(round(24525/2))
    # N = N_start + N_unit_test

    # step 2:
    data_c_dn_fn_ln_unit = data_c_dn_fn_ln[N_start:N] # data_c_dn_fn_ln list for smaller unit
    cost_data_unit = cost_data[N_start:N]
    #print data_c_dn_fn_ln_unit[0:2]

    # since ids are not used for this analysis, hence ids need to be removed
    # from data_c_dn_fn_ln data and named as data_c_dn_fn_ln_v1

    # step 3 : 
    cost = []
    drug_name = []
    #prescriber_name_lf = []
    data_c_dn_fn_ln_unit_v1 = []
    for i in range(len(data_c_dn_fn_ln_unit)) :
        entry_split = data_c_dn_fn_ln_unit[i].split(',')
        cost.append(entry_split[4])
        drug_name.append(entry_split[3])
        #prescriber_name_lf.append( [entry_split[1], entry_split[2]] )
        data_c_dn_fn_ln_unit_v1.append( [[entry_split[1], entry_split[2]],entry_split[3] ])

    #print data_c_dn_fn_ln_unit_v1[0:5]


    # cost[] contains the cost list of all drugs for the unit. Now top_cost[]
    # need to be sorted for all the drugs in descending order along with their
    # indices so that corresponding drug_name can be identified, as well as
    # number of times a drug was prescribed for the same prescriber.

    
    pharmacy_counting()

    
