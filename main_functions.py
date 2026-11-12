# Defines functions for project
# Cole Jansma, Vinh Le, Noah Tarver, Bennet Kruse, Connor Schultz, Matthew Spalla
# 11/12/2026

import numpy as np
import openpyxl as xl
from numpy.polynomial import Polynomial as poly
from matplotlib import pyplot as plt

def data_function(car_selection):

    workbook = xl.load_workbook("project_data.xlsx")
    sheet = workbook["Car{}".format(car_selection)]

    gear_ratios_labels = []
    gear_ratios = []
    parameters_symbols = []
    parameters = []
    exp_omega_es = []
    exp_torque_es = []
    max_omega_e = []
    max_omega_e_label = []

    for i in range(4,10): # pulls gear ratios and labels from sheet
        gear_ratio_label = sheet["A{}".format(i)].value
        gear_ratio = sheet["B{}".format(i)].value

        while gear_ratio != np.abs(gear_ratio): # verifies gear ratios are not negative
            gear_ratio = float(input("{} is negative. Please insert it again: ".format(gear_ratio_label)))

        sheet["B{}".format(i)] = gear_ratio # overwrites negative data with positive input
        
        gear_ratios_labels.append(gear_ratio_label)
        gear_ratios.append(gear_ratio)


    for i in range(12,26): # pulls parameters from sheet
        parameter_symbol = sheet["B{}".format(i)].value
        parameter = sheet["C{}".format(i)].value

        while parameter != np.abs(parameter): # verifies parameters are not negative
            parameter = float(input("{} is negative. Please insert it again: ".format(parameter_symbol)))

        sheet["C{}".format(i)] = parameter # overwrites negative data with positive input

        parameters_symbols.append(parameter_symbol)
        parameters.append(parameter)

    for i in range(4,19): # pulls dyno data from sheet
        exp_omega_e = sheet["F{}".format(i)].value
        exp_torque_e = sheet["G{}".format(i)].value

        exp_omega_es.append(exp_omega_e)
        exp_torque_es.append(exp_torque_e)

    # pulls max rpm and label from sheet
    max_omega_e_label.append(sheet["F21"].value)
    max_omega_e.append(sheet["G21"].value)

    workbook.save("project_data.xlsx")

    return  gear_ratios_labels, gear_ratios, parameters_symbols, parameters, exp_omega_es, exp_torque_es, max_omega_e, max_omega_e_label
