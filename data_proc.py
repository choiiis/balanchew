import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

right_dict_list = []

with open("right.json", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        right_data = json.loads(line)
        # count : line num
        print(count)
        count += 1
        right_dict_list.append(right_data)


matrix = [[0 for col in range(68)] for row in range(count)]

for i in range(0,count):
    for j in range(0, 68):
        matrix[i][j] = right_dict_list[i][str(j)][0]
        print(j, " ", right_dict_list[i][str(j)][0])

x = np.arange(0, 68)

for i in range(0,count):
    plt.scatter(x, matrix[i], 1, label=str(i))

plt.xlabel('face landmarks')
plt.ylabel('coordinates')

plt.title('Landmarks analysis')
plt.legend(loc='upper right')
plt.show()





#     lines = f.readlines()
#     jsonDF = pd.DataFrame(json.loads(line) for line in lines)
#     count = 0;
#     for line in lines:
#         count+= 1
#
# df = pd.DataFrame.from_records(jsonDF, columns=['1'])
#
# plt.title('left 1')
# df['1'].plot(label='1')
# plt.show(block=True)





# with open("right.json", "w") as json_file:
