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

X_train, X_test, y_train, y_test = train_test_split(data.values, target.values, test_size = 0.3)

sum1 = [0 for x in range(20)]
depth = 1
for i in range(10):
    X_train1, X_validate, y_train1, y_validate = train_test_split(X_train, y_train, test_size = 0.1)
    depth = 1
    for j in range(20):
        clf = tree.DecisionTreeClassifier(max_depth = depth)
        depth += 1
        clf.fit(X_train, y_train)
        y_p = clf.predict(X_test)
        sum1[j] += accuracy_score(y_test, y_p)

accuracy = list(map(lambda x: x/10.0, sum1))
for i in range(20):
	print("depth {} has accuracy {}: ".format(i+1, accuracy[i]))


'''

clf = tree.DecisionTreeClassifier(max_depth = 7)
clf.fit(data.values, target.values)
dot_data = tree.export_graphviz(clf, out_file = None, feature_names = list(data), class_names = ['0', '1'])
graph = graphviz.Source(dot_data)
graph.render('tree')
graph
'''