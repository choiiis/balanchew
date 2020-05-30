import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

right_dict_list = []
left_dict_list = []

with open("left_4(sis).json", "r") as f:
    lines = f.readlines()
    lcount = 0
    for line in lines:
        left_data = json.loads(line)
        # count : line num
        print(lcount)
        lcount += 1
        left_dict_list.append(left_data)

with open("right_4(sis).json", "r") as f:
    lines = f.readlines()
    rcount = 0
    for line in lines:
        right_data = json.loads(line)
        # count : line num
        print(rcount)
        rcount += 1
        right_dict_list.append(right_data)


landmark_info = []

for i in range(0,lcount):
    for j in range(0, 68):
        landmark_info.append([j, left_dict_list[i][str(j)][0], 'x', 'left'])
        landmark_info.append([j, left_dict_list[i][str(j)][1], 'y', 'left'])

for i in range(0,rcount):
    for j in range(0, 68):
        landmark_info.append([j, right_dict_list[i][str(j)][0], 'x', 'right'])
        landmark_info.append([j, right_dict_list[i][str(j)][1], 'y', 'right'])

landmark_df = pd.DataFrame(landmark_info, columns=['id', 'value', 'XY', 'LR'])
print(landmark_df)
landmark_df_x = landmark_df.loc[landmark_df["XY"] == "x"]
landmark_df_y = landmark_df.loc[landmark_df["XY"] == "y"]

plt.figure(figsize=(8,6))
sns.boxplot(x="id", y="value", hue="LR", data=landmark_df_x)
# sns.swarmplot(x="id", y="value", hue="LR", data=landmark_df_x, size = 1)

plt.xlabel('face landmarks')
plt.ylabel('coordinates')

plt.title('Landmarks analysis - Y')
plt.legend(loc='upper right')
plt.show()
