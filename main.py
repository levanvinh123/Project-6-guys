# 6 Guys Project
# Cole Jansma, Vinh Le, Noah Tarver, Bennet Kruse, Connor Schultz, Matthew Spalla
# 11/12/2026

import terminalCLS as cl
import openpyxl as xl
import main_functions as mf

cl.cls()

spacer="*"*62

print(spacer)
print("\t\t\t6 Guys Project")
print(spacer)

print("\nCar Options:\n1, 2015 Honda Odyssey (3.5L)\n2, 2019 Mazda MX-5 Miata (Manual)\n3, 2026 Toyota GR Corolla (Manual)\n4, 2017 Chevrolet Equinox LT (2.4L)\n5, Exit")

car_selection = 1 # intializes while loops
counter = 0 # counts how many times the loop runs 

workbook_data = xl.load_workbook("project_data.xlsx")
workbook_results = xl.load_workbook("project_results.xlsx")

# Remove all worksheets for workbook_results
for ws in workbook_results.worksheets:
    workbook_results.remove(ws)

while car_selection!=5: # loops until car_selection=5

    car_selection=float(input("\nPlease select a car (1-4) or exit (5): "))
    counter = counter + 1

    if car_selection!=int(car_selection): # verifies car_selection is valid
        while car_selection!=1 and car_selection!=2 and car_selection!=3 and car_selection!=4 and car_selection!=5:
            car_selection=float(input("\nInvalid selection. Please select a car (1-4) or exit (5): "))

    car_selection=int(car_selection) # transforms car_selection into an integer for use in data_function

    if car_selection!=5: # ends program if car_selection=5
        car, gear_ratios_labels, gear_ratios, parameters_symbols, parameters, exp_omega_es, exp_torque_es, max_omega_e, max_omega_e_label = mf.data_function(workbook_data, car_selection, spacer)
        rs, omega_es, torque_e_Nms, powers, ps, accelerations, wfs, wrs, wf_stats, wr_stats = mf.calculation_function(gear_ratios, parameters, exp_omega_es, exp_torque_es, max_omega_e)
        mf.output_functions(workbook_results, counter, car, gear_ratios_labels, gear_ratios, rs, omega_es, torque_e_Nms, powers, ps, accelerations, wfs, wrs, wf_stats, wr_stats, parameters_symbols, parameters, max_omega_e)

print("\nThank you!\n\n")
