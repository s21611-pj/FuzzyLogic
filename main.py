"""
Authors: Paweł Badysiak (s21166), Wojciech Turek (s21611)
How to run:
Install:
1. todo
2. todo
After instalation:
    todo
"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(50, 0, 10), 'temperature')
humidity = ctrl.Antecedent(np.arange(100, 0, 20), 'humidity')
atmospheric_pressure = ctrl.Antecedent(np.arange(870, 1089, 73), 'atmospheric_pressure')

alcohol_solution = ctrl.Consequent(np.arange(100, 10, 10), 'alcohol_solution')

alcohol_solution['10%'] = fuzz.trimf(alcohol_solution.universe, [90, 100, 100])
alcohol_solution['20%'] = fuzz.trimf(alcohol_solution.universe, [80, 90, 100])
alcohol_solution['30%'] = fuzz.trimf(alcohol_solution.universe, [70, 80, 90])
alcohol_solution['40%'] = fuzz.trimf(alcohol_solution.universe, [60, 70, 80])
alcohol_solution['50%'] = fuzz.trimf(alcohol_solution.universe, [50, 60, 70])
alcohol_solution['60%'] = fuzz.trimf(alcohol_solution.universe, [40, 50, 60])
alcohol_solution['70%'] = fuzz.trimf(alcohol_solution.universe, [30, 40, 50])
alcohol_solution['80%'] = fuzz.trimf(alcohol_solution.universe, [20, 30, 40])
alcohol_solution['90%'] = fuzz.trimf(alcohol_solution.universe, [10, 20, 30])
alcohol_solution['100%'] = fuzz.trimf(alcohol_solution.universe, [10, 10, 20])

temperature.view()
humidity.view()
atmospheric_pressure.view()

alcohol_solution['50%'].view()

# temp:
    # freezing
    # extremely - cold
    # very - cold
    # cold
    # fairly - cold


# humidity:
    # sticky
    # humid
    # comfortable
    # refreshing
    # dry

# pressure:
    # low
    # medium
    # high

rule1 = ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule2 = ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule3 = ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule4 = ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule5 = ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule6 = ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule7 = ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule8 = ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule9 = ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule10 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule11 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule12 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule13 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule14 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule15 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['high'], alcohol_solution['100%'])

rule16= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule17= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule18= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule19= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule20= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule21= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule22= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule23= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule24= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule25 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule26 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule27 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule28 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule29 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule30 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['high'], alcohol_solution['100%'])

rule31= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule32= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule33= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule34= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule35= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule36= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule37= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule38= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule39= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule40 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule41 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule42 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule43 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule44 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule45 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['high'], alcohol_solution['100%'])

rule46= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule47= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule48= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule49= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule50= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule51= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule52= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule53= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule54= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule55 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule56 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule57 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule58 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule59 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule60 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['high'], alcohol_solution['100%'])

rule61= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule62= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule63= ctrl.Rule(temperature['freezing'] | humidity['sticky'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule64= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule65= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule66= ctrl.Rule(temperature['freezing'] | humidity['humid'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule67= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule68= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule69= ctrl.Rule(temperature['freezing'] | humidity['comfortable'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule70 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule71 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule72 =ctrl.Rule(temperature['freezing'] | humidity['refreshing'] | atmospheric_pressure['high'], alcohol_solution['100%'])
rule73 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['low'], alcohol_solution['100%'])
rule74 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['medium'], alcohol_solution['100%'])
rule75 =ctrl.Rule(temperature['freezing'] | humidity['dry'] | atmospheric_pressure['high'], alcohol_solution['100%'])




"""
    00-10 st -> 20%
    10-20 st -> 30%
    20-30 st -> 40%
    30-40 st -> 50%
    
    inputs:
        1. temperatura 50-0 co 5
        2. wilgotnosc powwietrza 100-0 co 10
        3. cinienie atmosferyczne 870-1090 co 22 
            im wyzsze cisneinei tym woda ciezej zamarza
    output:
        ile % roztwor 100-10% co 10
        
        temp:
            freezing
            extremely-cold
            very-cold
            cold
            fairly-cold
            
        humidity:
            dry
            refreshing
            comfortable
            humid
            sticky
            
        pressure:
            low
            medium
            high

        

"""

