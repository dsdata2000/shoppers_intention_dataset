def test():
    output_data = ('./output/top_cost_drug.txt','wb')
    x = [10, 20, 30]
    for i in range( len(x) ) :
        output_data.write('%s\n' % x[i])
    output_data.close()
test()
