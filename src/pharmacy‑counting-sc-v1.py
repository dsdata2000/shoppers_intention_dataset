def test():
    output_data = ('./output/top_cost_drug.txt','wb')
    x = [10, 20, 30]
    for i in range( len(x) ) :
        cs = str(x[i])
        print cs 
        output_data.write('%s\n' % cs )
    output_data.close()
test()
