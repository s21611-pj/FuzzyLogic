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

temperature = ctrl.Antecedent(np.arange(0, 50, 10), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 100, 20), 'humidity')
atmospheric_pressure = ctrl.Antecedent(np.arange(870, 1089, 73), 'atmospheric_pressure')
alcohol_solution = ctrl.Consequent(np.arange(00, 100, 10), 'alcohol_solution')

temperature.automf(5)
humidity.automf(5)
atmospheric_pressure.automf(3)

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


rule1 = ctrl.Rule(temperature['good'] | humidity['good'] | atmospheric_pressure['poor'], alcohol_solution['100%'])
rule2 = ctrl.Rule(temperature['good'] | humidity['good'] | atmospheric_pressure['average'], alcohol_solution['100%'])
rule3 = ctrl.Rule(temperature['good'] | humidity['good'] | atmospheric_pressure['good'], alcohol_solution['100%'])
rule4 = ctrl.Rule(temperature['good'] | humidity['decent'] | atmospheric_pressure['poor'], alcohol_solution['100%'])
rule5 = ctrl.Rule(temperature['good'] | humidity['decent'] | atmospheric_pressure['average'], alcohol_solution['100%'])
rule6 = ctrl.Rule(temperature['good'] | humidity['decent'] | atmospheric_pressure['good'], alcohol_solution['100%'])
rule7 = ctrl.Rule(temperature['good'] | humidity['average'] | atmospheric_pressure['poor'], alcohol_solution['100%'])
rule8 = ctrl.Rule(temperature['good'] | humidity['average'] | atmospheric_pressure['average'], alcohol_solution['100%'])
rule9 = ctrl.Rule(temperature['good'] | humidity['average'] | atmospheric_pressure['good'], alcohol_solution['100%'])
rule10 = ctrl.Rule(temperature['good'] | humidity['mediocre'] | atmospheric_pressure['poor'], alcohol_solution['100%'])
rule11 = ctrl.Rule(temperature['good'] | humidity['mediocre'] | atmospheric_pressure['average'], alcohol_solution['100%'])
rule12 = ctrl.Rule(temperature['good'] | humidity['mediocre'] | atmospheric_pressure['good'], alcohol_solution['100%'])
rule13 = ctrl.Rule(temperature['good'] | humidity['poor'] | atmospheric_pressure['poor'], alcohol_solution['100%'])
rule14 = ctrl.Rule(temperature['good'] | humidity['poor'] | atmospheric_pressure['average'], alcohol_solution['100%'])
rule15 = ctrl.Rule(temperature['good'] | humidity['poor'] | atmospheric_pressure['good'], alcohol_solution['100%'])

rule16 = ctrl.Rule(temperature['decent'] | humidity['good'] | atmospheric_pressure['poor'], alcohol_solution['80%'])
rule17 = ctrl.Rule(temperature['decent'] | humidity['good'] | atmospheric_pressure['average'], alcohol_solution['80%'])
rule18 = ctrl.Rule(temperature['decent'] | humidity['good'] | atmospheric_pressure['good'], alcohol_solution['80%'])
rule19 = ctrl.Rule(temperature['decent'] | humidity['decent'] | atmospheric_pressure['poor'], alcohol_solution['80%'])
rule20 = ctrl.Rule(temperature['decent'] | humidity['decent'] | atmospheric_pressure['average'], alcohol_solution['80%'])
rule21 = ctrl.Rule(temperature['decent'] | humidity['decent'] | atmospheric_pressure['good'], alcohol_solution['80%'])
rule22 = ctrl.Rule(temperature['decent'] | humidity['average'] | atmospheric_pressure['poor'], alcohol_solution['80%'])
rule23 = ctrl.Rule(temperature['decent'] | humidity['average'] | atmospheric_pressure['average'], alcohol_solution['80%'])
rule24 = ctrl.Rule(temperature['decent'] | humidity['average'] | atmospheric_pressure['good'], alcohol_solution['80%'])
rule25 = ctrl.Rule(temperature['decent'] | humidity['mediocre'] | atmospheric_pressure['poor'], alcohol_solution['80%'])
rule26 = ctrl.Rule(temperature['decent'] | humidity['mediocre'] | atmospheric_pressure['average'], alcohol_solution['80%'])
rule27 = ctrl.Rule(temperature['decent'] | humidity['mediocre'] | atmospheric_pressure['good'], alcohol_solution['80%'])
rule28 = ctrl.Rule(temperature['decent'] | humidity['poor'] | atmospheric_pressure['poor'], alcohol_solution['80%'])
rule29 = ctrl.Rule(temperature['decent'] | humidity['poor'] | atmospheric_pressure['average'], alcohol_solution['80%'])
rule30 = ctrl.Rule(temperature['decent'] | humidity['poor'] | atmospheric_pressure['good'], alcohol_solution['80%'])

rule31 = ctrl.Rule(temperature['average'] | humidity['good'] | atmospheric_pressure['poor'], alcohol_solution['60%'])
rule32 = ctrl.Rule(temperature['average'] | humidity['good'] | atmospheric_pressure['average'], alcohol_solution['60%'])
rule33 = ctrl.Rule(temperature['average'] | humidity['good'] | atmospheric_pressure['good'], alcohol_solution['60%'])
rule34 = ctrl.Rule(temperature['average'] | humidity['decent'] | atmospheric_pressure['poor'], alcohol_solution['60%'])
rule35 = ctrl.Rule(temperature['average'] | humidity['decent'] | atmospheric_pressure['average'], alcohol_solution['60%'])
rule36 = ctrl.Rule(temperature['average'] | humidity['decent'] | atmospheric_pressure['good'], alcohol_solution['60%'])
rule37 = ctrl.Rule(temperature['average'] | humidity['average'] | atmospheric_pressure['poor'], alcohol_solution['60%'])
rule38 = ctrl.Rule(temperature['average'] | humidity['average'] | atmospheric_pressure['average'], alcohol_solution['60%'])
rule39 = ctrl.Rule(temperature['average'] | humidity['average'] | atmospheric_pressure['good'], alcohol_solution['60%'])
rule40 = ctrl.Rule(temperature['average'] | humidity['mediocre'] | atmospheric_pressure['poor'], alcohol_solution['60%'])
rule41 = ctrl.Rule(temperature['average'] | humidity['mediocre'] | atmospheric_pressure['average'], alcohol_solution['60%'])
rule42 = ctrl.Rule(temperature['average'] | humidity['mediocre'] | atmospheric_pressure['good'], alcohol_solution['60%'])
rule43 = ctrl.Rule(temperature['average'] | humidity['poor'] | atmospheric_pressure['poor'], alcohol_solution['60%'])
rule44 = ctrl.Rule(temperature['average'] | humidity['poor'] | atmospheric_pressure['average'], alcohol_solution['60%'])
rule45 = ctrl.Rule(temperature['average'] | humidity['poor'] | atmospheric_pressure['good'], alcohol_solution['60%'])

rule46 = ctrl.Rule(temperature['mediocre'] | humidity['good'] | atmospheric_pressure['poor'], alcohol_solution['40%'])
rule47 = ctrl.Rule(temperature['mediocre'] | humidity['good'] | atmospheric_pressure['average'], alcohol_solution['40%'])
rule48 = ctrl.Rule(temperature['mediocre'] | humidity['good'] | atmospheric_pressure['good'], alcohol_solution['40%'])
rule49 = ctrl.Rule(temperature['mediocre'] | humidity['decent'] | atmospheric_pressure['poor'], alcohol_solution['40%'])
rule50 = ctrl.Rule(temperature['mediocre'] | humidity['decent'] | atmospheric_pressure['average'], alcohol_solution['40%'])
rule51 = ctrl.Rule(temperature['mediocre'] | humidity['decent'] | atmospheric_pressure['good'], alcohol_solution['40%'])
rule52 = ctrl.Rule(temperature['mediocre'] | humidity['average'] | atmospheric_pressure['poor'], alcohol_solution['40%'])
rule53 = ctrl.Rule(temperature['mediocre'] | humidity['average'] | atmospheric_pressure['average'], alcohol_solution['40%'])
rule54 = ctrl.Rule(temperature['mediocre'] | humidity['average'] | atmospheric_pressure['good'], alcohol_solution['40%'])
rule55 = ctrl.Rule(temperature['mediocre'] | humidity['mediocre'] | atmospheric_pressure['poor'], alcohol_solution['40%'])
rule56 = ctrl.Rule(temperature['mediocre'] | humidity['mediocre'] | atmospheric_pressure['average'], alcohol_solution['40%'])
rule57 = ctrl.Rule(temperature['mediocre'] | humidity['mediocre'] | atmospheric_pressure['good'], alcohol_solution['40%'])
rule58 = ctrl.Rule(temperature['mediocre'] | humidity['poor'] | atmospheric_pressure['poor'], alcohol_solution['40%'])
rule59 = ctrl.Rule(temperature['mediocre'] | humidity['poor'] | atmospheric_pressure['average'], alcohol_solution['40%'])
rule60 = ctrl.Rule(temperature['mediocre'] | humidity['poor'] | atmospheric_pressure['good'], alcohol_solution['40%'])

rule61 = ctrl.Rule(temperature['poor'] | humidity['good'] | atmospheric_pressure['poor'], alcohol_solution['20%'])
rule62 = ctrl.Rule(temperature['poor'] | humidity['good'] | atmospheric_pressure['average'], alcohol_solution['20%'])
rule63 = ctrl.Rule(temperature['poor'] | humidity['good'] | atmospheric_pressure['good'], alcohol_solution['20%'])
rule64 = ctrl.Rule(temperature['poor'] | humidity['decent'] | atmospheric_pressure['poor'], alcohol_solution['20%'])
rule65 = ctrl.Rule(temperature['poor'] | humidity['decent'] | atmospheric_pressure['average'], alcohol_solution['20%'])
rule66 = ctrl.Rule(temperature['poor'] | humidity['decent'] | atmospheric_pressure['good'], alcohol_solution['20%'])
rule67 = ctrl.Rule(temperature['poor'] | humidity['average'] | atmospheric_pressure['poor'], alcohol_solution['20%'])
rule68 = ctrl.Rule(temperature['poor'] | humidity['average'] | atmospheric_pressure['average'], alcohol_solution['20%'])
rule69 = ctrl.Rule(temperature['poor'] | humidity['average'] | atmospheric_pressure['good'], alcohol_solution['20%'])
rule70 = ctrl.Rule(temperature['poor'] | humidity['mediocre'] | atmospheric_pressure['poor'], alcohol_solution['20%'])
rule71 = ctrl.Rule(temperature['poor'] | humidity['mediocre'] | atmospheric_pressure['average'], alcohol_solution['20%'])
rule72 = ctrl.Rule(temperature['poor'] | humidity['mediocre'] | atmospheric_pressure['good'], alcohol_solution['20%'])
rule73 = ctrl.Rule(temperature['poor'] | humidity['poor'] | atmospheric_pressure['poor'], alcohol_solution['20%'])
rule74 = ctrl.Rule(temperature['poor'] | humidity['poor'] | atmospheric_pressure['average'], alcohol_solution['20%'])
rule75 = ctrl.Rule(temperature['poor'] | humidity['poor'] | atmospheric_pressure['good'], alcohol_solution['20%'])

solution_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
    rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
    rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
    rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
    rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70,
    rule71, rule72, rule73, rule74, rule75
])

solution = ctrl.ControlSystemSimulation(solution_ctrl)


solution.input['temperature'] = 15
solution.input['humidity'] = 80
solution.input['atmospheric_pressure'] = 900

# Crunch the numbers
solution.compute()

print(solution.output['alcohol_solution'])
alcohol_solution.view(sim=solution)

plt.show()


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
            good
            decent
            average
            mediocre
            poor
            
        humidity:
            dry
            refreshing
            comfortable
            humid
            good
            
        pressure:
            low
            medium
            high

        

"""

