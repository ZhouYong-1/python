from sklearn.linear_model import LinearRegression
import numpy as np

x_train = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                   ])

y_train = np.array([6,15,24])

x_test =np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9],
                   ])

clf = LinearRegression()
clf.fit(x_train, y_train)

# 返回回归值
print(clf.predict(x_test))
# 返回权重
print(clf.coef_)
# 返回截距
print(clf.intercept_)