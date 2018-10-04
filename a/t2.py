import fasttext

classifier = fasttext.supervised('label_random1.txt', 'random_model', label_prefix='__label__')
# classifier = fasttext.load_model('random_model.bin', label_prefix='__label__')

result = classifier.test('random_test.txt')

print(classifier.label_prefix)
print(classifier.labels)

print('P@1:', result.precision)
print('R@1:', result.recall)
print('Number of examples:', result.nexamples)

texts = ['www.naver.com', 'ad.google.co.kr']
labels = classifier.predict_proba(texts, k=2)
print(labels)

