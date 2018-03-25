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
clf = tree.DecisionTreeClassifier(max_depth = 7, min_samples_split = 162)
clf.fit(data.values, target.values)
dot_data = tree.export_graphviz(clf, out_file = None, feature_names = list(data), class_names = ['0', '1'])
graph = graphviz.Source(dot_data)
graph.render('tree')
graph