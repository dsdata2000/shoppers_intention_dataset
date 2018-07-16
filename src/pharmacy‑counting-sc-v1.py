
# NODE => N_of_data_entry; 500000
NODE = int(round(10))
N_unit_test = 5
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
    data_c_dn_fn_ln = []
    cost_data = []
    idx = []
    data_input = open('./input/itcont.txt','r')
    for i in range(NODE) :  # 24525860
        line = data_input.readline()
        cs = line[4]
        print cs 
          
pharmacy_counting()
