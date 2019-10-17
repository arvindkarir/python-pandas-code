# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:30:43 2018

@author: User
"""

def filterby_rt(infile, outfile, n1, n2):
    f = open(infile, 'r')
    raw_data = f.readlines()
    f.close()
    data_list = []
    for each in raw_data:
        data_list.append(each.strip('\n'))
    header = data_list[0]
#    print(len(data_list))
    # if len of data_list ==1, then write can happen right away. Write will be a helper function. Else
    data_dict = {}
    for item in data_list[1:]:
        if item[0] in data_dict.keys():
            data_dict[item[0]].append([(item[1:].strip(',').split(','))])
        else:
            data_dict[item[0]] = [item[1:].strip(',').split(',')]
#    newlist = [ value  for key,value in data_dict.items() if int(key) >= n1 and int(key) <= n2 ] # just for fun
#    print(newlist)

    with open(outfile, 'w') as fo:
        fo.write('\t'.join(header.split(',')) + '\n\n')
        for k, v in (data_dict.items()):
            for each in v:
                if int(k) >= n1 and int(k) <= n2:
                    fo.write(str(k) + '\t' + str(each).strip('[],') + '\n\n')
        f.close()


filterby_rt('samplenew.txt', 'alternatenew.txt', 6,10)