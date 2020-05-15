# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:09:18 2020

@author: Anna-Katharina
"""
import random
import math
import statistics
import numpy as np

from Households import Household
class Model:
    """
    This is a class i the instance of a single model as described in the paper.
    
    1. Create Households
    3. Run model for x time steps
        3.0. Compute nb of allowances for this time step # TODO check sequence
        3.1. Compute demand for each household
        3.2. HH decide whether they buy
        3.3. HH decide why save or invest
        3.4. Compute price for allowances in the next period # TODO check in netlogo mode
    3.5. Save state variables
    4. Save results
    """
    def __init__(self, nb_hh, t_steps):
        self.t_steps = t_steps
        self.list_of_households = self.create_households(nb_hh=nb_hh)
        print("THESE ARE ALL YOUR HOUSEHOLDS:")
        for h in self.list_of_households:
            print(h.id)
            print("***")
            print(h.numpers)
            print(h.income)
            print(h.demand)
            print("---")
            
            
    def first_period(self):
        print("THESE ARE ALL YOUR HOUSEHOLDS IN THE FIRST PERIOD:")
        avg_demand = np.mean([h.demand for h in self.list_of_households])
        print("-----------------------")
        print("The average demand, that is ALLOWANCE PER HH, is:")
        print(avg_demand)
        print("-----------------------")
        for h in self.list_of_households:
            print(h.id)
            print("***") 
            h.calc_actualdemand_t0(avg_demand)
            h.decide_sellbuy_t0()
            h.decide_investsave()
            print(h.income)
            print(h.demand)
            if h.income < 0:
                print(">>>>>I am dead because I cannot make debt")
            else:
                {}
            print("---")
            
 #TODO delet dead household from list   
    
    def run(self):
        percentreducallow = 0.01
        price = 0.05
        #From NetLogo Code: according to p(t+1)-pt=α(Dt-St) = p_t+1 = p_t + alpha * (dempandpool - allowpool_new)
        #with demandpool = demand for allowances (in this case this is negative actualdemand)
        #and with allowpool = supply for allowances (in this case this is positive aactualdemand)
        #allowpool_new the refers to the supply for allowances of the current time stept, but since we have an implicit assumption for Markträumung this is irrelevant. 
        print("THESE ARE YOUR HOUSEHOLDS IN ALL OTHER TIME STEPS:")
        for i in range(self.t_steps):
            avg_demand = np.mean([h.demand for h in self.list_of_households])
            AllowanceAssignment = avg_demand - (avg_demand * percentreducallow)
            print("-----------------------")
            print("The new ALLOWANCE PER HH is:")
            print(AllowanceAssignment)
            print("-----------------------")
            print("Time step: {}".format(i))
            print("_ _ _")
            for h in self.list_of_households:
                print(h.id)
                print("***")
                h.calc_actualdemand_ti(avg_demand, percentreducallow)
                h.decide_sellbuy(price)
                h.decide_investsave()
                print(h.income)
                print(h.demand)
                if h.income < 0:
                    print(">>>>>I am dead because I cannot make debt")
                else:
                    {}
                print("--- ")
    
    def create_households(self, nb_hh):
        """Create the households

        Just creates a list of households.
        
        Parameters
        ----------
        nb_hh: int
            Nb of households in the mode
        """
        list_of_hh = [Household(id=i) for i in range(nb_hh)]
        return list_of_hh
    