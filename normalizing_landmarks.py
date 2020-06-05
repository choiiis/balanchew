# 얼굴 크기에 따라 데이터 normalize하고 csv에 저장
# 가로 길이 100으로 맞추기

import json
import pandas as pd
import math

x = pd.DataFrame()
y = pd.DataFrame()

with open("right_8.json", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
        # print(count)
        data = json.loads(line)
        df = pd.DataFrame.from_dict(data, orient='index').T

        xlist = df.loc[0]
        xlist_df = pd.DataFrame(xlist).T
        ylist = df.loc[1]
        ylist_df = pd.DataFrame(ylist).T

        xdist = xlist[xlist.idxmax(axis=1)] - xlist[xlist.idxmin(axis=1)]
        ydist = ylist[ylist.idxmax(axis=1)] - ylist[ylist.idxmin(axis=1)]

        # print("[x, y] : [" + str(xdist) + ", " + str(ydist) + "] ---normarlized--> " + \
        #       "[x, y] : [" + str(xdist * (100 / xdist)) + ", " + str(ydist * (100 / xdist)) + "]")


        normalized_x = (xlist - xlist[xlist.idxmin(axis=1)]) * (100 / xdist)
        normalized_x = pd.DataFrame(normalized_x).T
        x = pd.concat([x, normalized_x])
        # print(normalized_x)

        normalized_y = (ylist - ylist[ylist.idxmin(axis=1)]) * (100 / xdist)
        normalized_y = pd.DataFrame(normalized_y).T
        y = pd.concat([y, normalized_y])
        # print(normalized_y)

    x.to_csv('normalized_x.csv', sep = ',', na_rep = 'NaN', index=False)
    y.to_csv('normalized_y.csv', sep = ',', na_rep = 'NaN', index=False)


        # nose = math.sqrt(((xlist[29] - xlist[30]) ** 2) + \
        #                   ((ylist[29] - ylist[30]) ** 2))
        # print("nose origin : " + str(nose))

        # nose_n = math.sqrt(((normalized_x[29] - normalized_x[30]) ** 2) + \
        #                  ((normalized_y[29] - normalized_y[30]) ** 2))
        # print("nose origin : " + str(nose) + "          nose after normalizing : " + str(nose_n))

        # print("nose origin : " + str(xlist[30]) + "         " + str(ylist[30]))
        # print("nose normalized : " + str(normalized_x[30]) + "         " + str(normalized_y[30]))


