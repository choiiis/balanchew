import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# xlist_total = pd.DataFrame()
# ylist_total = pd.DataFrame()
#
# with open("test.json", "r") as f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         count += 1
#         data = json.loads(line)
#         df = pd.DataFrame.from_dict(data, orient='index').T
#
#         xlist = df.loc[0]
#         xlist_df = pd.DataFrame(xlist).T
#         ylist = df.loc[1]
#         ylist_df = pd.DataFrame(ylist).T
#
#         xlist_total = pd.concat([xlist_total, xlist])
#         ylist_total = pd.concat([ylist_total, ylist])
#
#
# xlist_total.rename(columns={0: 'value'}, inplace=True)
# ylist_total.rename(columns={0: 'value'}, inplace=True)
#
# xlist_total["axis"] = 'x'
# ylist_total["axis"] = 'y'
#
# xlist_total = xlist_total.reset_index()
# ylist_total = ylist_total.reset_index()
#
# xlist_total['index'] = xlist_total['index'].astype(int)
# ylist_total['index'] = ylist_total['index'].astype(int)
#
# print(xlist_total)
# print('---------------')
# print(ylist_total)
#
# list_total = pd.concat([xlist_total, ylist_total])
# list_total['label'] = 'left'
# # list_total = list_total.reset_index()
# print(list_total)
#
#
# plt.figure(figsize=(8,6))
# sns.boxplot(x='index', y='value', data=ylist_total)
# sns.swarmplot(x="index", y="value", data=ylist_total, size = 1)
#
# plt.xlabel('face landmarks')
# plt.ylabel('value')
#
# plt.title('Landmarks analysis - Y')
# plt.legend(loc='upper right')
# plt.show()







xfile = pd.read_csv("normalized_x.csv")
yfile = pd.read_csv("normalized_y.csv")
xlist = pd.DataFrame()
ylist = pd.DataFrame()

for i in range(len(xfile)):
    df = pd.DataFrame(xfile.loc[i])
    df.rename(columns={i: 'value'}, inplace=True)
    xlist = pd.concat([xlist, df], axis=0)

for i in range(len(yfile)):
    df = pd.DataFrame(yfile.loc[i])
    df.rename(columns={i: 'value'}, inplace=True)
    ylist = pd.concat([ylist, df], axis=0)


xlist["axis"] = 'x'
ylist["axis"] = 'y'
xlist = xlist.reset_index()
ylist = ylist.reset_index()

xlist['index'] = xlist['index'].astype(int)
ylist['index'] = ylist['index'].astype(int)

print(xlist)
print('-----------------------------')
print(ylist)

list_total = pd.concat([xlist, ylist])
list_total['label'] = 'left'
list_total = list_total.reset_index()
print(list_total)


plt.figure(figsize=(8,6))
sns.boxplot(x='index', y='value', data=ylist)
sns.swarmplot(x="index", y="value", data=ylist, size = 1)

plt.xlabel('face landmarks')
plt.ylabel('value')

plt.title('Landmarks analysis - Y')
plt.legend(loc='upper right')
plt.show()