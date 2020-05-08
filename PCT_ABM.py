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
    
    def __init__(self, numpers, income, socioecol, econ, ipercent):
        """
        This is a method that ascribes *random* parameters to the households.
        Those parameters are:
        - Number of Persons living in the Household (Integer)
        - Income (Integer)
             incseq is a list of integers from which the monthly income is randomly drawn
        - Socioecological Motiviation (Float)
        - Economic Motivation (Float)
        """
        
        self.numpers = random.randrange(1, 4)
        """
        The implicit assumption for Number of Persons per Household is a uniform distribution.
        Thus, household with 5 Members are as likely as households with 1, 2 or 3 Members, which most likely does not resemble the German population. 
        Further work on this code could include a left skewed distribution. 
        """
        incseq = (500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000)
        self.income = random.choice(incseq)
        """
        The implicit assumption for income is a uniform distribution.
        Thus, household with 500 Euros income are as likely as households with 5000 or more Euros income, which most likely does not resemble the German income distribution.
        Further work on this code could include a left skewed distribution. 
        """
        self.socioecol = random.random()
        self.econ = random.random()
        """
        socioecol and econ are variables that denote the socioecological and economical motivation of households in %.
        """
        
        
        """
        The variables ipercent and demand are *not randomly* assigned.
        """
        
        self.ipercent = 0.1
        """
        ipercent is a variable that denotes the income that can be spend on carbon reduction and/or allowances for each household 
        it can arbitrarily be chosen by the modeler. 
        The default setting is 1%
        """
#AB HIER WIRDS KRAUT UND RÜBEN!
    def calcdemand(self, numpers, income, actualdemand):
        """
        demand is a variable that denotes the demand for 
        The function is retrieved from Seidl [2018]
        It is a rough estimate for the demand per household from Federal Environment Office (2016), page 65.
        Link:  https://www.umweltbundesamt.de/sites/default/files/medien/378/publikationen/texte_39_2016_repraesentative_erhebung_von_pro-kopf-verbraeuchen_natuerlicher_ressourcen.pdf
        """    
        self.demand  = (1.1 - numpers * 0.05) * (math.log(math.log(income)) - 0.9) * 20278.0 * numpers * (0.8 + 0.4) * 0.527
        #hhier bekomme ich bis jetzt immer eine Fehlermeldung - print(Anna.calcdemand(2,6000))  gibt das Output None.        
        """
        actualdemand is a variable that denotes the initial demand for carbon allowances in the first time period.
        It will then updated in each time period. 
        The actualdemand variable is calculated as the difference between the demand for allowances of the household (i) and the assigned allowances (ii).
            (i) demand for allowances:
                The function is retrieved from Seidl [2018]
                It is a rough estimate for the demand per household from Federal Environment Office (2016), page 65.
                Link:  https://www.umweltbundesamt.de/sites/default/files/medien/378/publikationen/texte_39_2016_repraesentative_erhebung_von_pro-kopf-verbraeuchen_natuerlicher_ressourcen.pdf
            (ii) assigned allowances: 
                The assumption here is that the initial allowance assignment equals the average allowance demand of all households. 
        """
        #Ab hier wird  es etwas unübersichtlich - ich weiß nicht, ob die Idee, die ich hatte funktioniert.
        list_numpers = [] #TODO wie kann ich hier eine Liste erstellen, bei der die Elemente die Personenanzahl jedes einzelnen Haushalts ist?  
        NumPers = sum(list_numpers)
                
        list_demand = [] #TODO wie kann ich hier eine Liste erstellen, bei der die Elemente der errechnete Demand jedes einzelnen Haushalts ist?  
        Demand = sum(list_demand)
        BeginDemand = Demand / NumPers 
                                
        self.actualdemand = demand - BeginDemand
        # TODO C: Hier wurde ohne Grund eingerueckt und damit ein Fehler verursacht; zudem muss print mit Klammern als Funktion verwendet werden (wir sind ja Python 3)
        if actualdemand < 0:
            print("I gotta work on my carbon footprint!")
        elif actualdemand > 0:
            print("I am already soooo ecofriendly!")
        elif actualdemand == 0: # TODO C: Tests auf Gleichheit mit '==' nicht '='
            print("Just about right!")
        else:
            print("Something had gone wrong!")
        #TODO overwrite demand von oben, damit der neue Demand eine eigenchaft  
        
        """
        Implicit assumption here: Households FIRST decide whether they sell or buy allowances and only then think about investement.
        This is important because the sell/buy decision has an impact on the investment decision. 
        """
        # TODO Bei den Funktion im Folgenden hast du bei der Definition immer 'self' als erstes Argument vergessen
        def decide_sellbuy(self):
            """
            Households decide whether they sell or buy allowances.
            Factors are: actualdemand, socioecol, econ
            """
            if actualdemand > 0: # TODO C Wenn hier das oben in Zeile 95 gemeinte actualdemand gemeint ist musst du schreiben: self.actualdemand
                sell 
            if actualdemand <0:
                buy
            else:
                print("I did nothing")
        # TODO C Bei den nächsten beiden Funktionen ist sold und bought nicht definiert
        def sell(self):
            """
            This is a function that makes households sell all their affluent carbon allowances.
            """
            #TODO this will have to do with the market! 
            #TODO der Haushalt muss sich das merken und dann eine Eigenschanft haben, der beschreibt dass diese Aktion gemacht wurde:
            sold
            
        def buy(self):
            """
            This is a function that makes households buy exactly as many carbon allowances as they need to cover their demand.
            """
            # TODO this will have to do with the market! 
            #TODO der Haushalt muss sich das merken und dann eine Eigenschanft haben, der beschreibt dass diese Aktion gemacht wurde: 
            bought
            
            
        """
        Implicit assumption here: households can only change their demand through investments in carbon abatement technologies. 
        """
        def decide_investsave():
            """
            Households decide whether they invest money in carbon abatement technologies or save money.
            """
            # TODO C: die Variablen sold and bought, econ und socioecol sind hier nicht definiert; wahrscheinlich willst du self.econ, self.socioecol etc. verwenden, weil es ja in init definiert Klassenattribute sind?
            #TODO klären ob ich die econ und socioecol so in ein IfStatement packen kann
            # TODO C: Es sollten ja "und" Tests sein, also ob econ > 0.6 UND socioecol >0.6 oder? Dann muss man das so machen:
            if sold:
                if (econ > 0.6) and (socioecol > 0.6):
                    invest
                elif (econ > 0.6) and (socioecol < 0.6):
                    save
                elif (econ < 0.6) and (socioecol > 0.6):
                    invest
                elif (econ < 0.6) and (socioecol < 0.6):
                    save
                else:
                    print("Do you know what my motivation is?!")
            # TODO C: Hier auch wie oben anpassen
            if bought: 
                if (econ > 0.6) and (socioecol > 0.6):
                    invest
                elif (econ > 0.6) and (socioecol < 0.6):
                    invest
                elif (econ < 0.6) and (socioecol > 0.6):
                    invest
                elif (econ < 0.6) and (socioecol < 0.6):
                    save
                else:
                    print("Do you know what my motivation is?!")
            else:
                print("I dont know whether I sold or bought allowances")
        
        def invest():
            """
            Households invest in carbon abatement technologies (more sufficient supplies or PV/Solar-Power)
            """
            #TODO was passiert: die Haushalte haben weniger Einkommen, d.h. sie  geben all ihr verfügbares Einkommen aus (ipercent) und haben im nächsten Monat weniger Demand (Faktor ausdenken!)
            
        def save():
            """
            Households save their money and thus their demand does not change.
            Only high income households can allow not to change their demand; low income households cannot make any debt and thus "die" 
            """
            #TODO was passiert: Einkommen steigt, Demand bleibt gleich im nächsten Monat.
class Market: 
    """
    This is the Carbon Allowance Market
    """
    def __init__(self, allowallocation, percentreducallow, startprice, n_households):
        self.allowallocation = allowallocation
        """
        percentreducallow is the percantage of how much the total amount of allowances is reduced per each year 
        Reasonable values here are 0 up to 5%, depending on how much is being allowed at the beginning. 
        It can arbitrarily be chosen by the modeler. 
        The default setting is 1%
        """
        self.percentreducallow = 0.1
        """
        startprice is the initial price for one unit of carbon allowances.
        it can arbitrarily be chosen by the modeler. 
        The default setting is 0.02 Euro
        """
        self.startprice = 0.02 
        
        """
        Call the new method to create the households
        """
        self.households = self.setup_households(n_households)
        
    def setup_households(self, nb_of_hh):
        """Creates the households

        This function should be called via the `__init__` function
        of the class `Market`. It creates the number of households.

        Parameters
        ----------
        nb_of_hh : int
            The number of households to be created
        """
        # TODO C: Hier musst du noch die Startwerte fur die Haushalte eintragen und damit die None Werte ersetzen. Diese sind ja v.a. Parameter, sollten also irgendwo am Anfang festgelegt werden
        households = [Household(numpers=None, income=None, 
                                socioecol=None, econ=None, 
                                ipercent=None) for i in range(nb_of_hh)]
        return households
 
#Fehlt noch: Model mit n Haushalten bevölkern
#Fehlt noch: Time ticks einbauen und Aktionen pro Phase machen 