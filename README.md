# PharmCalc

A python program for useful pharmacy calculations!

#### Video Demo:  <(https://youtu.be/xaljaE0unZY?si=-lRAZWUythouN-LZ)>

---
#### Libraries/Modules Required

Can be found in requirements.txt

- Used modules such as `sys` and `time` from the Python Standard Library
- Used modules from third-party library (PyPI) such as `tabulate` from `tabulate` and `Figlet` from `pyfiglet`

---
#### Description:
In the main project.py file, it contains several functions to display the main menu which allows users to either 1. calculate creatinine clearance of a patient or 2. calculate the SG-FRS-2023 Risk Score of a patient based on certain inputs.

Main Function Description:
- The main function will act as the user interface, displaying the main menu to allow users to enter their options either to proceed with using the calculators or to exit the program.

- When using the calculators, the various functions as listed below are used to help in calculating and printing the results as required before displaying a menu either to return to the main page or exit the program.

Functions Created
1. `display_menu_main()` displays the main menu opening message as well as options to direct users either to 1. Creatinine Clearance Calculation or 2. ASCVD Risk Calculation.

2. `display_menu_return()` displays the return or exit menu after a certain calculation is over.

3. `get_options()` displays a prompt to get user's options.

4. `get_input_CrCl()` will prompt users to key in essential inputs for creatinine clearance calculations such as age, weight, SCr and gender.

5. `cal_CrCl(age, weight, SCr, gender)` will return the result for calculating CrCl rounded to 2 decimal places as units: ml/min. The parameters given are age = int, weight = int, SCr = int (in umol/L), gender= "M" or "F"

6. `get_input_ASCVD()` will prompt users to key in essential inputs for ASCVD Risk calculation such as age, race, smoking status, systolic BP, BP treatment status, total cholesterol, HDL cholesterol and race. This will return the parameters listed above as a list.

7. `cal_age_points_M(age)` and `cal_age_points_F(age)` will return the result for age points based on the parameter: patients age (age = int) and whether they are male or female - different functions will return different results

8. `cal_smoke_points_M(smoke, age)` and `cal_smoke_points_F(smoke, age)` will return the result for smoke points based on parameters: patients age (age = int) and their smoking status (smoke = "Y" or "N"). This is dependent on gender as well if the patient is either male or female - different functions will return different results

9. `cal_BP_points_M(BP, BP_tx)` and `cal_BP_points_F(BP, BP_tx)` will return the result for blood pressure points based on parameters: patients systolic blood pressure (BP = int) and whether they are currently treated for hypertension/blood pressure (BP_tx = "Y" or "N"). This is dependent on gender as well if the patient is either male or female - different functions will return different results

10. `cal_TC_points_M(TC,age)` and `cal_TC_points_F(TC,age)` will return the result for total cholesterol points based on parameters: patients total cholesterol (TC = float , rounded to 1 decimal place) and their age (age = int). This is dependent on gender as well if the patient is either male or female - different functions will return different results

11. `cal_HDL_points(HDL)` will return the result for HDL points based on the parameter: patients high density lipoprotein (HDL = float, rounded to 1 decimal place) and whether they are male or female - different functions will return different results

12. `cal_ASCVDRiskScore_M(total_points,race)` and `cal_ASCVDRiskScore_F(total_points,race)` will return the result for the SG-FRS-2023 or ASCVD Risk Score as a format string as well as individual scoring points and total points as a format string as well based on parameters: total points (from the summation of age points, smoke points, BP points, TC points and HDL points) and patients race (race = "C" or "M" or "I"). This is dependent on gender as well if the patient is either male or female - different functions will return different results.

---
#### Usage:
To run the application in CS50.dev codespaces:
```
$ python project.py
```

Follow the instructions as stated on the display menus:

![Screenshot of the main menu after successfully running the program](/project/screenshots/main_menu_1.jpg)

---
For Creatinine Clearance calculation:

Inputs needed: Age, Weight, Serum Creatinine, Gender

![Screenshot of the CrCl calculation page](/project/screenshots/crcl_menu.jpg)

---
For ASCVD Risk Score calculation:

Inputs needed: Gender, Race, Age, Total Cholesterol, Smoking Status, High Density Lipoprotein (HDL) Cholesterol, Systolic Blood Pressure, Treatment for Hypertension Status

![Screenshot of the ASCVD Risk calculation page](/project/screenshots/ascvd_risk_menu.jpg)

---
After results calculation, either return to the main menu or exit the program:

![Screenshot of the return to menu or exit the program display](/project/screenshots/return_or_exit_menu.jpg)

---
#### Version:
1.0
