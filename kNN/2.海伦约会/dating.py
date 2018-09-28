from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import operator


def file2matrix(filename):
    fr = open(filename, 'r', encoding='utf-8')
    # 获取文件行数
    numberOfLines = len(fr.readlines())
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []  # prepare labels return # 准备返回的标签
    index = 0
    fr = open(filename, 'r', encoding='utf-8')
    for line in fr.readlines():
        # str.strip([chars]) --返回已移除字符串头尾指定字符所生成的新字符串
        line = line.strip()  # 以 '\t' 切割字符串
        listFromLine = line.split('\t')
        # 每列的属性数据
        returnMat[index, :] = listFromLine[0:3]
        # 每列的类别数据，就是 label 标签数据
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        # print(classLabelVector)
        index += 1
    # 返回数据矩阵returnMat和对应的类别classLabelVector
    return returnMat, classLabelVector


if __name__ == '__main__':
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    print(datingDataMat)
    fig = plt.figure()  # 创建一个图形实例
    ax = fig.add_subplot(111)  # 子图：就是在一张figure里面生成多张子图,返回的是Axes实例
    # ax = fig.add_subplot(349) #参数349的意思是：将画布分割成3行4列，图像画在从左到右从上到下的第9块，
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], )  # 构造一个散点图
    # ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
    plt.show()
