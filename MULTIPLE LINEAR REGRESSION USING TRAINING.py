# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:06:11 2020

@author: lohit
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_excel("E:/ppts/5-multiple-linear-reg/hiring.xlsx")
df
import math
median_experience = math.floor(df.experience.median())
median_testscore = math.floor(df.testscore.median())
median_interviewscore=math.floor(df.interviewscore.median())
df.experince =df.experince.fillna(median_experience)
df 
df.testscore=df.testscore.fillna(median_testscore)
df.experience=df.experience.fillna(median_experience)
df.interviewscore=df.interviewscore.fillna(median_interviewscore)
df
reg = linear_model.LinearRegression() 
reg.fit(df[['experience', 'testscore', 'interviewscore']], df['salary']) 
reg.coef_
reg.intercept_
reg.predict([[2,9,6]])#47056.91056911
reg.predict([[12,10,10]])#88227.64227642
