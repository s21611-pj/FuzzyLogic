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
rule2 = ctrl.Rule(arsenic['average'] | cadmium['average'] | benzopyrene['average'], air_quality['average'])
rule3 = ctrl.Rule(arsenic['low'] | cadmium['low'] | benzopyrene['low'], air_quality['high'])

solution_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3
])


if __name__ == '__main__':

    is_over = True

    while is_over:
        val1 = int(input("Arsenic (from 1 to 10): "))
        val2 = int(input("Cadmium (from 1 to 10): "))
        val3 = int(input("Benzopyrene (from 1 to 10): "))

        if (10 >= val1 >= 0) and (10 >= val2 >= 0) and (10 >= val3 >= 0):
            is_over = False

            solution = ctrl.ControlSystemSimulation(solution_ctrl)
            solution.input['arsenic'] = int(val1)
            solution.input['cadmium'] = int(val2)
            solution.input['benzopyrene'] = int(val3)

            # Crunch the numbers
            solution.compute()

            print(solution.output['air_quality'])
            air_quality.view(sim=solution)

            plt.show()
