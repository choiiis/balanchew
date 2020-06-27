from matplotlib import pyplot
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification, make_regression
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# left_train_mov = pd.read_csv("./move_dir/vector_data/left_x_train2.csv")
# left_mov_test = pd.read_csv("./move_dir/vector_data/CJL_left_x.csv")
# right_train_mov = pd.read_csv("./move_dir/vector_data/right_x_train2.csv")
# right_mov_test = pd.read_csv("./move_dir/vector_data/CJL_right_x.csv")
#
# left_train_mov['pos'] = 'left'
# right_train_mov['pos'] = 'right'
# left_mov_test['pos'] = 'left'
# right_mov_test['pos'] ='right'
#
# train_mov = pd.concat([left_train_mov, right_train_mov])
# train_mov = train_mov.reset_index(drop=True)
# test_mov = pd.concat([left_mov_test, right_mov_test])
# test_mov = test_mov.reset_index(drop=True)
#
#
#
# train_mov.loc[train_mov.pos=='left', 'pos'] = 0
# train_mov.loc[train_mov.pos=='right', 'pos'] = 1
# test_mov.loc[test_mov.pos=='left', 'pos'] = 0
# test_mov.loc[test_mov.pos=='right', 'pos'] = 1
# train_mov = train_mov.astype({'pos':'int'})
# test_mov = test_mov.astype({'pos':'int'})


left_mov = pd.read_csv('./move_dir/vector_data/left_x.csv')
right_mov = pd.read_csv('./move_dir/vector_data/right_x.csv')
left_mov['pos'] = 'left'
right_mov['pos'] = 'right'
mov = pd.concat([left_mov, right_mov])
mov = mov.reset_index(drop=True)

mov.loc[mov.pos=='left', 'pos'] = 0
mov.loc[mov.pos=='right', 'pos'] = 1
mov = mov.astype({'pos':'int'})

print(mov['16'].head(50))

select = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
          '11', '12', '13', '14', '15', '16', '48', '49', '50',\
          '51', '52', '53', '54', '55', '56', '57', '58', '59', \
          '60', '61', '62', '63', '64', '65', '66', '67']

# select = ['3', '4', '5', '6', '7', '8', '9', '10', \
#           '11', '12', '13', '48', '49', '50',\
#           '51', '52', '53', '54', '55', '56', '57', '58', '59', \
#           '60', '61', '62', '63', '64', '65', '66', '67']


data = mov.loc[:,select]
target = mov["pos"]
cor = data.corr()
print(data.corr())
cor = pd.DataFrame(cor)

# training_data = train_mov.loc[:,select]
# training_labels = train_mov["pos"]
# validation_data = test_mov.loc[:,select]
# validation_labels = train_mov["pos"]

# cor = training_data.corr()
# print(training_data.corr())
cor = pd.DataFrame(cor)

cor.to_csv('correlation.csv')
print(cor[['58', '54', '14', '2', '9']])

# plt.figure(figsize=(30,30))
# sns.heatmap(data = data.corr(), annot=True,fmt = '.2f', linewidths=.5, cmap='Blues')
# sns.heatmap(data = data.corr(), linewidths=.9, cmap='Blues')
# plt.show()

training_data, validation_data , training_labels, validation_labels = \
    train_test_split(data, target, stratify=target, random_state=0)





n_feature = 37
index = np.arange(n_feature)
forest = RandomForestClassifier(n_estimators=100, n_jobs=-1)
forest.fit(training_data, training_labels)

plt.barh(index, forest.feature_importances_, align='center')
plt.yticks(index, select)
plt.ylim(-1, n_feature)
plt.xlabel('feature importance', size=15)
plt.ylabel('feature', size=15)
plt.show()
#
#
#
# forest = ExtraTreesClassifier(n_estimators=250, random_state=0)
# forest.fit(training_data, training_labels)
#
# importances = forest.feature_importances_
# std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
# indices = np.argsort(importances)[::-1]
#
# #62
# n_feature = 37
# plt.bar(range(training_data.shape[1]), importances[indices],
#         color="r", yerr=std[indices], align="center")
# plt.xticks(range(training_data.shape[1]), indices)
# plt.xlim([-1, training_data.shape[1]])
# plt.show()
