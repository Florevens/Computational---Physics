# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:29:52 2022

@author: flore
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import math
import scipy.stats as st
import pandas as pd 

mean = 4

upperlim = mean + 2*math.sqrt(mean)
lowerlim = mean - 2*math.sqrt(mean)
iupperlim = math.trunc(upperlim)
ilowerlim = math.trunc(lowerlim)
if ilowerlim < 0:
    ilowerlim = 0
poissonprob = []
print(ilowerlim,iupperlim)

for i in range(ilowerlim,iupperlim+1):
    poissonprob.append( math.exp(-1*mean)*mean**i/math.factorial(i) )
xrange = list(range(ilowerlim,iupperlim+1))
print(xrange)
print(poissonprob)

plt.xticks()
plt.bar(xrange, poissonprob)
"""the probabilities to measure 3 and 4( at .19) counts are very similar but that probability
starts getting lower on the right hand side of the poison at the measures of 5(at .16) counts"""