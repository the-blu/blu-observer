import re


def main():
    # f1 = open('./url-dataset/data1.txt', 'r+')  # edit
    #
    # fdata = f1.readlines()
    # f1.seek(0)
    # f1.truncate()

    f1 = open('./url-dataset/vi/data3.txt', 'r')
    # f2 = open('data1.txt', 'r')
    f3 = open('./url-dataset/vi/data4.txt','w')

    fdata = f1.readlines()
    # fdata2 = f2.readlines()

    for i in fdata:
        # print i[:-1]
        new_url = re.sub('(www.)?', '', i) #\d

        # new_url = re.sub('https?://(www.)?', '', i) #\d
        # new_url = re.sub('https?://', '', i)
        # print new_url[:-1]

        new_url = re.sub('[0-9]', '', i)

        # url = re.compile(r"https?//")
        # i = re.findall(r'(https?://)',i)
        # i = i.replace(url, "")
        # url.sub('', i).strip().strip('/')
        # i = i.replace("http://", "")
        # print new_url[:-1]


        # new_url2 = re.sub('[-=#:$%&]', '', new_url)  #-=.#/?:$%&
        # print new_url2

        f3.write(new_url)

        # break


    f1.close()
    f3.close()

if __name__ == '__main__':
    main()