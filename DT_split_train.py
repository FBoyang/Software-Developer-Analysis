import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import graphviz

df = pd.read_csv("one_hot.csv")

target = df.iloc[: , 0]
data = df.iloc[:, df.columns != 'IsSoftwareDev']



sum1 = [0 for x in range(20)]
split = 2
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(data.values, target.values, test_size = 0.2)
    split = 2
    for j in range(20):
        clf = tree.DecisionTreeClassifier(max_depth = 7, min_samples_split = split)
        split += 10
        clf.fit(X_train, y_train)
        y_p = clf.predict(X_test)
        sum1[j] += accuracy_score(y_test, y_p)

accuracy = list(map(lambda x: x/100.0, sum1))
for i in range(20):
	print("min_split {} has accuracy {}: ".format(i*10 + 2, accuracy[i]))