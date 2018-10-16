import json
from collections import OrderedDict

f = open("data2.txt", "w")

def rm_dup():
    f1 = open('data2.txt','r+')
    fdata = f1.readlines()
    f1.truncate(0)
    temp = []
    for i in fdata:
        temp.append(i)

    temp = list(OrderedDict.fromkeys(temp))

    for n in temp:
        f1.write(n)

    f1.close()

def sum(label, li):

    for reqs in li:
        #check empty
        if not reqs:
            pass
        else:
            for sub in reqs:
                # print(sub.get('sub_domain'))
                url = label + sub.get('sub_domain')
            # print(reqs)
                f.write(url + '\n')



def main():
    with open('../dataset.json') as data_file:
        data = json.load(data_file)

    label_t = []
    label_f = []

    query = []

    for i in data:
        label_f.append(i['label_f'])
        label_t.append(i['label_t'])

    sum("__label__F ", label_f)
    sum("__label__T ", label_t)
    f.close()

    rm_dup()


if __name__ == '__main__':
  main()