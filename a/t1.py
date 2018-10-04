import fasttext

classifier = fasttext.supervised('data_train.txt', 'data_model', label_prefix='__label__')
result = classifier.test('test.txt')
print('P@1:', result.precision)
print('R@1:', result.recall)
print('Number of examples:', result.nexamples)

texts = ['greet Good Day', 'Good Morning. Did you have break-fast ?']
labels = classifier.predict_proba(texts, k=2)
print(labels)

