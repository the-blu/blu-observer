f=open('data5.txt','r')
f2=open('1.txt','w')
fdata = f.readlines()


for i in fdata:
    f2.write("['" + i[9:10] + "']" + ', ')


