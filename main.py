"""
==========================================
AirQuality System: The breathing problem
==========================================
Problem solved:
    Population need to get know if air condition is not harmful for their health.
    Our AirQuality System allows to do that in simple way.
Authors: Paweł Badysiak (s21166), Wojciech Turek (s21611)
How to run:
Install:
1. pip install scikit-fuzzy
2. pip install matplotlib
3. pip install numpy
After instalation:
  -> in console open folder with main.py and run command "python main.py" to run the script
  -> follow instructions in terminal when program will start
"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
    3 membership functions - three main elements that pollute the air on earth
"""
arsenic = ctrl.Antecedent(np.arange(0, 11, 1), 'arsenic')
cadmium = ctrl.Antecedent(np.arange(0, 11, 1), 'cadmium')
benzopyrene = ctrl.Antecedent(np.arange(0, 11, 1), 'benzopyrene')

"""
    Output data - result as quality of air expressed in scale 1-100 (1 - polluted/dangerous, 100 - best quality) 
"""
air_quality = ctrl.Consequent(np.arange(0, 101, 1), 'air_quality')

"""
    Automatically populate the universe with membership functions
"""
arsenic.automf(3, variable_type='quantity')
cadmium.automf(3, variable_type='quantity')
benzopyrene.automf(3, variable_type='quantity')

"""
    Triangular membership functions generator
"""
air_quality['low'] = fuzz.trimf(air_quality.universe, [0, 0, 30])
air_quality['average'] = fuzz.trimf(air_quality.universe, [15, 45, 70])
air_quality['high'] = fuzz.trimf(air_quality.universe, [60, 100, 100])

"""
    View/statistics in graphic format
"""
arsenic.view()
cadmium.view()
benzopyrene.view()

"""
    Customized "rules" of FuzzyLogic behaviour  
"""
rule1 = ctrl.Rule(arsenic['high'] | cadmium['high'] | benzopyrene['high'], air_quality['low'])
rule2 = ctrl.Rule(arsenic['average'] | cadmium['average'] | benzopyrene['average'], air_quality['average'])
rule3 = ctrl.Rule(arsenic['low'] | cadmium['low'] | benzopyrene['low'], air_quality['high'])

"""
    FuzzyLogic System Controller.
"""
solution_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3
])

"""
    Driver for user to provide data and get result in graphic format
"""
if __name__ == '__main__':

    is_over = True

    # Program runs in loop until user provide valid input
    while is_over:
        val1 = int(input("Arsenic (from 0 to 10): "))
        val2 = int(input("Cadmium (from 0 to 10): "))
        val3 = int(input("Benzopyrene (from 0 to 10): "))

        if (10 >= val1 >= 0) and (10 >= val2 >= 0) and (10 >= val3 >= 0):
            is_over = False

            solution = ctrl.ControlSystemSimulation(solution_ctrl)
            solution.input['arsenic'] = int(val1)
            solution.input['cadmium'] = int(val2)
            solution.input['benzopyrene'] = int(val3)

            solution.compute()

            print(solution.output['air_quality'])
            air_quality.view(sim=solution)

            plt.show()
