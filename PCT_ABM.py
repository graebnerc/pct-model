# -*- coding: utf-8 -*-
"""
**************************Personal Carbon Trading******************************

Agent-based model translated from NetLogo to Python.

WORK IN PROGRESS

Make sure to adapt the model according to your prefrerences, this especially includes:
    1) ipercent 
    2) start price 
# TODO der Rest der einstellbaren Variablen 
"""

import random
import math
import statistics
import numpy as np

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
        # self.actualdemand = self.calc_actualdemand_t0() # TODO Das sollte nicht in der init Funktion stehen (siehe Ergänzung in Modell Klasse)
        """
        The variable actualdemand is a float variable that denotes the carbon allowance demand per household.
        It is calcualted differently for the first time period in contrast to all other time periods.
        """
        self.selling = selling # TODO Diese Variable ist noch nicht definiert worden
        """
        The variable selling is a boolean variable that denotes whether the household sold allowances or bought allowances
        """
        self.income_spent = income_spent # TODO Diese Variable ist noch nicht definiert worden
        """
        The variable income_spent is a float variable that denotes how much income the household spends on carbon abatement technologies. 
        """
        self.ipercent = 0.1
        """
        The variable ipercent is *not randomly* assigned, but arbitraily chosen by the modeler.
        ipercent is a float variable that denotes the income that can be spend on carbon reduction and/or allowances for each household 
        The default setting is 1%
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
        InitialAllowanceAssignment = avg_demand
                                
        self.actualdemand = self.demand - InitialAllowanceAssignment
        if self.actualdemand < 0:
            print ("I gotta work on my carbon footprint!")
        elif self.actualdemand > 0:
            print ("I am already soooo ecofriendly!")
        elif self.actualdemand == 0:
            print ("Just about right!")
        else:
            print ("Something had gone wrong!")
    
    def calc_actualdemand_ti(self, demand, percentreducallow):
        """
        The actualdemand variable in all other time periods is calculated as the difference between the demand for allowances of the household (variable: demand) and the a percentage of the initially assigned allowances.
        The percentage of the decrease of allocated allowances can be set by the modeler. 
        """
        AllowanceAssignment = InitialAllowanceAssignment - InitialAllowanceAssignment*percentreducallow
        
        self.actualdemand = self.demand - AllowanceAssignment
        if self.actualdemand < 0:
            print ("I gotta work on my carbon footprint!")
        elif self.actualdemand > 0:
            print ("I am already soooo ecofriendly!")
        elif self.actualdemand == 0:
            print ("Just about right!")
        else:
            print ("Something had gone wrong!")
        
        
        """
        Implicit assumption here: Households FIRST decide whether they sell or buy allowances and only then think about investement.
        This is important because the sell/buy decision has an impact on the investment decision. 
        """        
    def sell(self, actualdemand, income, selling):
        """
        This is a function that makes households sell all their affluent carbon allowances.
        """
        profit = self.actualdemand * m_startprice
        m_allocation = m_allocation + self.actualdemand
        self.income = self.income + profit
        self.actualdemand = 0 
        self.selling = True
        #TODO funktioniert das so?! Besonders in Bezug auf den Markt?
        #TODO denn: m_startprice und m_allocation sind Charakteristika der Klasse Markt
    def buy(self, actualdemand, income, selling):
        """
        This is a function that makes households buy exactly as many carbon allowances as they need to cover their demand.
        """
        loss = self.actualdemand * m_startprice
        m_allocation = m_allocation - self.actualdemand
        self.income = self.income - loss
        self.actualdemand = 0
        self.selling = False
        #TODO funktioniert das so?! Besonders in Bezug auf den Markt? Spiegelverkehrt zu Buy?!         
    def decide_sellbuy(self, actualdemand, sell, buy):
        """
        Households decide whether they sell or buy allowances.
        Factors are: actualdemand, socioecol, econ
        """
        if self.actualdemand > 0:
            self.sell(self.actualdemand, self.sell, self.buy) 
        if self.actualdemand < 0:
            self.buy(self.actualdemand, self.sell, self.buy)
        else:
            print("I did nothing")
   

        """
        Implicit assumption here: households can only change their demand through investments in carbon abatement technologies. 
        """
    def invest(self, income_spent, income, ipercent, actualdemand):
        """
        Households invest in carbon abatement technologies (more sufficient supplies or PV/Solar-Power, etc.).
        Demand for carbon allowances will thus be lower in the next time step.
        """
        self.income_spent = self.income * ipercent 
        self.income = self.income - self.income_spent 
        self.actualdemand = self.actualdemand * 0.02
        """
        The assumption here is that an investment of ipercent of the income will reduce the demand for carbon allowances by 2%, which is an arbirarily chosen number.
        Further work on this code could include research-based evidence for this claim and change the arbirarily chosen 2% to a higher/lower number. 
        """
           
    def save(self, income, actualdemand):
        """
        Households save their money and thus their demand does not change.
        Only high income households can allow not to change their demand; low income households cannot make any debt and thus "die" 
        """
        self.income = self.income
        self.actualdemand = self.actualdemand
        #TODO have a line of code that lets Households die  !!!      
    
    def decide_investsave(self, selling, socioecol, econ):
        """
        Households decide whether they invest money in carbon abatement technologies or save money.
        """
        if selling == True: 
            if self.econ > 0.6 and self.socioecol > 0.6:
                self.invest(self.income_spent, self.income, self.ipercent, self.actualdemand)
            elif self.econ > 0.6 and self.socioecol < 0.6:
                self.save(self.income, self.actualdemand)
            elif self.econ < 0.6 and self.socioecol > 0.6:
                self.invest(self.income_spent, self.income, self.ipercent, self.actualdemand)
            elif self.econ < 0.6 and self.socioecol < 0.6:
                self.save(self.income, self.actualdemand)
            else:
                print("Something went wrong!")
        elif selling == False:
            if self.econ > 0.6 and self.socioecol > 0.6:
                self.invest(self.income_spent, self.income, self.ipercent, self.actualdemand)
            elif self.econ > 0.6 and self.socioecol < 0.6:
                self.invest(self.income_spent, self.income, self.ipercent, self.actualdemand)
            elif self.econ < 0.6 and self.socioecol > 0.6:
                self.invest(self.income_spent, self.income, self.ipercent, self.actualdemand)
            elif self.econ < 0.6 and self.socioecol < 0.6:
                self.save(self.income, self.actualdemand)
        else:
            print("I dont know whether I sold or bought allowances")
     
class Market: 
    """
    This is the Carbon Allowance Market
    """
    def __init__(self, m_allocation, m_price, percentreducallow, startprice):
        self.m_allocation = m_allocation
        """
        m_allocation is a float variable that denots the total amount of available carbon allowances on the market.
        It is especially used in the sell/buy function.
        """
        m_price = m_price
        """
        m_price is a float variable that denots the market price for one unit of carbon allowances.
        It is especially used in the sell/buy function.
        """
        self.percentreducallow = 0.01
        """
        percentreducallow is the percantage of how much the total amount of allowances is reduced per each year 
        Reasonable values here are 0 up to 5%, depending on how much is being allowed at the beginning. 
        It can arbitrarily be chosen by the modeler. 
        The default setting is 1%.
        """
        self.startprice = 0.02 
        """
        startprice is a float variable that denotes the initial price for one unit of carbon allowances.
        it can arbitrarily be chosen by the modeler. 
        The default setting is 0.02 Euro
        """
        #TODO wie wird der Marktpreis errechnet? 
    
    def calc_allocation(self, m_allocation):
        """
        This is a function that sums up all the allowances that are took to or from the market aka sold or bought at the market.
        """
        #m_allocation = m_allocation
        
        #m_allocation = sum(value["actualdemand"] for value in all_households)
        
    def calc_price(self, m_price):
        """
        This is a function that calculates the market price for allowances for the next time step. 
        """
        
        
        
"""
Das ist eine Lösung für die Bevölkerung des Models
"""
"""
n = range(1, 101) # 100 Haushalte werden erzeugt

all_households = [] # Leere Liste erzeugen, in welcher die einzelnen Haushalte gespeichert werden

for i in n:
    single_household = {} # Für jeden einzelnen Haushalt wird ein Dictionary erzeugt. Dadurch können wir dann über ihre Namen auf die einzelnen Werte zugreifen.
    household = Household(0, 0, 0, 0, 0, 0, 0, 0, 0)
    single_household["numpers"] = household.numpers
    single_household["income"] = household.income
    single_household["socioecol"] = household.socioecol
    single_household["econ"] = household.econ
    single_household["actualdemand"] = household.actualdemand
    single_household["demand"] = household.demand
    single_household["selling"] = household.selling
    single_household["income_spent"] = household.income_spent
    single_household["ipercent"] = household.ipercent
    
    all_households.append(single_household) # Die Werte für das eben erzeugte "Household"-Objekt werden der Liste hinzugefügt.
    
all_households

sum_all_persons = sum(value["numpers"] for value in all_households) # Die Werte für "numpers" in allen Haushalten werden aufaddiert 
sum_all_demand = sum(value["demand"] for value in all_households)
"""

class Model:
    """
    This is a class i the instance of a single model as described in the paper.
    
    1. Create Households
    2. Create Market
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
        avg_demand = np.mean([h.demand for h in self.list_of_households])
        for h in self.list_of_households:
            h.calc_actual_demand_t0(avg_demand)
        
    def run(self):
        for i in range(self.t_steps):
            print("Time step: {}".format(i))
            # compute allowences
            #for j in self.list_of_households:
            #    j.calc_actualdemand_ti()
    
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
        

        
# example_model = Model(nb_h=100)

#TODO Fehlt noch: Time ticks einbauen und Aktionen pro Phase machen 