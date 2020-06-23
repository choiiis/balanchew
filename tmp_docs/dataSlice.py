# 얼굴 크기 normalize 한 상태
# 얼굴 크기/ 위치에 따라 길이 차이 없는지 확인

import json
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

# lx1=pd.read_csv("../video_lm/CHM_left_x.csv")
# ly1=pd.read_csv("../video_lm/CHM_left_y.csv")
# rx1=pd.read_csv("../video_lm/CHM_right_x.csv")
# ry1=pd.read_csv("../video_lm/CHM_right_y.csv")
#
# lx2=pd.read_csv("../video_lm/CJL_left_x.csv")
# ly2=pd.read_csv("../video_lm/CJL_left_y.csv")
# rx2=pd.read_csv("../video_lm/CJL_right_x.csv")
# ry2=pd.read_csv("../video_lm/CJL_right_y.csv")
#
# lx3=pd.read_csv("../video_lm/Dad_left_x.csv")
# ly3=pd.read_csv("../video_lm/Dad_left_y.csv")
# rx3=pd.read_csv("../video_lm/Dad_right_x.csv")
# ry3=pd.read_csv("../video_lm/Dad_right_y.csv")
#
# lx4=pd.read_csv("../video_lm/HJW_left_x.csv")
# ly4=pd.read_csv("../video_lm/HJW_left_y.csv")
# rx4=pd.read_csv("../video_lm/HJW_right_x.csv")
# ry4=pd.read_csv("../video_lm/HJW_right_y.csv")
#
# lx5=pd.read_csv("../video_lm/KSH_left_x.csv")
# ly5=pd.read_csv("../video_lm/KSH_left_y.csv")
# rx5=pd.read_csv("../video_lm/KSH_right_x.csv")
# ry5=pd.read_csv("../video_lm/KSH_right_y.csv")
#
# lx6=pd.read_csv("../video_lm/KWK_left_x.csv")
# ly6=pd.read_csv("../video_lm/KWK_left_y.csv")
# rx6=pd.read_csv("../video_lm/KWK_right_x.csv")
# ry6=pd.read_csv("../video_lm/KWK_right_y.csv")
#
# lx7=pd.read_csv("../video_lm/LSY_left_x.csv")
# ly7=pd.read_csv("../video_lm/LSY_left_y.csv")
# rx7=pd.read_csv("../video_lm/LSY_right_x.csv")
# ry7=pd.read_csv("../video_lm/LSY_right_y.csv")
#
# lx8=pd.read_csv("../video_lm/LYE_left_x.csv")
# ly8=pd.read_csv("../video_lm/LYE_left_y.csv")
# rx8=pd.read_csv("../video_lm/LYE_right_x.csv")
# ry8=pd.read_csv("../video_lm/LYE_right_y.csv")
#
# lx9=pd.read_csv("../video_lm/LYJ_left_x.csv")
# ly9=pd.read_csv("../video_lm/LYJ_left_y.csv")
# rx9=pd.read_csv("../video_lm/LYJ_right_x.csv")
# ry9=pd.read_csv("../video_lm/LYJ_right_y.csv")
#
# lx10=pd.read_csv("../video_lm/Mom_left_x.csv")
# ly10=pd.read_csv("../video_lm/Mom_left_y.csv")
# rx10=pd.read_csv("../video_lm/Mom_right_x.csv")
# ry10=pd.read_csv("../video_lm/Mom_right_y.csv")
#
# lx11=pd.read_csv("../video_lm/Sis_left_x.csv")
# ly11=pd.read_csv("../video_lm/Sis_left_y.csv")
# rx11=pd.read_csv("../video_lm/Sis_right_x.csv")
# ry11=pd.read_csv("../video_lm/Sis_right_y.csv")
#
# lx12=pd.read_csv("../video_lm/all_left_x_filtered.csv")
# ly12=pd.read_csv("../video_lm/all_left_y_filtered.csv")
# rx12=pd.read_csv("../video_lm/all_right_x_filtered.csv")
# ry12=pd.read_csv("../video_lm/all_right_y_filtered.csv")
#
# lx13=pd.read_csv("../video_lm/all_left_x_filtered_nor.csv")
# ly13=pd.read_csv("../video_lm/all_left_y_filtered_nor.csv")
# rx13=pd.read_csv("../video_lm/all_right_x_filtered_nor.csv")
# ry13=pd.read_csv("../video_lm/all_right_y_filtered_nor.csv")

lx1=pd.read_csv("../move_dir/filtered_data/CHM_left_x_5_nor.csv")
ly1=pd.read_csv("../move_dir/filtered_data/CHM_left_y_5_nor.csv")
rx1=pd.read_csv("../move_dir/filtered_data/CHM_right_x_5_nor.csv")
ry1=pd.read_csv("../move_dir/filtered_data/CHM_right_y_5_nor.csv")


lx2=pd.read_csv("../move_dir/filtered_data/CJL_left_x_5_nor.csv")
ly2=pd.read_csv("../move_dir/filtered_data/CJL_left_y_5_nor.csv")
rx2=pd.read_csv("../move_dir/filtered_data/CJL_right_x_5_nor.csv")
ry2=pd.read_csv("../move_dir/filtered_data/CJL_right_y_5_nor.csv")

lx3=pd.read_csv("../move_dir/filtered_data/Dad_left_x_5_nor.csv")
ly3=pd.read_csv("../move_dir/filtered_data/Dad_left_y_5_nor.csv")
rx3=pd.read_csv("../move_dir/filtered_data/Dad_right_x_5_nor.csv")
ry3=pd.read_csv("../move_dir/filtered_data/Dad_right_y_5_nor.csv")

lx4=pd.read_csv("../move_dir/filtered_data/HJW_left_x_5_nor.csv")
ly4=pd.read_csv("../move_dir/filtered_data/HJW_left_y_5_nor.csv")
rx4=pd.read_csv("../move_dir/filtered_data/HJW_right_x_5_nor.csv")
ry4=pd.read_csv("../move_dir/filtered_data/HJW_right_y_5_nor.csv")

lx5=pd.read_csv("../move_dir/filtered_data/KSH_left_x_5_nor.csv")
ly5=pd.read_csv("../move_dir/filtered_data/KSH_left_y_5_nor.csv")
rx5=pd.read_csv("../move_dir/filtered_data/KSH_right_x_5_nor.csv")
ry5=pd.read_csv("../move_dir/filtered_data/KSH_right_y_5_nor.csv")

lx6=pd.read_csv("../move_dir/filtered_data/KWK_left_x_5_nor.csv")
ly6=pd.read_csv("../move_dir/filtered_data/KWK_left_y_5_nor.csv")
rx6=pd.read_csv("../move_dir/filtered_data/KWK_right_x_5_nor.csv")
ry6=pd.read_csv("../move_dir/filtered_data/KWK_right_y_5_nor.csv")

lx7=pd.read_csv("../move_dir/filtered_data/LSY_left_x_5_nor.csv")
ly7=pd.read_csv("../move_dir/filtered_data/LSY_left_y_5_nor.csv")
rx7=pd.read_csv("../move_dir/filtered_data/LSY_right_x_5_nor.csv")
ry7=pd.read_csv("../move_dir/filtered_data/LSY_right_y_5_nor.csv")

lx8=pd.read_csv("../move_dir/filtered_data/LYE_left_x_5_nor.csv")
ly8=pd.read_csv("../move_dir/filtered_data/LYE_left_y_5_nor.csv")
rx8=pd.read_csv("../move_dir/filtered_data/LYE_right_x_5_nor.csv")
ry8=pd.read_csv("../move_dir/filtered_data/LYE_right_y_5_nor.csv")

lx9=pd.read_csv("../move_dir/filtered_data/LYJ_left_x_5_nor.csv")
ly9=pd.read_csv("../move_dir/filtered_data/LYJ_left_y_5_nor.csv")
rx9=pd.read_csv("../move_dir/filtered_data/LYJ_right_x_5_nor.csv")
ry9=pd.read_csv("../move_dir/filtered_data/LYJ_right_y_5_nor.csv")

lx10=pd.read_csv("../move_dir/filtered_data/Mom_left_x_5_nor.csv")
ly10=pd.read_csv("../move_dir/filtered_data/Mom_left_y_5_nor.csv")
rx10=pd.read_csv("../move_dir/filtered_data/Mom_right_x_5_nor.csv")
ry10=pd.read_csv("../move_dir/filtered_data/Mom_right_y_5_nor.csv")

lx11=pd.read_csv("../move_dir/filtered_data/Sis_left_x_5_nor.csv")
ly11=pd.read_csv("../move_dir/filtered_data/Sis_left_y_5_nor.csv")
rx11=pd.read_csv("../move_dir/filtered_data/Sis_right_x_5_nor.csv")
ry11=pd.read_csv("../move_dir/filtered_data/Sis_right_y_5_nor.csv")

x1 = lx11['59']
x2 = ly11['59']
x3 = rx11['59']
x4 = ry11['59']

plt.figure(figsize=(12, 7))
plt.subplot(211)
plt.plot(x1, label="x")
plt.plot(x2, label="y")
plt.subplot(212)
plt.plot(x3, label="x")
plt.plot(x4, label="y")
plt.legend(loc='upper right')

plt.show()


