"""
==========================================
AirQuality Systems: The breathing problem
==========================================
Authors: Paweł Badysiak (s21166), Wojciech Turek (s21611)
How to run:
Install:
1. pip install scikit-fuzzy
2. pip install matplotlib
After instalation:
  -> in console open folder with main.py and run command "python main.py" to run the script
"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

arsenic = ctrl.Antecedent(np.arange(0, 11, 1), 'arsenic')
cadmium = ctrl.Antecedent(np.arange(0, 11, 1), 'cadmium')
benzopyrene = ctrl.Antecedent(np.arange(0, 11, 1), 'benzopyrene')
air_quality = ctrl.Consequent(np.arange(0, 101, 1), 'air_quality')

arsenic.automf(3, variable_type='quantity')
cadmium.automf(3, variable_type='quantity')
benzopyrene.automf(3, variable_type='quantity')


air_quality['low'] = fuzz.trimf(air_quality.universe, [0, 0, 30])
air_quality['average'] = fuzz.trimf(air_quality.universe, [15, 45, 70])
air_quality['high'] = fuzz.trimf(air_quality.universe, [60, 100, 100])


arsenic.view()
cadmium.view()
benzopyrene.view()


rule1 = ctrl.Rule(arsenic['high'] | cadmium['high'] | benzopyrene['high'], air_quality['low'])
rule2 = ctrl.Rule(arsenic['high'] | cadmium['high'] | benzopyrene['average'], air_quality['low'])
rule3 = ctrl.Rule(arsenic['high'] | cadmium['high'] | benzopyrene['low'], air_quality['low'])

rule4 = ctrl.Rule(arsenic['high'] | cadmium['average'] | benzopyrene['high'], air_quality['low'])
rule5 = ctrl.Rule(arsenic['high'] | cadmium['average'] | benzopyrene['average'], air_quality['low'])
rule6 = ctrl.Rule(arsenic['high'] | cadmium['average'] | benzopyrene['low'], air_quality['average'])

rule7 = ctrl.Rule(arsenic['high'] | cadmium['low'] | benzopyrene['high'], air_quality['low'])
rule8 = ctrl.Rule(arsenic['high'] | cadmium['low'] | benzopyrene['average'], air_quality['average'])
rule9 = ctrl.Rule(arsenic['high'] | cadmium['low'] | benzopyrene['low'], air_quality['low'])

rule10 = ctrl.Rule(arsenic['average'] | cadmium['high'] | benzopyrene['high'], air_quality['low'])
rule11 = ctrl.Rule(arsenic['average'] | cadmium['high'] | benzopyrene['average'], air_quality['average'])
rule12 = ctrl.Rule(arsenic['average'] | cadmium['high'] | benzopyrene['low'], air_quality['average'])

rule13 = ctrl.Rule(arsenic['average'] | cadmium['average'] | benzopyrene['high'], air_quality['low'])
rule14 = ctrl.Rule(arsenic['average'] | cadmium['average'] | benzopyrene['average'], air_quality['average'])
rule15 = ctrl.Rule(arsenic['average'] | cadmium['average'] | benzopyrene['low'], air_quality['low'])

rule16 = ctrl.Rule(arsenic['average'] | cadmium['low'] | benzopyrene['high'], air_quality['average'])
rule17 = ctrl.Rule(arsenic['average'] | cadmium['low'] | benzopyrene['average'], air_quality['average'])
rule18 = ctrl.Rule(arsenic['average'] | cadmium['low'] | benzopyrene['low'], air_quality['high'])

rule19 = ctrl.Rule(arsenic['low'] | cadmium['high'] | benzopyrene['high'], air_quality['low'])
rule20 = ctrl.Rule(arsenic['low'] | cadmium['high'] | benzopyrene['average'], air_quality['average'])
rule21 = ctrl.Rule(arsenic['low'] | cadmium['high'] | benzopyrene['low'], air_quality['high'])

rule22 = ctrl.Rule(arsenic['low'] | cadmium['average'] | benzopyrene['high'], air_quality['average'])
rule23 = ctrl.Rule(arsenic['low'] | cadmium['average'] | benzopyrene['average'], air_quality['high'])
rule24 = ctrl.Rule(arsenic['low'] | cadmium['average'] | benzopyrene['low'], air_quality['high'])

rule25 = ctrl.Rule(arsenic['low'] | cadmium['low'] | benzopyrene['high'], air_quality['high'])
rule26 = ctrl.Rule(arsenic['low'] | cadmium['low'] | benzopyrene['average'], air_quality['high'])
rule27 = ctrl.Rule(arsenic['low'] | cadmium['low'] | benzopyrene['low'], air_quality['high'])


solution_ctrl = ctrl.ControlSystem([
    # rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
    # rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
    # rule21, rule22, rule23, rule24, rule25, rule26,
    rule1, rule14, rule27
])

# solution = ctrl.ControlSystemSimulation(solution_ctrl)
#
#
# solution.input['arsenic'] = 0
# solution.input['cadmium'] = 0
# solution.input['benzopyrene'] = 10
#
# # Crunch the numbers
# solution.compute()
#
# print(solution.output['air_quality'])
# air_quality.view(sim=solution)
#
# plt.show()


if __name__ == '__main__':
    solution = ctrl.ControlSystemSimulation(solution_ctrl)

    val1 = input("Arsenic (from 1 to 10): ")
    val2 = input("Cadmium (from 1 to 10): ")
    val3 = input("Benzopyrene (from 1 to 10): ")

    solution.input['arsenic'] = int(val1)
    solution.input['cadmium'] = int(val2)
    solution.input['benzopyrene'] = int(val3)

    # Crunch the numbers
    solution.compute()

    print(solution.output['air_quality'])
    air_quality.view(sim=solution)

    plt.show()