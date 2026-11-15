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

def calculation_function(gear_ratios,parameters,exp_omega_es, exp_torque_es, max_omega_e):

    # Assigns names to parameters to aid in calculation
    car_velocity_kmh = parameters[0]
    terrain_slope = parameters[1]
    wheelbase = parameters[2]
    wheel_radius = parameters[3]
    roll_resistance_coeff = parameters[4]
    CoG_height = parameters[5]
    final_drive_eff = parameters[6]
    transmission_eff = parameters[7]
    car_weight = parameters[8]
    air_density = parameters[9]
    final_drive_ratio = parameters[10]
    front_wheel_CoG_distance = parameters[11]
    drag_coeff = parameters[12]
    frontal_area = parameters[13]

    car_velocity_ms = car_velocity_kmh * 1000 / 3600 # converts km/hr to m/s for calculations

    torque_rpm_curve_fit = poly.fit(exp_omega_es,exp_torque_es,4) # fits a quartic curve to the rpm-torque data

    r_rolling = roll_resistance_coeff * car_weight * np.cos(terrain_slope) # rolling resistance
    grade_load = car_weight * np.sin(terrain_slope) # grade load
    r_air = 0.5 * air_density * drag_coeff * frontal_area * car_velocity_ms**2 # air drag

    r = r_rolling + grade_load + r_air # R

    omega_w = (car_velocity_ms / wheel_radius) * (60/(2*np.pi)) # rpm at wheels
    omega_t = final_drive_ratio * omega_w # rpm at transmission

    omega_es = [] # rpm at engine for each gear
    torque_e_Nms = [] # torque at engine for each gear
    powers = [] # power at engine for each gear
    torque_ts = [] # torque at transmission for each gear
    torque_ds = [] # torque at differential for each gear
    ps = [] # P for each gear

    for i in range(0,6):
        
        omega_e = gear_ratios[i] * omega_t

        if omega_e > max_omega_e[0]:
            omega_e = "OOR"
            omega_es.append(omega_e)

            power = "OOR"
            powers.append(power)

            torque_e_Nm = "OOR"
            torque_e_Nms.append(torque_e_Nm)
            
            torque_t = "OOR"
            torque_ts.append(torque_t)

            torque_d = "OOR"
            torque_ds.append(torque_d)
        else:
            omega_es.append(omega_e)

            torque_e_Nm = torque_rpm_curve_fit(omega_e)
            torque_e_Nms.append(torque_e_Nm)
            
            torque_e_ftlb = torque_e_Nm * 0.737562149

            power = (omega_e * torque_e_ftlb) / 5252
            powers.append(power)

            torque_t = transmission_eff * gear_ratios[i] * torque_e_Nm
            torque_ts.append(torque_t)

            torque_d = final_drive_eff * final_drive_ratio * torque_t
            torque_ds.append(torque_d)

            p = torque_d / wheel_radius
            ps.append(p)

    return r, omega_es, torque_e_Nms, powers, ps




