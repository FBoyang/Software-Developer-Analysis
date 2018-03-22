from sklearn.svm import LinearSVC
import mglearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("FCC.csv")
#extract x value and y value
y_df = df.iloc[:, -1]
x_df = df.iloc[:, df.columns != 'IsSoftwareDev']

obj_df = x_df.select_dtypes(include=['object']).copy()
float_df = x_df.select_dtypes(exclude=['object']).copy()

n_obj_df = pd.DataFrame()

#convert obj type feature to one hot number
for i in range(obj_df.shape[1]):
    x_dummies = pd.get_dummies(obj_df.iloc[:, i].values)
    n_obj_df = pd.concat([x_dummies, n_obj_df], axis = 1)
    

x_value = pd.concat([n_obj_df, float_df], axis = 1).values 
y_value = y_df.values
#n_df = pd.concat(float_df, n_obj_df)




with open("value.txt" ,'w') as file:
    for item in x_value:
        for i in item:
            file.write("%d ,"% i)



logreg = LogisticRegression()
logreg.fit(x_value, y_value)
print("done")


'''
raw processing
'''
####################################

'''
do prediction
'''
# Get 2D array of data of other categories
df = pd.read_csv('FCC.csv')
colNames = list(df.columns)
colNames.remove('IsSoftwareDev')

X = []
for header in colNames:
    row = df[header].values.tolist()
    X.append(row)

# Get a list of software developers
sde = df.IsSoftwareDev.tolist()

# Training Data
linear_svm = LinearSVC().fit(X, sde)

mglearn.plots.plot_2d_separator(linear_svm, X)
mglearn.discrete_scatter(X[:, 0], X[:, 7], sde) # Modify column indexes here

plt.xlabel("Features")
plt.ylabel("Is Software Developer")


