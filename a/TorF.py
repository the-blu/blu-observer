import random
import os
import fasttext
f = open('./test-result/vi/result1-5.txt', 'w') #edit

def train(fname):

    classifier = fasttext.supervised('../b/train.txt', '../b/random_model',label_prefix='__label__')  # ,lr=0.1, epoch=10
    # classifier = fasttext.load_model('random_model.bin', label_prefix='__label__')
    result = classifier.test('../b/test.txt')

    precison = 'P@1: ' + '%s' % result.precision
    recall = 'R@1: ' + '%s' % result.recall
    num_ex = 'Number of examples: ' + '%s' % result.nexamples
    f.write(fname + '\n' + precison + '\n' + recall + '\n' + num_ex + '\n')

    # texts = ['m.kbcard.com/cxh/js/mblhomeIa/lib/cxhia.js?201711161558', 'pagead2.googlesyndication.com/pagead/js/r20181001/r20180604/show_ads_impl.js', 'compass.adop.cc/RD/dea00a01-c096-459b-b57f-5ea292222e38', 'common.like.naver.com/css/likeItButton_TVCAST.css?20140326', 'page.kakao.com/static/common/icon_trace_off.png?509ba8ff2e3abf181e390f7f8f84cb0b']
    # texts = ['m.kbcard.com/cxh/js/mblhomeIa/lib/cxhia.js?', 'pagead.googlesyndication.com/pagead/js/r/r/show_ads_impl.js', 'compass.adop.cc/RD/deaa-c-b-bf-eae', 'common.like.naver.com/css/likeItButton_TVCAST.css?', 'page.kakao.com/static/common/icon_trace_off.png?baffeabfefffcbb']

    vi = []
    fvi = open('./url-dataset/vi/data5.txt', 'r')
    fvidata = fvi.readlines()
    for i in fvidata:
        vi.append(i[11:])


    labels = classifier.predict(vi, k=1)
    f.write('%s'%labels + '\n'*3)

def get_dataset(ht, hf, tt, tf, file):
    os.system('head -n %d ../b/data1_final_t.txt > ../b/train.txt'%ht)
    os.system("head -n %d ../b/data1_final_f.txt > cat>> ../b/train.txt"%hf)
    os.system("tail -n %d ../b/data1_final_t.txt > ../b/test.txt"%tt)
    os.system("tail -n %d ../b/data1_final_f.txt > cat>> ../b/test.txt"%tf)

    train(file)


def main():
    f1 = open('./url-dataset/ko/data4_1.txt', 'r') #edit
    f2 = open('../b/data1_final_t.txt', 'w')
    f3 = open('../b/data1_final_f.txt', 'w')

    fdata = f1.readlines()

    t = []
    f = []
    count_t = 0
    count_f = 0

    for i in fdata:
        if i[:10] == '__label__T':
            t.append(i)
            count_t += 1
        else:
            f.append(i)
            count_f += 1

    #shuffle
    random.shuffle(t)
    random.shuffle(f)

    for i in t:
        f2.write(i[:-1]+"\n")
    for i in f:
        f3.write(i[:-1]+"\n")


    print('T= '+ '%d'%count_t +', F= ' + '%d'%count_f)

    nn = '%d'%(count_t/count_f +1)
    print(nn)

    for i in range(1,int(nn)):
        count_t = count_f*i
        print('\n')
        tf_ratio = '%d'%i + ':1'
        print('(', tf_ratio,')')
        print('T:F = ', count_t, ':', count_f)
        print('train: test = ')
        for j in range(1,10):
            head_t = count_t / (j + 1) * j
            tail_t = count_t / (j + 1)
            head_f = count_f / (j + 1) * j
            tail_f = count_f / (j + 1)
            print('%d'%j + ':1 = ' + '%d'%head_t + ':' + '%d'%tail_t + ' = ' + '%d'%head_f + ':' + '%d'%tail_f)
            test_train_ratio = '%d'%j + ':1'
            # print(test_train_ratio)

            file = tf_ratio + '/' + test_train_ratio
            # print(file)
            get_dataset(head_t, head_f, tail_t, tail_f, file)


if __name__ == '__main__':
  main()






