#bmi.csv data로 svm 분류
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import time
start_time=time.time()


#키와 몸무게 데이터 읽어들이기
left_df=pd.read_csv("left4_y.csv")
right_df=pd.read_csv("right4_y.csv")
left_df["pos"]="left"
right_df["pos"]="right"
df = pd.concat([left_df, right_df])

#칼럼을 자르고 정규화하기
# label=df["label"]
# w=df["weight"]
# h=df["height"]
# wh=pd.concat([w,h],axis=1) #데이터프레임 합치기 ###정규화가 어디서 일어난거?
label=df["pos"]
# y13=df["13"]
y3=df["3"]
# y12=df["12"]
y13=df["13"]
y59=df["59"]
y65=df["65"]
# y57=df["57"]
# y66=df["66"]
# y9=df["9"]
# y7=df["7"]
# y7=df["7"]
# y7=df["7"]
yy=pd.concat([y3, y13, y59, y65],axis=1) #데이터프레임 합치기 ###정규화가 어디서 일어난거?

#학습 전용 데이터와 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(yy,label)

#데이터 학습하기
clf=svm.SVC() #support vector classification
clf.fit(data_train, label_train)

#데이터 예측하기
predict=clf.predict(data_test)

#결과 테스트하기
ac_score=metrics.accuracy_score(label_test, predict)
cl_report=metrics.classification_report(label_test, predict)
print("정답률: ", ac_score)
print("\n-----report-----\n", cl_report)

# csv load
# df = pd.read_csv("bmi.csv", index_col=2)

# 그래프 그리기 시작
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)


# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
# def scatter(lbl, color):
#     b = df.loc[lbl]
#     ax.scatter(b["weight"], b["height"], c=color, label=lbl)


# scatter("fat", "red")
# scatter("normal", "yellow")
# scatter("thin", "purple")


# ax.legend()
# plt.savefig("bmi-test.png")
# plt.show()