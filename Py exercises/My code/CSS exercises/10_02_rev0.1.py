# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:19:57 2018

@author: User
"""




def getData(infile, outfile, minline, maxline):
        with open(infile) as afile:
            readfile = afile.read()
            readfile = readfile.split('\n')
            readfile = readfile[1:]
            readfile = readfile[:-1]
#            lenof = (len(readfile) )
            lol = []
#            lol = [ [0]*5 for j in range(lenof) ]
#            print(lol)
            for line in readfile:
                stringof = line.split(',')
                lol.append(stringof)
#            print(lol)
#            sortedlol = sorted(lol, key = lambda x: int(x[0]))
#            print(sortedlol)
            filtlol = list(filter(lambda x: minline<=int(x[0])<=maxline,lol ) )
            filtlol.insert(0, ['ref', 'state', 'city', 'dateof', 'datein'])
            print((filtlol) )
        otherfile = open(outfile, "w")
        for each in filtlol:
            out = ''.join(each)
            otherfile.write(out )
        otherfile.close()


getData("samplenew.txt", "newfile.txt", 5, 10)






# using enumerate to print lines between certain numbers
#while True :
#           readfile = afile.read()
#           for num, line in enumerate(readfile.split('\n')):
#                    if num in range(minline, maxline+1):
#                        print(num, line)
#                    else:
#                        pass
#                if ("" == line):
##                    print ("file finished")
#                    break;