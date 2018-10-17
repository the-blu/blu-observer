import json
from collections import OrderedDict

# f = open("data1.txt", "w") #edit
f = open("./url-dataset/ko/data6.txt", "w") #edit


def rm_dup():
    # f1 = open('data1.txt','r+') #edit
    f1 = open('./url-dataset/ko/data6.txt','r+') #edit

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

def sum(label, li):

    for reqs in li:
        #check empty
        if not reqs:
            pass
        else:
            for sub in reqs:
                if sub.get('path') is '/':
                    # print(k)
                    if not sub.get('query_string'):
                        url1 = (sub.get('sub_domain') + '?')
                        # print(url1)
                    else:
                        url1 = (sub.get('sub_domain') + sub.get('path') + '?')
                        # print(url1)
                else:
                    url1 = (sub.get('sub_domain')+sub.get('path')+'?')
                # print(url1)
                query = sub.get('query_string')
                # print(query)
                for q in query:
                    n = q.get('name')
                    val = q.get('value')

                    url1 = url1 + n + '&'

                    # if not val:
                    #     url1 = url1 + n + '&'
                    # elif 'TagError: adsbygoogle.push()' in val:
                    #     pass
                    # elif '\n' in val:
                    #     url1 = url1 + (n + '=' + val.replace('\n','')) + '&'
                    # else:
                    #     url1 = url1 + (n+'='+val) + '&'

                url1 = label + url1 #__label__

                f.write(url1[:-1] + '\n')




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

    #deduplication
    rm_dup()


if __name__ == '__main__':
  main()