exe = ['.jpg','.png','.css','.JPG','?jpg','?png','?css','?JPG','woff','off2','jpeg','JPEG','PNG']


f1 = open('./url-dataset/ko/data3_3.txt','r')
f2 = open('./url-dataset/ko/data4_1.txt','w') #edit

fdata = f1.readlines()
# f1.seek(0)
# f1.truncate()

# f = open('data1_2.txt', 'r') #label1
# f2 = open('data2.txt', 'w')

for i in fdata:

    # print(i[-5:-1])
    if i[-5:-1] not in exe:
        f2.write(i)


f1.close()
f2.close()