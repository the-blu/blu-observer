import fasttext

f = open('r1.txt', 'w')

classifier = fasttext.supervised('../b/train.txt', '../b/random_model', label_prefix='__label__') #,lr=0.1, epoch=10, lr=0.1, epoch=40
# classifier = fasttext.load_model('../b/random_model.bin', label_prefix='__label__')

result = classifier.test('../b/test.txt')

print(classifier.label_prefix)
print(classifier.labels)
#
# precison = 'P@1: ' + '%s'%result.precision
# recall = 'R@1: ' + '%s'%result.recall
# num_ex = 'Number of examples: ' + '%s'%result.nexamples
# f.write(precison + '\n' + recall + '\n'+ num_ex)
# print(precison)

print('P@1: ', result.precision)
print('R@1: ', result.recall)
print('Number of examples:', result.nexamples)

# texts = ['m.kbcard.com/cxh/js/mblhomeIa/lib/cxhia.js?201711161558\n', 'googlead.co.kr\n']


f_vn = open('./url-dataset/vi/data1.txt', 'r')
fdata = f_vn.readlines()
texts = []
for i in fdata:
    texts.append(i)

labels = classifier.predict_proba(texts, k=1)
for n in labels:

    f.write('%s'%n+ '\n' )
#
print(labels)
# for i in fdata:
#     labels = classifier.predict_proba(i, k=1)
#     f.write(i + '\n')
#     f.write('%s'%labels + '\n' * 3)
#     # print(labels)


# text1 = ['naver.com']
# text2 = ['adsevice.google.co.kr']
# labels = classifier.predict_proba(texts, k=1)
# label1 = classifier.predict_proba(text1, k=1)
# label2 = classifier.predict_proba(text2, k=1)



