import json
import pandas as pd
import math
import matplotlib.pyplot as plt
import os
import seaborn as sns


all_x = pd.read_csv('./move_dir/filtered_data/LSY_left_x_5_nor.csv')
all_y = pd.read_csv('./move_dir/filtered_data/LSY_left_y_5_nor.csv')
all_x2 = pd.read_csv('./move_dir/filtered_data/LSY_right_x_5_nor.csv')
all_y2 = pd.read_csv('./move_dir/filtered_data/LSY_right_y_5_nor.csv')

ptrn = [2, 18, 43, 62, 67, 80, 99, 121, 136, 152, 165]
ptrn2 = [0, 24, 43, 62, 79, 101, 115, 138, 151, 173, 186]

dist_avg = pd.DataFrame()
tmp_sum = pd.DataFrame()

for j in range(len(ptrn) - 1):
    count = 0
    tmp_sum = [0 for _ in range(0, 68)]
    for i in range(ptrn[j], ptrn[j + 1]):
        count += 1
        dist = [0 for _ in range(0, 68)]
        for k in range(0, 68):
            dist[k] = math.sqrt(((all_x[str(k)][i] - all_x[str(k)][i + 1]) ** 2) + \
                                ((all_y[str(k)][i] - all_y[str(k)][i + 1]) ** 2))
            tmp_sum[k] += dist[k]
    for q in range(0, 68):
        tmp_sum[q] = tmp_sum[q] / count
    dist_avg = pd.concat([dist_avg, pd.DataFrame(tmp_sum).T])

dist_avg = dist_avg.reset_index(drop=True)
dist_avg_t = dist_avg.T



dist_avg2 = pd.DataFrame()
tmp_sum2 = pd.DataFrame()

for j in range(len(ptrn2) - 1):
    count = 0
    tmp_sum2 = [0 for _ in range(0, 68)]
    for i in range(ptrn2[j], ptrn2[j + 1]):
        print("i is " + str(i))
        count += 1
        dist = [0 for _ in range(0, 68)]
        for k in range(0, 68):
            dist[k] = math.sqrt(((all_x2[str(k)][i] - all_x2[str(k)][i + 1]) ** 2) + \
                                ((all_y2[str(k)][i] - all_y2[str(k)][i + 1]) ** 2))
            print("dist[" + str(k) + "] is" + str(dist[k]))
            tmp_sum2[k] += dist[k]

    for q in range(0, 68):
        tmp_sum2[q] = tmp_sum2[q] / count

    print("----------------tmp_sum----------------")
    print(tmp_sum2)
    dist_avg2 = pd.concat([dist_avg2, pd.DataFrame(tmp_sum2).T])

dist_avg2 = dist_avg2.reset_index(drop=True)
dist_avg2_t = dist_avg2.T
print(dist_avg2)

plt.figure(figsize=(16, 9))
plt.subplot(211)
sns.boxplot(data=dist_avg)
# plt.title("average movement boxplot")
plt.xlabel("landmark num")
plt.ylabel("movement")

plt.subplot(212)
sns.boxplot(data=dist_avg2)
plt.title("average movement boxplot")
plt.xlabel("landmark num")
plt.ylabel("movement")
plt.show()

plt.show()


