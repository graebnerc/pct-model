# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:09:18 2020

@author: Anna-Katharina
"""
import random
import math
import statistics
import numpy as np

from Model import Model

"""
Initialization of the Model. 
Insert Number of Households and Time Steps. 
"""
FirstTry = Model(2, 2)
"""
The Model will give back an list of all households with the following information:
    ID of Household
    ***
    Numper of Persons living in the Household
    Income per time step
    Initial Demand
"""

"""
The first period is different because the market operates with a set start price. 
In all other periods the market price will be calculated from demand and supply of allowances on the market.
"""

FirstTry.first_period()
"""
This will give back an list of all households with the following information:
    ID of Household
    ***
    The actual demand, that is average demand - demand of the household
    Whether the Household is above or below average
    Decision and
    Success in regard to the selling or buying
    Decision and
    Success in regard to the investing or saving
    The new income after the first period
    The new demand after the first period
"""

FirstTry.run()
"""
This will give back an list of all households with the following information:
    Time Step
    _ _ _
    HH ID
    ***
    New actual demand, that is the new allowances per household - new demand of household
    Whether the Household is above or below it
    Decision and
    Success in regard to the selling or buying
    Decision and
    Success in regard to the investing or saving
    The new income after the first period
    The new demand after the first period
"""