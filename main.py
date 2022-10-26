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

arsenic = ctrl.Antecedent(np.arange( , ,), 'arsenic')
cadmium = ctrl.Antecedent(np.arange( , ,), 'cadmium')
benzopyrene = ctrl.Antecedent(np.arange( , ,), 'benzopyrene')
air_quality = ctrl.Consequent(np.arange(0, 10, 1), 'air_quality')

arsenic.automf(5)
cadmium.automf(5)
benzopyrene.automf(3)


air_quality['low'] = fuzz.trimf(air_quality.universe, [0, 0, 30])
air_quality['medium'] = fuzz.trimf(air_quality.universe, [0, 30, 70])
air_quality['high'] = fuzz.trimf(air_quality.universe, [30, 70, 100])


arsenic.view()
cadmium.view()
benzopyrene.view()


rule1 = ctrl.Rule(arsenic['good'] | cadmium['good'] | benzopyrene['average'], air_quality['low'])
rule2 = ctrl.Rule(arsenic['good'] | cadmium['good'] | benzopyrene['average'], air_quality['100%'])
rule3 = ctrl.Rule(arsenic['good'] | cadmium['good'] | benzopyrene['good'], air_quality['100%'])
rule4 = ctrl.Rule(arsenic['good'] | cadmium['decent'] | benzopyrene['poor'], air_quality['100%'])
rule5 = ctrl.Rule(arsenic['good'] | cadmium['decent'] | benzopyrene['average'], air_quality['100%'])
rule6 = ctrl.Rule(arsenic['good'] | cadmium['decent'] | benzopyrene['good'], air_quality['100%'])
rule7 = ctrl.Rule(arsenic['good'] | cadmium['average'] | benzopyrene['poor'], air_quality['100%'])
rule8 = ctrl.Rule(arsenic['good'] | cadmium['average'] | benzopyrene['average'], air_quality['100%'])
rule9 = ctrl.Rule(arsenic['good'] | cadmium['average'] | benzopyrene['good'], air_quality['100%'])
rule10 = ctrl.Rule(arsenic['good'] | cadmium['mediocre'] | benzopyrene['poor'], air_quality['100%'])
rule11 = ctrl.Rule(arsenic['good'] | cadmium['mediocre'] | benzopyrene['average'], air_quality['100%'])
rule12 = ctrl.Rule(arsenic['good'] | cadmium['mediocre'] | benzopyrene['good'], air_quality['100%'])
rule13 = ctrl.Rule(arsenic['good'] | cadmium['poor'] | benzopyrene['poor'], air_quality['100%'])
rule14 = ctrl.Rule(arsenic['good'] | cadmium['poor'] | benzopyrene['average'], air_quality['100%'])
rule15 = ctrl.Rule(arsenic['good'] | cadmium['poor'] | benzopyrene['good'], air_quality['100%'])

rule16 = ctrl.Rule(arsenic['decent'] | cadmium['good'] | benzopyrene['poor'], air_quality['80%'])
rule17 = ctrl.Rule(arsenic['decent'] | cadmium['good'] | benzopyrene['average'], air_quality['80%'])
rule18 = ctrl.Rule(arsenic['decent'] | cadmium['good'] | benzopyrene['good'], air_quality['80%'])
rule19 = ctrl.Rule(arsenic['decent'] | cadmium['decent'] | benzopyrene['poor'], air_quality['80%'])
rule20 = ctrl.Rule(arsenic['decent'] | cadmium['decent'] | benzopyrene['average'], air_quality['80%'])
rule21 = ctrl.Rule(arsenic['decent'] | cadmium['decent'] | benzopyrene['good'], air_quality['80%'])
rule22 = ctrl.Rule(arsenic['decent'] | cadmium['average'] | benzopyrene['poor'], air_quality['80%'])
rule23 = ctrl.Rule(arsenic['decent'] | cadmium['average'] | benzopyrene['average'], air_quality['80%'])
rule24 = ctrl.Rule(arsenic['decent'] | cadmium['average'] | benzopyrene['good'], air_quality['80%'])
rule25 = ctrl.Rule(arsenic['decent'] | cadmium['mediocre'] | benzopyrene['poor'], air_quality['80%'])
rule26 = ctrl.Rule(arsenic['decent'] | cadmium['mediocre'] | benzopyrene['average'], air_quality['80%'])
rule27 = ctrl.Rule(arsenic['decent'] | cadmium['mediocre'] | benzopyrene['good'], air_quality['80%'])


solution_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
    rule21, rule22, rule23, rule24, rule25, rule26, rule27
])

solution = ctrl.ControlSystemSimulation(solution_ctrl)


solution.input['arsenic'] = 0
solution.input['cadmium'] = 0
solution.input['benzopyrene'] = 0

# Crunch the numbers
solution.compute()

print(solution.output['air_quality'])
air_quality.view(sim=solution)

plt.show()


