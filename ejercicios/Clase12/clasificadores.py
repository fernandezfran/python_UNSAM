#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

k = 100 # number of repetitions
iris_dataset = load_iris()
knn_score, clf_score, rf_score = [], [], []

for i in range(k):

    # random choice of train and test data
    X_train, X_test, y_train, y_test = train_test_split(
            iris_dataset['data'], iris_dataset['target']
            )

    # fit of the methods
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    # score of the methods
    knn_score.append(knn.score(X_test, y_test))
    clf_score.append(clf.score(X_test, y_test))
    rf_score.append(rf.score(X_test, y_test))

print("Mean score (knn): {:.2f} +/- {:.2f}".format(np.mean(knn_score),
                                                   np.std(knn_score)))
print("Mean score (clf): {:.2f} +/- {:.2f}".format(np.mean(clf_score),
                                                   np.std(clf_score)))
print("Mean score  (rf): {:.2f} +/- {:.2f}".format(np.mean(rf_score),
                                                   np.std(rf_score)))
