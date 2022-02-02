# 얼굴 크기 normalize 한 상태
# 얼굴 크기/ 위치에 따라 길이 차이 없는지 확인

import json
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

lx1=pd.read_csv("../video_lm/CHM_left_x.csv")
ly1=pd.read_csv("../video_lm/CHM_left_y.csv")
rx1=pd.read_csv("../video_lm/CHM_right_x.csv")
ry1=pd.read_csv("../video_lm/CHM_right_y.csv")

lx2=pd.read_csv("../video_lm/CJL_left_x.csv")
ly2=pd.read_csv("../video_lm/CJL_left_y.csv")
rx2=pd.read_csv("../video_lm/CJL_right_x.csv")
ry2=pd.read_csv("../video_lm/CJL_right_y.csv")

lx3=pd.read_csv("../video_lm/Dad_left_x.csv")
ly3=pd.read_csv("../video_lm/Dad_left_y.csv")
rx3=pd.read_csv("../video_lm/Dad_right_x.csv")
ry3=pd.read_csv("../video_lm/Dad_right_y.csv")

lx4=pd.read_csv("../video_lm/HJW_left_x.csv")
ly4=pd.read_csv("../video_lm/HJW_left_y.csv")
rx4=pd.read_csv("../video_lm/HJW_right_x.csv")
ry4=pd.read_csv("../video_lm/HJW_right_y.csv")

lx5=pd.read_csv("../video_lm/KSH_left_x.csv")
ly5=pd.read_csv("../video_lm/KSH_left_y.csv")
rx5=pd.read_csv("../video_lm/KSH_right_x.csv")
ry5=pd.read_csv("../video_lm/KSH_right_y.csv")

lx6=pd.read_csv("../video_lm/KWK_left_x.csv")
ly6=pd.read_csv("../video_lm/KWK_left_y.csv")
rx6=pd.read_csv("../video_lm/KWK_right_x.csv")
ry6=pd.read_csv("../video_lm/KWK_right_y.csv")

lx7=pd.read_csv("../video_lm/LSY_left_x.csv")
ly7=pd.read_csv("../video_lm/LSY_left_y.csv")
rx7=pd.read_csv("../video_lm/LSY_right_x.csv")
ry7=pd.read_csv("../video_lm/LSY_right_y.csv")

lx8=pd.read_csv("../video_lm/LYE_left_x.csv")
ly8=pd.read_csv("../video_lm/LYE_left_y.csv")
rx8=pd.read_csv("../video_lm/LYE_right_x.csv")
ry8=pd.read_csv("../video_lm/LYE_right_y.csv")

lx9=pd.read_csv("../video_lm/LYJ_left_x.csv")
ly9=pd.read_csv("../video_lm/LYJ_left_y.csv")
rx9=pd.read_csv("../video_lm/LYJ_right_x.csv")
ry9=pd.read_csv("../video_lm/LYJ_right_y.csv")

lx10=pd.read_csv("../video_lm/Mom_left_x.csv")
ly10=pd.read_csv("../video_lm/Mom_left_y.csv")
rx10=pd.read_csv("../video_lm/Mom_right_x.csv")
ry10=pd.read_csv("../video_lm/Mom_right_y.csv")

lx11=pd.read_csv("../video_lm/Sis_left_x.csv")
ly11=pd.read_csv("../video_lm/Sis_left_y.csv")
rx11=pd.read_csv("../video_lm/Sis_right_x.csv")
ry11=pd.read_csv("../video_lm/Sis_right_y.csv")

# x = lx2['59']
# y = ly2['59']-30
# x = rx1['54']
# y = ry1['54']


lxn = pd.DataFrame()
for i in range(0,68):
    lxtmp = lx11[str(i)].T
    lxtmp2 = pd.DataFrame([lxtmp[0]])
    lxtmp2 = lxtmp2.append([lxtmp[1]])
    # for j in range(1, len(lx11) - 1):
    #     lxtmp2 = lxtmp2.append([(lxtmp[j-1] + 2 * lxtmp[j] + lxtmp[j+1]) / 4])
    for j in range(2, len(lx11) - 2):
        lxtmp2 = lxtmp2.append([(lxtmp[j-2] + 2* lxtmp[j-1]
                                 + 3 * lxtmp[j] + 2 * lxtmp[j+1] + lxtmp[j+2]) / 9])
    lxtmp2 = lxtmp2.append([lxtmp[len(lx11) - 2]])
    lxtmp2 = lxtmp2.append([lxtmp[len(lx11)-1]])
    lxn = pd.concat([lxn,lxtmp2.T])
lxn = lxn.reset_index(drop=True).T.reset_index(drop=True)

lyn = pd.DataFrame()
for i in range(0,68):
    lytmp = ly11[str(i)].T
    lytmp2 = pd.DataFrame([lytmp[0]])
    lytmp2 = lytmp2.append([lytmp[1]])
    # for j in range(1, len(ly11) - 1):
    #     lytmp2 = lytmp2.append([(lytmp[j-1] + 2 * lytmp[j] + lytmp[j+1]) / 4])
    for j in range(2, len(ly11) - 2):
        lytmp2 = lytmp2.append([(lytmp[j-2] + 2* lytmp[j-1]
                                 + 3 * lytmp[j] + 2 * lytmp[j+1] + lytmp[j+2]) / 9])
    lytmp2 = lytmp2.append([lytmp[len(ly11) - 2]])
    lytmp2 = lytmp2.append([lytmp[len(ly11)-1]])
    lyn = pd.concat([lyn,lytmp2.T])
lyn = lyn.reset_index(drop=True).T.reset_index(drop=True)

rxn = pd.DataFrame()
for i in range(0,68):
    rxtmp = rx11[str(i)].T
    rxtmp2 = pd.DataFrame([rxtmp[0]])
    rxtmp2 = rxtmp2.append([rxtmp[1]])
    # for j in range(1, len(rx11) - 1):
    #     rxtmp2 = rxtmp2.append([(rxtmp[j-1] + 2 * rxtmp[j] + rxtmp[j+1]) / 4])
    for j in range(2, len(rx11) - 2):
        rxtmp2 = rxtmp2.append([(rxtmp[j-2] + 2* rxtmp[j-1]
                                 + 3 * rxtmp[j] + 2 * rxtmp[j+1] + rxtmp[j+2]) / 9])
    rxtmp2 = rxtmp2.append([rxtmp[len(rx11) - 2]])
    rxtmp2 = rxtmp2.append([rxtmp[len(rx11)-1]])
    rxn = pd.concat([rxn,rxtmp2.T])
rxn = rxn.reset_index(drop=True).T.reset_index(drop=True)

ryn = pd.DataFrame()
for i in range(0,68):
    rytmp = ry11[str(i)].T
    rytmp2 = pd.DataFrame([rytmp[0]])
    rytmp2 = rytmp2.append([rytmp[1]])
    # for j in range(1, len(ry11) - 1):
    #     rytmp2 = rytmp2.append([(rytmp[j-1] + 2 * rytmp[j] + rytmp[j+1]) / 4])
    for j in range(2, len(ry11) - 2):
        rytmp2 = rytmp2.append([(rytmp[j-2] + 2* rytmp[j-1]
                                 + 3 * rytmp[j] + 2 * rytmp[j+1] + rytmp[j+2]) / 9])
    rytmp2 = rytmp2.append([rytmp[len(ry11) - 2]])
    rytmp2 = rytmp2.append([rytmp[len(ry11)-1]])
    ryn = pd.concat([ryn,rytmp2.T])
ryn = ryn.reset_index(drop=True).T.reset_index(drop=True)


# x = lx1['59']
# y = ly1['59']-30
# x = ry1['59']
# y = ryn['59'] + 5


x1 = lx11['59']
y1 = lxn[59]
x2 = ly11['59']
y2 = lyn[59]
x3 = rx11['59']
y3 = rxn[59]
x4 = ry11['59']
y4 = ryn[59]
#
# lxn.to_csv('../move_dir/filtered_data/Sis_left_x_5.csv', sep=',', na_rep='NaN', index=False)
# lyn.to_csv('../move_dir/filtered_data/Sis_left_y_5.csv', sep=',', na_rep='NaN', index=False)
# rxn.to_csv('../move_dir/filtered_data/Sis_right_x_5.csv', sep=',', na_rep='NaN', index=False)
# ryn.to_csv('../move_dir/filtered_data/Sis_right_y_5.csv', sep=',', na_rep='NaN', index=False)


plt.figure(figsize=(12, 7))
plt.subplot(421)
plt.plot(x1, label="origin")
plt.legend(loc='upper right')
# plt.subplot(422)
# plt.plot(y1, label="sliding window 3")
# plt.legend(loc='upper right')
plt.subplot(422)
plt.plot(y1, label="sliding window 5")
plt.legend(loc='upper right')

plt.subplot(423)
plt.plot(x2, label="origin")
plt.legend(loc='upper right')
# plt.subplot(424)
# plt.plot(y2, label="sliding window 3")
# plt.legend(loc='upper right')
plt.subplot(424)
plt.plot(y2, label="sliding window 5")
plt.legend(loc='upper right')

plt.subplot(425)
plt.plot(x3, label="origin")
plt.legend(loc='upper right')
# plt.subplot(426)
# plt.plot(y3, label="sliding window 3")
# plt.legend(loc='upper right')
plt.subplot(426)
plt.plot(y3, label="sliding window 5")
plt.legend(loc='upper right')

plt.subplot(427)
plt.plot(x4, label="origin")
plt.legend(loc='upper right')
# plt.subplot(428)
# plt.plot(y4, label="sliding window 3")
# plt.legend(loc='upper right')
plt.subplot(428)
plt.plot(y4, label="sliding window 5")
plt.legend(loc='upper right')
# plt.savefig("../move_dir/filtered_data/Sis5.png")
plt.show()


