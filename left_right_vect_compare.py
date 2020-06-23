import json
import pandas as pd
import math
import matplotlib.pyplot as plt
import os
import seaborn as sns


lx = pd.read_csv('./move_dir/filtered_data/Sis_left_x_5_nor.csv')
ly = pd.read_csv('./move_dir/filtered_data/Sis_left_y_5_nor.csv')
rx = pd.read_csv('./move_dir/filtered_data/Sis_right_x_5_nor.csv')
ry = pd.read_csv('./move_dir/filtered_data/Sis_right_y_5_nor.csv')


ptrn = [0, 23, 50, 74, 97, 132, 150, 180, 199, 225]
ptrn2 =[0, 25, 48, 71, 93, 114, 136, 152, 176, 199, 214]

vect_lx_all2 = pd.DataFrame()
vect_rx_all2 = pd.DataFrame()
vect_ly_all2 = pd.DataFrame()
vect_ry_all2 = pd.DataFrame()

vect_lx_cnt = []
vect_ly_cnt = []
vect_rx_cnt = []
vect_ry_cnt = []


rnge = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]

vect_lx_all = []
vect_ly_all = []
vect_rx_all = []
vect_ry_all = []
for k in rnge:
    print('=========== landmark no.' + str(k) + '==============')

    print('---------------left---------------')
    for i in range(len(ptrn) - 1):
        lx1 = lx[str(k)][ptrn[i]]
        ly1 = ly[str(k)][ptrn[i]]
        for j in range(ptrn[i] + 1, ptrn[i + 1]):
            vect_lx = lx[str(k)][j] - lx1
            vect_ly = ly[str(k)][j] - ly1
            vect_lx_all.append(vect_lx)
            vect_ly_all.append(vect_ly)
            vect_lx_cnt.append(vect_lx)
            vect_ly_cnt.append(vect_ly)
        print(vect_lx_all)

    print('---------------right---------------')
    for i in range(len(ptrn2) - 1):
        rx1 = rx[str(k)][ptrn2[i]]
        ry1 = ry[str(k)][ptrn2[i]]
        for j in range(ptrn2[i] + 1, ptrn2[i + 1]):
            vect_rx = rx[str(k)][j] - rx1
            vect_ry = ry[str(k)][j] - ry1
            vect_rx_all.append(vect_rx)
            vect_ry_all.append(vect_ry)
            vect_rx_cnt.append(vect_rx)
            vect_ry_cnt.append(vect_ry)
        print(vect_rx_all)


vect_lx_all = pd.DataFrame(vect_lx_all)
vect_rx_all = pd.DataFrame(vect_rx_all)
vect_ly_all = pd.DataFrame(vect_ly_all)
vect_ry_all = pd.DataFrame(vect_ry_all)

alll = pd.concat([vect_lx_all.T, vect_ly_all.T]).T
alll['pos'] = 'left'
allr = pd.concat([vect_rx_all.T, vect_ry_all.T]).T
allr['pos'] = 'right'
all = pd.concat([alll, allr])
all.columns = ['x', 'y', 'pos']

print(alll)
print(allr)
print(all)

sns.FacetGrid(all, hue="pos", height=4).map(plt.scatter, "x", "y").add_legend()
plt.grid()
plt.show()





