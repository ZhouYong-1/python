# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:57:10 2018
@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression  # 导入线性回归模型
from sklearn.preprocessing import PolynomialFeatures  # 导入多项式回归模型

# 给定x、y数据
x = np.array([50, 100, 150, 200, 250, 300]).reshape(6, 1)
y = np.array([150, 200, 250, 280, 310, 330])
# 绘制散点图

plt.plot(x, y, 'g.', markersize=20)
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([30, 400, 100, 400])
plt.grid(True)
# 线性回归
linear_regressor = LinearRegression()
linear_regressor.fit(x, y)
x2 = np.array([30, 400]).reshape(2, 1)
y2 = linear_regressor.predict(x2)
plt.plot(x2, y2, label='$y = ax + c$')
plt.legend()
# 多项式回归

polynomial = PolynomialFeatures(degree=3)  # 二次多项式
x_transformed = polynomial.fit_transform(x)  # x每个数据对应的多项式系数

poly_linear_model = LinearRegression()  # 创建回归器
poly_linear_model.fit(x_transformed, y)  # 训练数据

xx = np.linspace(30, 400, 100)  # 绘制多项式曲线数据
xx_transformed = polynomial.fit_transform(xx.reshape(xx.shape[0], 1))  # 把训练好X值的多项式特征实例应用到一系列点上,形成矩阵
yy = poly_linear_model.predict(xx_transformed)
plt.plot(xx, yy, label="$y = ax^2 + bx + c$")
plt.legend()

x_test = [[250], [300]]
y_test = [[310], [330]]
# R 方也叫确定系数  介于 0～1 之间的正数  LinearRegression 的 score 方法可以计算 R 方
print('一元线性回归 r-squared', linear_regressor.score(x_test, y_test))

x_test_cubic = polynomial.transform(x_test)
print('三次线性回归 r-squared', poly_linear_model.score(x_test_cubic, y_test))

# 预测一个数值
aa = polynomial.fit_transform([[50]])
bb = poly_linear_model.predict(aa)
print(bb)