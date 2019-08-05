

import numpy as np
import matplotlib.pyplot as plt

# 训练集中所有样本是否都分类正确
def is_error(data, label, w, b):
    for i in range(len(data)):
        prediction = w.dot(data[i].transpose()) + b
        if prediction * label[i] <= 0:
            return True
    return False

data = np.asarray([[3,3], [4,3], [1,1]])
label = np.asarray([1, 1, -1])
learning_rate = 1

w = np.asarray([0, 0])
b = 0

while is_error(data, label, w, b):
    for i in range(len(data)):
        sample = data[i]
        loss = label[i] * (w.dot(sample.transpose()) + b)
        if loss <= 0:
            w = w + learning_rate * label[i] * sample
            b = b + learning_rate * label[i]
    print(w,b)


plt.scatter(data[:2, 0],data[:2, 1], marker='+')
plt.scatter(data[-1, 0],data[-1, 1])
line_x = np.arange(0,5,0.01)
line_y = -(w[0] * line_x + b) / w[1]
plt.plot(line_x, line_y)
plt.show()