
import random

def main():
    f1 = open('../make_train.txt','r')

    f2 = open('../b/data1_final_t.txt', 'w')
    f3 = open('../b/data1_final_f.txt', 'w')

    fdata = f1.readlines()

    t = []
    f = []
    count_t = 0
    count_f = 0

    for i in fdata:
        if i[:10] == '__label__t':
            t.append(i)
            count_t += 1
        else:
            f.append(i)
            count_f += 1

    # shuffle
    random.shuffle(t)
    random.shuffle(f)

    for i in t:
        f2.write(i[:-1] + "\n")
    for i in f:
        f3.write(i[:-1] + "\n")

    print('T= ' + '%d' % count_t + ', F= ' + '%d' % count_f)

    nn = '%d' % (count_t / count_f + 1)
    print(nn)




if __name__ == '__main__':
  main()