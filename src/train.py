#!/usr/bin/env python
# coding=utf8

from sklearn import svm
from numpy import *
from sklearn.model_selection import *
import numpy as np

if __name__ == '__main__':
    data = np.loadtxt('train_data_len17', dtype=float, delimiter=',')
    x, y = np.split(data, (17,), axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)
    #clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
    clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
    clf.fit(x_train, y_train.ravel())
    print clf.score(x_train, y_train)
    y_hat = clf.predict(x_train)
    print clf.score(x_test, y_test)
    y_hat = clf.predict(x_test)
