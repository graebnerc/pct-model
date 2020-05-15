# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:05:31 2020

@author: Anna-Katharina
"""
import random
import math

class Household:
    """
    This is a class of Households.
    """
    def __init__(self, id):
        """
        This is a method that ascribes *random* parameters to the households.
        """
        self.id = id
        self.numpers = random.randrange(1, 4)
        """
        The variable numpers is an integer that denotes how many persons are living in the household.
        The implicit assumption for Number of Persons per Household is a uniform distribution.
        Thus, household with 5 Members are as likely as households with 1, 2 or 3 Members, which most likely does not resemble the German population. 
        Further work on this code could include a left skewed distribution. 
        """
        incseq = (500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0, 4000.0, 4500.0, 5000.0, 5500.0, 6000.0)
        self.income = random.choice(incseq)
        """
        The variable income is an float that denots how much income the household has in total.
        incseq is a list of floats from which the monthly income is randomly drawn.
        The implicit assumption for income is a uniform distribution.
        Thus, household with 500 Euros income are as likely as households with 5000 or more Euros income, which most likely does not resemble the German income distribution.
        Further work on this code could include a left skewed distribution. 
        """
        self.socioecol = random.random()
        self.econ = random.random()
        """
        socioecol and econ are float variables between 0 and 1 that denote the socioecological and economical motivation of households in %.
        """

        self.demand = (1.1 - self.numpers * 0.05) * (math.log(math.log(self.income)) - 0.9) * 20278.0 * self.numpers * (0.8 + 0.4) * 0.527
        """
        The variable demand is a float that denotes how much carbon allowances one household demands in accordance to its number of persons and income.
        The function is retrieved from Seidl [2018]
        It is a rough estimate for the demand per household from Federal Environment Office (2016), page 65.
        Link:  https://www.umweltbundesamt.de/sites/default/files/medien/378/publikationen/texte_39_2016_repraesentative_erhebung_von_pro-kopf-verbraeuchen_natuerlicher_ressourcen.pdf
        """
        """
        The variable actualdemand is a float variable that denotes the carbon allowance demand per household.
        It is calcualted differently for the first time period in contrast to all other time periods.
        """
        self.selling = None
        """
        The variable selling is a boolean variable that denotes whether the household sold allowances or bought allowances
        """
        self.investing = None
        """
        The variable investing is a boolean variable that denotes whether the household invests in carbon abatement technologies or not.
        """
        self.income_spent = 0.0
        """
        The variable income_spent is a float variable that denotes how much income the household spends on carbon abatement technologies. 
        """
        
        
        
    def calc_actualdemand_t0(self, avg_demand):
        """Compute demand in first time step

        The actualdemand variable in the first time period is calculated as the difference between the demand for allowances of the household (variable: demand) and the initially assigned allowances.
        The assumption here is that the initial allowance assignment is the average allowance demand of all households. 

        Parameters
        ----------
        avg_demand : float
            Average demand of all households
        """
                                  
        self.actualdemand = (self.demand - avg_demand)
        print(self.actualdemand)
        if self.actualdemand > 0:
            print("I gotta work on my carbon footprint!")
        elif self.actualdemand < 0:
            print("I am already soooo ecofriendly!")
        elif self.actualdemand == 0:
            print("Just about right!")
        else:
            print("Something had gone wrong!")
    
    def calc_actualdemand_ti(self, avg_demand, percentreducallow):
        """
        The actualdemand variable in all other time periods is calculated as the difference between the demand for allowances of the household (variable: demand) and the a percentage of the initially assigned allowances.
        The percentage of the decrease of allocated allowances can be set by the modeler. 
        """
        self.percentreducallow = 0.01
        """
        percentreducallow is the percantage of how much the total amount of allowances is reduced per each year 
        Reasonable values here are 0 up to 5%, depending on how much is being allowed at the beginning. 
        It can arbitrarily be chosen by the modeler. 
        The default setting is 1%.
        """
        AllowanceAssignment = avg_demand - (avg_demand * percentreducallow)
        
        self.actualdemand = self.demand - AllowanceAssignment
        print(self.actualdemand)        
        if self.actualdemand > 0:
            print ("I gotta work on my carbon footprint!")
        elif self.actualdemand < 0:
            print ("I am already soooo ecofriendly!")
        elif self.actualdemand == 0:
            print ("Just about right!")
        else:
            print ("Something had gone wrong!")
        
        
        """
        Implicit assumption here: Households FIRST decide whether they sell or buy allowances and only then think about investement.
        This is important because the sell/buy decision has an impact on the investment decision. 
        Also: there is the implicit assumption that the carbon allowances budget is always 0 after each time period, that is carbon allowances cannot be safed or transfered to the next time step.
        """        
#TODO erkläre warum anders        
    def decide_sellbuy_t0(self):
        """
        Households decide whether they sell or buy allowances.
        Factors are: actualdemand, socioecol, econ
        """
        startprice = 0.2
        """
        startprice is a float variable that denotes the initial price for one unit of carbon allowances.
        it can arbitrarily be chosen by the modeler. 
        The default setting is 0.02 Euro
        """
        if self.actualdemand > 0:
            print("I need to buy allowances!")
            self.selling = False
        elif self.actualdemand < 0:
            print("I want to sell allowances!")
            self.selling = True
        else:
            print("I did nothing...") 
            self.selling = None
        
         
        """
        Households buy exactly as many carbon allowances as they need to cover their demand.
        OR
        Households sell all their affluent carbon allowances.
        """
        if self.selling == False:
           loss = self.actualdemand * startprice
           self.income = self.income - loss
           self.actualdemand = 0.0
           print("I bought allowances!")
        elif self.selling == True:
           profit = (0 - self.actualdemand) * startprice
           self.income = self.income + profit
           print("I sold allowances!")
           self.actualdemand = 0.0
        else:
            self.selling == None
            print("I neither bought nor sold! ")     
        
    
 #TODO Explain   
    def decide_sellbuy(self, price):
        """
        Households decide whether they sell or buy allowances.
        Factors are: actualdemand, socioecol, econ
        """
        if self.actualdemand > 0:
            print("I need to buy allowances again!")
            self.selling = False
        elif self.actualdemand < 0:
            print("I want to sell allowances again!")
            self.selling = True
        else:
            print("I did nothing...") 
            self.selling = None
        
         
        """
        Households buy exactly as many carbon allowances as they need to cover their demand.
        OR
        Households sell all their affluent carbon allowances.
        """
        if self.selling == False:
           loss = self.actualdemand * price
           self.income = self.income - loss
           self.actualdemand = 0.0
           print("I bought allowances!")
        elif self.selling == True:
           profit = (0 - self.actualdemand) * price
           self.income = self.income + profit
           print("I sold allowances!")
           self.actualdemand = 0.0
        else:
            self.selling == None
            print("I neither bought nor sold! ")
         
        
        """
        Implicit assumption here: households can only change their demand through investments in carbon abatement technologies. 
        """

    def decide_investsave(self):
        """
        Households decide whether they invest money in carbon abatement technologies or save money.
        """
        ipercent = 0.1
        """
        The variable ipercent is *not randomly* assigned, but arbitraily chosen by the modeler.
        ipercent is a float variable that denotes the income that can be spend on carbon reduction and/or allowances for each household 
        The default setting is 1%
        """
        if self.income > 0:
            if self.selling == True: 
                if self.econ > 0.6 and self.socioecol > 0.6:
                    print("I want to invest in carbon abatement technology!")
                    self.investing = True
                elif self.econ > 0.6 and self.socioecol < 0.6:
                    print("I want to save my cash...")
                    self.investing = False
                elif self.econ < 0.6 and self.socioecol > 0.6:
                    print("I want to invest in carbon abatement technologies!")
                    self.investing = True
                elif self.econ < 0.6 and self.socioecol < 0.6:
                    print("I want to save my cash...")
                    self.investing = False
                    
                else:
                    print("Something went wrong!")
            elif self.selling == False:
                if self.econ > 0.6 and self.socioecol > 0.6:
                    print("I want to invest in carbon abatement technologies!")
                    self.investing = True
                elif self.econ > 0.6 and self.socioecol < 0.6:
                    print("I want to invest in carbon abatement technologies!")
                    self.investing = True
                elif self.econ < 0.6 and self.socioecol > 0.6:
                    print("I want to invest in carbon abatement technologies!")
                    self.investing = True
                elif self.econ < 0.6 and self.socioecol < 0.6:
                    print("I want to save my cash...")
                    self.investing = False
            else:
                print("I dont know whether I sold or bought allowances...")
        else:
            print("I am bankrupt! Help!")
            self.investing = None
        """
        Households invest in carbon abatement technologies (more sufficient supplies or PV/Solar-Power, etc.).
        Demand for carbon allowances will thus be lower in the next time step.
        The assumption here is that an investment of ipercent of the income will reduce the demand for carbon allowances by 2%, which is an arbirarily chosen number.
        Further work on this code could include research-based evidence for this claim and change the arbirarily chosen 2% to a higher/lower number. 
        Households save their money and thus their demand does not change.
        Only high income households can allow not to change their demand; low income households cannot make any debt and thus "die" 
        """
        if self.investing == True:
            self.income_spent = self.income * ipercent 
            self.income = self.income - self.income_spent 
            self.demand = self.demand - (self.demand * 0.02)
            print("I invested money, yeah!")
        elif self.investing == False:
            self.income = self.income
            self.actualdemand = self.actualdemand
            print("I saved money, juhu!")
        else:
            self.investing == None
            print("I neither invested nor saved...")
            
        