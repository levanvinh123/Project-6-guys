# 6 Guys Project
# Cole Jansma, Vinh Le, Noah Tarver, Bennet Kruse, Connor Schultz, Matthew Spalla
# 11/12/2026

import terminalCLS as cl
import main_functions as mf

cl.cls()

car_selection=1

gear_ratios_labels, gear_ratios, parameters_symbols, parameters, exp_omega_es, exp_torque_es, max_omega_e, max_omega_e_label=mf.data_function(car_selection)
