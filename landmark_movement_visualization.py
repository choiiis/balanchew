import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

lx = pd.read_csv('./move_dir/filtered_data/CHM_left_x_5_nor.csv')
ly = pd.read_csv('./move_dir/filtered_data/CHM_left_y_5_nor.csv')
rx = pd.read_csv('./move_dir/filtered_data/CHM_right_x_5_nor.csv')
ry = pd.read_csv('./move_dir/filtered_data/CHM_right_y_5_nor.csv')

ptrn = [29, 58, 86, 112, 140, 166, 187, 211, 235, 253]
ptrn2 = [3, 33, 64, 87, 115, 151, 174, 203, 228, 251, 277]
rnge = [48, 54, 66]
for i in rnge:
    for j in range(len(ptrn)-1):
        cnt = 0
        while True:
            if cnt > ptrn[j+1] - ptrn[j]:
                break
            cnt += 3
            alll = pd.concat([pd.DataFrame(lx[str(i)].loc[ptrn[j]:ptrn[j] + cnt]).T,
                              pd.DataFrame(ly[str(i)].loc[ptrn[j]:ptrn[j] + cnt]).T]).T
            alll['pos'] = 'left'
            alll.columns = ['x', 'y', 'pos']
            allr = pd.concat([pd.DataFrame(rx[str(i)].loc[ptrn[j]:ptrn[j] + cnt]).T,
                              pd.DataFrame(ry[str(i)].loc[ptrn[j]:ptrn[j] + cnt]).T]).T
            allr['pos'] = 'right'
            allr.columns = ['x', 'y', 'pos']
            all = pd.concat([alll, allr])
            all.reset_index(drop=True)

            first = all.loc[ptrn[j]]
            first['pos'] = ['left first', 'right first']
            all = all.drop([ptrn[j]])
            all = all.append(first)

            sns.FacetGrid(all, hue="pos", palette='Set1', height=4).map(plt.scatter, "x", "y", s=15).add_legend()
            plt.grid()
            plt.show()




