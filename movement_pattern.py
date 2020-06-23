# 얼굴 크기 normalize 한 상태
# 얼굴 크기/ 위치에 따라 길이 차이 없는지 확인

import json
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

lst = [48, 60, 64, 54]
for mark_num in lst:
    x = pd.DataFrame()
    y = pd.DataFrame()

    vis_df = []
    vis_dfn = []

    vis_df2 = []
    vis_df2n = []

    with open("./video_lm/Sis_right.json", "r") as f1:
        lines = f1.readlines()
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

            # 정규화된 x를 normalized_x에 저장
            normalized_x = (xlist - xlist[xlist.idxmin(axis=1)]) * (100 / xdist)
            normalized_y = (ylist - ylist[ylist.idxmin(axis=1)]) * (100 / xdist)

            for i in range(mark_num, mark_num + 1):
                print("--------[" + str(i) + "]--------")
                dist = math.sqrt(((xlist[i] - xlist[30]) ** 2) + \
                                 ((ylist[i] - ylist[30]) ** 2))
                dist_n = math.sqrt(((normalized_x[i] - normalized_x[30]) ** 2) + \
                                   ((normalized_y[i] - normalized_y[30]) ** 2))

                print("point : (" + str(xlist[i]) + ", " + str(ylist[i]) + \
                      ") -- normalized --> (" + str(normalized_x[i]) + ", " + str(normalized_y[i]) + ")")

                print("dist : " + str(dist) + " -- normalized --> " + str(dist_n) + "\n")

                vis_df.append(xlist[i])
                vis_dfn.append(normalized_x[i])

                vis_df2.append(ylist[i])
                vis_df2n.append(normalized_y[i])

        print(vis_dfn)
        print(vis_df2n)
        print(df)

        # plt.figure(figsize=(12,7))
        # plt.title(str(mark_num) + "graph")
        # # plt.subplot(221)
        # # plt.title("X before normalizing")
        # # plt.plot(vis_df)
        # # plt.plot(vis2_df)
        # plt.subplot(211)
        # plt.title("X after normalizing")
        # plt.plot(vis_dfn)
        # # plt.subplot(223)
        # # plt.title("Y before normalizing")
        # # plt.plot(vis_df2)
        # # plt.plot(vis2_df2)
        # plt.subplot(212)
        # plt.title("Y after normalizing")
        # plt.plot(vis_df2n)
        #
        # plt.legend(loc='upper right')
        # # plt.savefig("./move_dir/Sisright_" + str(mark_num) + ".png")
        # # plt.show()
