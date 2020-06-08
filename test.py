# 얼굴 크기 normalize 한 상태
# 얼굴 크기/ 위치에 따라 길이 차이 없는지 확인

import json
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

x = pd.DataFrame()
y = pd.DataFrame()
vis_df = []
vis_dfn = []
vis_df2 = []
vis_df2n = []
vis_df3 = []
vis_df3n = []

with open("left_all.json", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
        # print(count)
        data = json.loads(line)
        df = pd.DataFrame.from_dict(data, orient='index').T

        # 0은 x, 1은 y. json 1줄 읽어서 x만 따로 xlist_df, y만 따로 ylist_df
        xlist = df.loc[0]
        xlist_df = pd.DataFrame(xlist).T
        ylist = df.loc[1]
        ylist_df = pd.DataFrame(ylist).T

        # 정규화 후 가로 세로 길이
        xdist = xlist[xlist.idxmax(axis=1)] - xlist[xlist.idxmin(axis=1)]
        ydist = ylist[ylist.idxmax(axis=1)] - ylist[ylist.idxmin(axis=1)]

        # print("[x, y] : [" + str(xdist) + ", " + str(ydist) + "] -- normarlized --> " + \
        #       "[x, y] : [" + str(xdist * (100 / xdist)) + ", " + str(ydist * (100 / xdist)) + "]")


        #정규화된 x를 normalized_x에 저장
        normalized_x = (xlist - xlist[xlist.idxmin(axis=1)]) * (100 / xdist)
        normalized_y = (ylist - ylist[ylist.idxmin(axis=1)]) * (100 / xdist)


        for i in range(6, 7):
            print("--------[" + str(i) + "]--------")
            dist = math.sqrt(((xlist[i] - xlist[30]) ** 2) + \
                             ((ylist[i] - ylist[30]) ** 2))
            dist_n = math.sqrt(((normalized_x[i] - normalized_x[30]) ** 2) + \
                               ((normalized_y[i] - normalized_y[30]) ** 2))


            print("point : (" + str(xlist[i]) + ", " + str(ylist[i]) + \
                  ") -- normalized --> (" + str(normalized_x[i]) +", " + str(normalized_y[i]) + ")")

            print("dist : " + str(dist) + " -- normalized --> " + str(dist_n) + "\n")

            vis_df.append(xlist[i])
            vis_dfn.append(normalized_x[i])

            vis_df2.append(ylist[i])
            vis_df2n.append(normalized_y[i])

            vis_df3.append(dist)
            vis_df3n.append(dist_n)


    print(vis_df)
    print(vis_dfn)

    plt.subplot(321)
    plt.title("X before normalizing")
    plt.plot(vis_df)
    plt.subplot(322)
    plt.title("X after normalizing")
    plt.plot(vis_dfn)
    plt.subplot(323)
    plt.title("Y before normalizing")
    plt.plot(vis_df2)
    plt.subplot(324)
    plt.title("Y after normalizing")
    plt.plot(vis_df2n)
    plt.subplot(325)
    plt.title("dist before normalizing")
    plt.plot(vis_df3)
    plt.subplot(326)
    plt.title("dist after normalizing")
    plt.plot(vis_df3n)
    plt.legend(loc='upper right')
    plt.show()
