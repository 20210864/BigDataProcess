#!/usr/bin/python3
import numpy as np
import operator
from os import listdir
from pathlib import Path


def createDataSet(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def hwClassifier(training, test):
    trLabels = []
    tsLabels = []
    trainingFileList = listdir(training)
    testFileList = listdir(test)
    r = len(trainingFileList)
    s = len(testFileList)
    trainingMat = np.zeros((r, 1024))
    a = 0
    for trf in Path(training).iterdir():
        trainingMat[a, :] = createDataSet(trf)
        trfStr = trainingFileList[a]
        trStr = trfStr.split('.')[0]
        trNumStr = int(trStr.split('_')[0])
        trLabels.append(trNumStr)
        a+=1

    for k in range(1, 21):
        b = 0
        errorRate = 0
        error = 0
        for tsf in Path(test).iterdir():
            tsfStr = testFileList[b]
            tsStr = tsfStr.split('.')[0]
            tsNumStr = int(tsStr.split('_')[0])
            testData = createDataSet(tsf)
            classifierResult = classify0(testData, trainingMat, trLabels, k)
            if (classifierResult != tsNumStr):
                error += 1
            b+=1
        errorRate = error/s*100
        print(int(errorRate))


hwClassifier("trainingDigits", "testDigits")
