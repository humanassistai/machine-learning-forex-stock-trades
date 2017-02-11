#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
so we suspect that possibly

To compare patterns:
use a % change calculation to calculate similarity between each %change
movement in the pattern finder. From those numbers, subtract them from 100, to
get a "how similar" #. From this point, take all 10 of the how similars,
and average them. Whichever pattern is MOST similar, is the one we will assume
we have found.
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import bytespdate2num
import numpy as np
import time
from matplotlib import style
style.use('ggplot')
(date, bid, ask) = np.loadtxt('GBPUSD1d.txt', unpack=True, delimiter=','
                              ,
                              converters={0: mdates.bytespdate2num('%Y%m%d%H%M%S'
                              )})
#Simple Average
avgLine = ((bid+ask)/2)
#used to store pattern
patternAr = []
performanceAr = []
patForRec =[]


def percentChange(startPoint,currentPoint):
    try:
        x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0001
'''
The goal of patternFinder is to begin collection of %change patterns
in the tick data. From there, we also collect the short-term outcome
of this pattern. Later on, the length of the pattern, how far out we
look to compare to, and the length of the compared range be changed,
and even THAT can be machine learned to find the best of all 3 by
comparing success rates.
'''
def patternStorage():
    startTime = time.time() #check the procesing time
    # required to do a pattern array, because the liklihood of an identical
    # %change across millions of patterns is fairly likely and would
    # cause problems. IF it was a problem of identical patterns,
    # then it wouldnt matter, but the % change issue
    # would cause a lot of harm. Cannot have a list as a dictionary Key.
    #MOVE THE ARRAYS THEMSELVES#
    #This finds the length of the total array for us
    x = len(avgLine)-30
    #This will be our starting point, allowing us to compare to the
    #past 10 % changes.
    y = 11
    # where we are in a trade. #
    # can be none, buy,
    # print('i am here')
    currentStance = 'none'
    while y < x:
        pattern = [];
        p1 = percentChange(avgLine[y-10], avgLine[y-9])
        p2 = percentChange(avgLine[y-10], avgLine[y-8])
        p3 = percentChange(avgLine[y-10], avgLine[y-7])
        p4 = percentChange(avgLine[y-10], avgLine[y-6])
        p5 = percentChange(avgLine[y-10], avgLine[y-5])
        p6 = percentChange(avgLine[y-10], avgLine[y-4])
        p7 = percentChange(avgLine[y-10], avgLine[y-3])
        p8 = percentChange(avgLine[y-10], avgLine[y-2])
        p9 = percentChange(avgLine[y-10], avgLine[y-1])
        p10= percentChange(avgLine[y-10], avgLine[y])
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            avgOutcome = lambda x, y: x + y, outcomeRange / len(outcomeRange)
        except Exception as e:
            print(str(e))
        avgOutcome = 0
        #function to account for the average of the items in the array
        #reduce = lambda x, y: x + y, outcomeRange/len(outcomeRange)
        # print(reduce)
        # print("check")
        #Define
        futureOutcome = percentChange(currentPoint, avgOutcome)
        print(currentPoint)
        print('where we are historically:',currentPoint)
        print('soft outcome of the horizon:',avgOutcome)
        print('This pattern brings a future change of:',futureOutcome)
        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        print('------------------')
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        #can use .index to find the index value, then search for that value to get the matching information.
        # so like, performanceAr.index(12341)
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y+=1
        endTime = time.time()
        print(len(patternAr))
        print(len(performanceAr))
        print('Pattern storing took:', endTime-startTime)

def patternRecognition():
    #mostRecentPoint = avgLine[-1]
    patForRec = []
    #Simple Average
    cp1 = percentChange(avgLine[-11], avgLine[-10])
    cp2 = percentChange(avgLine[-11], avgLine[-9])
    cp3 = percentChange(avgLine[-11], avgLine[-8])
    cp4 = percentChange(avgLine[-11], avgLine[-7])
    cp5 = percentChange(avgLine[-11], avgLine[-6])
    cp6 = percentChange(avgLine[-11], avgLine[-5])
    cp7 = percentChange(avgLine[-11], avgLine[-4])
    cp8 = percentChange(avgLine[-11], avgLine[-3])
    cp9 = percentChange(avgLine[-11], avgLine[-2])
    cp10= percentChange(avgLine[-11], avgLine[-1])
    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    print(patForRec)

def graphRawFX():
    fig = plt.figure(figsize=(10, 7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    ax1.plot(date, bid)
    ax1.plot(date, ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'
                                  ))
    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, ask - bid, facecolor='g', alpha=.3)
    plt.subplots_adjust(bottom=.23)
    plt.show()


patternRecognition()
