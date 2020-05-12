import os
#import operator
from operator import itemgetter

file1=open('/home/pandeyao/directedGraph/part-r-00000')

d={}
d2={}

for line in file1:
    words=line.split()
    if len(words)!=0:
        #print(words)
        s=str(words[1])
        #print(words[0])
        s2=words[0]
        #print(s2)
        my_list=s.split('#')
        #print(my_list)
        s1=my_list[1]
        #count=my_list[1]
        d.update({s2:int(s1)})
        d2.update({my_list[2]:my_list[0]})


#print(d)
my_list1=sorted(d.items(), key=itemgetter(1))
#print('Sorted List:',my_list1)

path2 = '/home/pandeyao/directedGraph/output.txt'
f = open(path2,'a')

f.write("\nNode with Minimum connectivity is" + " "+ str(my_list1[0][0]) + " " + "and the count is"+ " " +str(my_list1[0][1]))
f.write("\nNode with Maximum Connectivity is"+ " "+str(my_list1[-1][0])+" " +"and the count is"+ " "+str(my_list1[-1][1]))
#print('Node with Minimum connectivity is',str(my_list1[0][0]),'which is',my_list1[0][1])
#print('Node with Maximum Connectivity is',str(my_list1[-1][0]),'which is',my_list1[-1][1])
#print(d2)

for k,v in d2.items():
    if k == my_list1[-1][0]:
       # print('The Longest Adj List is:-',v ,'for Node', k)
        #print('The Longest Adj List is:-' + ' ' +str(v) + ' ' +'for Node'+ ' ' +str(k))
        f.write("\nThe Longest Adj List is:" + "{ " +str(v) + " }" +"for Node -"+ " " +str(k))

f.write("\n\n.....................................................................................................\n")
