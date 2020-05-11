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

class Household:
    """
    This is a class of Households.
    """
    def __init__(self, numpers, income, socioecol, econ, actualdemand, demand, selling, income_spent, ipercent):
        """
        This is a method that ascribes *random* parameters to the households.
        """
        
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
        self.actualdemand = actualdemand 
        """
        The variable actualdemand is a float variable that denotes the carbon allowance demand per household.
        """
        self.demand = (1.1 - self.numpers * 0.05) * (math.log(math.log(self.income)) - 0.9) * 20278.0 * self.numpers * (0.8 + 0.4) * 0.527
        """
        The variable demand is a float that denotes how much carbon allowances one household demands in accordance to its number of persons and income.
        The function is retrieved from Seidl [2018]
        It is a rough estimate for the demand per household from Federal Environment Office (2016), page 65.
        Link:  https://www.umweltbundesamt.de/sites/default/files/medien/378/publikationen/texte_39_2016_repraesentative_erhebung_von_pro-kopf-verbraeuchen_natuerlicher_ressourcen.pdf
        """
        self.selling = selling
        """
        The variable selling is a boolean variable that denotes whether the household sold allowances or bought allowances
        """
        self.income_spent = income_spent
        """
        The variable income_spent is a float variable that denotes how much income the household spends on carbon abatement technologies. 
        """
        self.ipercent = 0.1
        """
        The variable ipercent is *not randomly* assigned, but arbitraily chosen by the modeler.
        ipercent is a float variable that denotes the income that can be spend on carbon reduction and/or allowances for each household 
        The default setting is 1%
        """
        
        
    def calc_actualdemand(self, demand):    
        """
        actualdemand is a variable that denotes the initial demand for carbon allowances in the first time period.
        It will then updated in each time period. 
        The actualdemand variable is calculated as the difference between the demand for allowances of the household (variable: demand) and the initially assigned allowances.
        The assumption here is that the initial allowance assignment is the average allowance demand of all households. 
        """
        InitialAllowanceAssignment = sum_all_demand / sum_all_persons 
                                
        self.actualdemand = self.demand - InitialAllowanceAssignment
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
        #TODO does this then this then refer here to the next time step?
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
        #TODO was passiert: eigentlich ja nichts, denn das Einkommen steigt ja schon in der sell/buy function, Demand bleibt gleich im nächsten Monat.
        #TODO macht die Funktion dann das was ich möchte? 
        #TODO have a line of code that lets Households die  !!!      
    
    def decide_investsave(self, selling, socioecol, econ):
        """
        Households decide whether they invest money in carbon abatement technologies or save money.
        """
        if selling == True: 
            if self.econ > 0.6 and self.socioecol > 0.6:
                self.invest
            elif self.econ > 0.6 and self.socioecol < 0.6:
                self.save
            elif self.econ < 0.6 and self.socioecol > 0.6:
                self.invest
            elif self.econ < 0.6 and self.socioecol < 0.6:
                self.save
            else:
                print("Something went wrong!")
        elif selling == False:
            if self.econ > 0.6 and self.socioecol > 0.6:
                self.invest
            elif self.econ > 0.6 and self.socioecol < 0.6:
                self.invest
            elif self.econ < 0.6 and self.socioecol > 0.6:
                self.invest
            elif self.econ < 0.6 and self.socioecol < 0.6:
                self.save
        else:
            print("I dont know whether I sold or bought allowances")
       #TODO stimmt das so mit den if/elif/else statements?  
     
class Market: 
    """
    This is the Carbon Allowance Market
    """
    def __init__(self, m_allocation, percentreducallow, startprice, m_price):
        self.m_allocation = m_allocation
        """
        m_allocation is a float variable that denots the total amount of available carbon allowances on the market.
        It is especially used in the sell/buy function.
        """
        self.percentreducallow = 0.1
        """
        percentreducallow is the percantage of how much the total amount of allowances is reduced per each year 
        Reasonable values here are 0 up to 5%, depending on how much is being allowed at the beginning. 
        It can arbitrarily be chosen by the modeler. 
        The default setting is 1%
        """
        self.startprice = 0.02 
        """
        startprice is a float variable that denotes the initial price for one unit of carbon allowances.
        it can arbitrarily be chosen by the modeler. 
        The default setting is 0.02 Euro
        """
        m_price = m_price
        """
        m_price is a float variable that denots the market price for one unit of carbon allowances.
        It is especially used in the sell/buy function.
        """
        #TODO wie wird der Marktpreis errechnet? 


"""
Das ist eine Lösung für die Bevölkerung des Models
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


#TODO Fehlt noch: Time ticks einbauen und Aktionen pro Phase machen 