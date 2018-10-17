from collections import OrderedDict

def main():
    f1 = open('../make_train.txt','r+')
    fdata = f1.readlines()
    f1.seek(0)
    f1.truncate()

    temp = []
    for i in fdata:
        temp.append(i)

    temp = list(OrderedDict.fromkeys(temp))

    for n in temp:
        f1.write(n)

    f1.close()




if __name__ == '__main__':
  main()