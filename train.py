from __future__ import print_function
import fileinput
from glob import glob
import sys

from seqlearn.datasets import load_conll
# from seqlearn.evaluation import bio_f_score
from seqlearn.perceptron import StructuredPerceptron
from sklearn.metrics import accuracy_score


def features(sentence, i):
    word = sentence[i]
    yield "word:{}" + word.lower()
    if word[0].isupper():
        yield "CAP"
    if i > 0:
        yield "word-1:{}" + sentence[i - 1].lower()
        if i > 1:
            yield "word-2:{}" + sentence[i - 2].lower()
    if i + 1 < len(sentence):
        yield "word+1:{}" + sentence[i + 1].lower()
        if i + 2 < len(sentence):
            yield "word+2:{}" + sentence[i + 2].lower()


def describe(X, lengths):
    print("{0} sequences, {1} tokens.".format(len(lengths), X.shape[0]))


def load_data():
    file = glob('data/sample.log')

    # 80% training, 20% test
    print("Loading training data...", end=" ")
    # train_files = [f for i, f in enumerate(files) if i % 5 != 0]
    train = load_conll(fileinput.input(file), features)
    print(train)
    X_train, _, lengths_train = train
    describe(X_train, lengths_train)

    print("Loading test data...", end=" ")
    # test_files = [f for i, f in enumerate(files) if i % 5 == 0]
    test = load_conll(fileinput.input(file), features)
    X_test, _, lengths_test = test
    describe(X_test, lengths_test)

    return train, test


if __name__ == "__main__":
    print(__doc__)
    train, test = load_data()
    X_train, y_train, lengths_train = train
    X_test, y_test, lengths_test = test

    clf = StructuredPerceptron(verbose=True, max_iter=1)
    print("Training %s" % clf)
    clf.fit(X_train, y_train, lengths_train)

    y_pred = clf.predict(X_test, lengths_test)
    print("Accuracy: %.3f" % (100 * accuracy_score(y_test, y_pred)))
    # print("CoNLL F1: %.3f" % (100 * bio_f_score(y_test, y_pred)))