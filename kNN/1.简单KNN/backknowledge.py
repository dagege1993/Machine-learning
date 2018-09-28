# numpy.tile()是个什么函数呢，说白了，就是把数组沿各个方向复制
import numpy as np

'''b = np.array([[1, 2], [3, 4]])
print('原始数据')
print(b)

print('沿x轴复制2遍')
print(np.tile(b, 2))  # 沿X轴复制2倍
print('沿X轴复制1倍（相当于没有复制），再沿Y轴复制2倍')

print('沿X轴复制1倍（相当于没有复制），再沿Y轴复制2倍')
print(np.tile(b, (2, 1)))  # 沿X轴复制1倍（相当于没有复制），再沿Y轴复制2倍
'''

'''
# 二维数据求和
print(np.sum([0.5, 1.5]))

print(np.sum([[0, 1], [0, 5]]))

print('原始数据')
print([[0, 1], [0, 5]])
print("当axis为0时,是压缩行,即将每一列的元素相加,将矩阵压缩为一行")
print(np.sum([[0, 1], [0, 5]], axis=0))
print('当axis为1时,是压缩列,即将每一行的元素相加,将矩阵压缩为一列')
print(np.sum([[0, 1], [0, 5]], axis=1))
'''

# numpy.argsort(a, axis=-1, kind=’quicksort’, order = None)
# 功能: 将矩阵a按照axis排序，并返回排序后的下标
# 参数: a:输入矩阵， axis: 需要排序的维度
# 返回值: 输出排序后的下标

x = np.array([3, 1, 2])
print('原始数据')
print(x)
print('np.argsort(x)排序的数据')
print(np.argsort(x))
print('排序原始数据')
x = np.array([[1, 5, 7], [3, 2, 4]])
print('沿着行向下(每列)的元素进行排序')
print(np.argsort(x, axis=0))  # 沿着行向下(每列)的元素进行排序
print('沿着列向右(每行)的元素进行排序')
print(np.argsort(x, axis=1))  # 沿着列向右(每行)的元素进行排序
