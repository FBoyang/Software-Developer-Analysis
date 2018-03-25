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

feature_importance = pd.Series(clf.feature_importances_, index = data.columns)
feature_importance = feature_importance.sort_values(ascending = False)

diction = {}
feature_key = feature_importance.keys()
for item, key in zip(feature_importance, feature_key):
    if item > 0.01:
        diction[key] = item


diction = pd.Series(diction).sort_values()
print(diction)
diction.plot(kind = 'barh', figsize = (7,6), title = "feature_importance")
plt.tight_layout()
plt.show()
