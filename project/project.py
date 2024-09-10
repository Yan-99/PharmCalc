#PharmCalc Program
import sys
import time
from tabulate import tabulate
from pyfiglet import Figlet

def main():
    running = True
    while running:
        figlet = Figlet()
        figlet.setFont(font='slant')
        print(figlet.renderText("Welcome to PharmCalc v1.0!"))
        time.sleep(0.5)
        print(display_menu_main())
        main_input = get_options()
        if main_input == 1:
            age, weight, SCr, gender = get_input_CrCl()
            result = cal_CrCl(age, weight, SCr, gender)
            print(f"{round(result,2)}ml/min")
            print(display_menu_return())
            return_input = get_options()
            if return_input == 1:
                main_input = ""
                running = True
            else:
                main_input = 3

        if main_input == 2:
            gender, race, age, total_cholesterol, smoke, HDL_input, BP_input, BP_tx = get_input_ASCVD()
            total_points = 0
            if gender == "M":
                age_points = cal_age_points_M(age)
                smoke_points = cal_smoke_points_M(smoke,age)
                BP_points = cal_BP_points_M(BP_input,BP_tx)
                HDL_points = cal_HDL_points(HDL_input)
                TC_points = cal_TC_points_M(total_cholesterol, age)
                total_points = age_points + smoke_points + BP_points + HDL_points + TC_points
                final_risk = cal_ASCVDRiskScore_M(total_points,race)
                print(f"Age Points: {age_points}, Smoke Points: {smoke_points}, BP Points: {BP_points}, HDL Points: {HDL_points}, TC Points: {TC_points}, Total: {total_points}")
                print(f"{final_risk} 10-Year Risk(%) from recalibrated SG-FRS-2023")
                print(display_menu_return())
                return_input = get_options()
                if return_input == 1:
                    main_input = ""
                    running = True
                else:
                    main_input = 3

            else:
                age_points = cal_age_points_F(age)
                smoke_points = cal_smoke_points_F(smoke,age)
                BP_points = cal_BP_points_F(BP_input,BP_tx)
                HDL_points = cal_HDL_points(HDL_input)
                TC_points = cal_TC_points_F(total_cholesterol, age)
                total_points = age_points + smoke_points + BP_points + HDL_points + TC_points
                final_risk = cal_ASCVDRiskScore_F(total_points,race)
                print(f"Age Points: {age_points}, Smoke Points: {smoke_points}, BP Points: {BP_points}, HDL Points: {HDL_points}, TC Points: {TC_points}, Total: {total_points}")
                print(f"{final_risk} 10-Year Risk(%) from recalibrated SG-FRS-2023")
                print(display_menu_return())
                return_input = get_options()
                if return_input == 1:
                    main_input = ""
                    running = True
                else:
                    main_input = 3



        if main_input == 3:
            print("Thanks for using PharmCalc!")
            time.sleep(0.5)
            sys.exit()


def display_menu_main():
    main_menu = [{"Key":"1", "Options":"Creatinine Clearance"},
        {"Key":"2", "Options":"ASCVD Risk Score - SG"},
        {"Key":"3", "Options":"Exit"}]
    time.sleep(0.5)
    return(tabulate(main_menu, headers="keys", tablefmt="grid"))


def display_menu_return():
    return_menu = [{"Key":"1", "Options":"Return to main"},
        {"Key":"2", "Options":"Exit"}]
    time.sleep(0.5)
    return(tabulate(return_menu, headers="keys", tablefmt="grid"))


def get_options():
    get_input = int(input("Enter your option: "))
    return get_input


def get_input_CrCl():
    get_age = int(input("Enter age: "))
    get_weight = int(input("Enter weight(kg): "))
    get_SCr = int(input("Enter serum creatinine(umol/L): "))
    get_gender = input("Male or Female? Please enter M or F: ")
    return [get_age, get_weight, get_SCr, get_gender]


def cal_CrCl(age, weight, SCr, gender):
    if gender.upper() == "M":
        result = ((140 - age) * weight) / (0.8 * SCr)
        return result

    else:
        result = (((140 - age) * weight) / (0.8 * SCr) ) * 0.85
        return result


def get_input_ASCVD():
    get_gender = input("Male or Female? Please enter M or F: ")
    get_race = input("Chinese/Malay/Indian? Please enter as C/M/I: ")
    get_age = int(input("Enter age: "))
    get_cholesterol = float(input("Enter total cholesterol(mmol/L): "))
    get_smoking = input("Enter smoker status (Y/N): ")
    get_HDL = float(input("Enter HDL cholesterol: "))
    get_BP = int(input("Enter systolic BP (mmHg): "))
    get_BP_tx = input("Is patient taking BP medications/treated for BP? (Y/N): ")
    return [get_gender, get_race, get_age, round(get_cholesterol,1), get_smoking, round(get_HDL,1), get_BP, get_BP_tx]


def cal_age_points_M(age):
    age_points = 0
    age_dict = {(20, 34):-9,(35, 39):-4,(40, 44):0,(45, 49):3,
                (50, 54):6,(55, 59):8,(60, 64):10,(65, 69):11,
                (70, 74):12, (75, 79):13}
    for (start, end), value in age_dict.items():
        if start <= age <= end:
            age_points = value
        if age < 20:
            age_points = -9
        if age > 79:
            age_points = 13
    return age_points

def cal_age_points_F(age):
    age_points = 0
    age_dict = {(20, 34):-7,(35, 39):-3,(40, 44):0,(45, 49):3,
                (50, 54):6,(55, 59):8,(60, 64):10,(65, 69):12,
                (70, 74):14,(75, 79):16}
    for (start, end), value in age_dict.items():
        if start <= age <= end:
            age_points = value
        if age < 20:
            age_points = -7
        if age > 79:
            age_points = 16
    return age_points


def cal_smoke_points_M(smoke, age):
    smoking_points = 0
    smoke = smoke.upper()
    if smoke == "N":
        smoking_points = 0
        return smoking_points
    else:
        smoking_dict = {(20, 39): 8,(40, 49): 5,(50, 59): 3,(60, 69): 1,(70, 79): 1}

        for (start, end), value in smoking_dict.items():
            if start <= age <= end:
                smoking_points = value
            if age < 20:
                smoking_points = 8
            if age > 79:
                smoking_points = 1
    return smoking_points


def cal_smoke_points_F(smoke, age):
    smoking_points = 0
    smoke = smoke.upper()
    if smoke == "N":
        smoking_points = 0
        return smoking_points
    else:
        smoking_dict = {(20, 39): 9,(40, 49): 7,(50, 59): 4,(60, 69): 2,(70, 79): 1}

        for (start, end), value in smoking_dict.items():
            if start <= age <= end:
                smoking_points = value
            if age < 20:
                smoking_points = 9
            if age > 79:
                smoking_points = 1
    return smoking_points


def cal_BP_points_M(BP, BP_tx):
    BP_points = 0
    BP_tx = BP_tx.upper()
    if BP_tx == "N":
        BP_dict_untreated = {(120,129):0,(130,139):1,(140,159):1}
        for (start, end), value in BP_dict_untreated.items():
            if start <= BP <= end:
                BP_points = value
            if BP < 120:
                BP_points = 0
            if BP >= 160:
                BP_points = 2
        return BP_points

    else:
        BP_dict_treated = {(120,129):1,(130,139):2,(140,159):2}

        for (start, end), value in BP_dict_treated.items():
            if start <= BP <= end:
                BP_points = value
            if BP < 120:
                BP_points = 0
            if BP >= 160:
                BP_points = 3
        return BP_points


def cal_BP_points_F(BP, BP_tx):
    BP_points = 0
    BP_tx = BP_tx.upper()
    if BP_tx == "N":
        BP_dict_untreated = {(120,129):1,(130,139):2,(140,159):3}
        for (start, end), value in BP_dict_untreated.items():
            if start <= BP <= end:
                BP_points = value
            if BP < 120:
                BP_points = 0
            if BP >= 160:
                BP_points = 4
        return BP_points

    else:
        BP_dict_treated = {(120,129):3,(130,139):4,(140,159):5}

        for (start, end), value in BP_dict_treated.items():
            if start <= BP <= end:
                BP_points = value
            if BP < 120:
                BP_points = 0
            if BP >= 160:
                BP_points = 6
        return BP_points


def cal_TC_points_M(TC,age):
    TC_points =0
    if TC < 4.1:
        return TC_points

    else:
        TC_dict = {(4.1,5.1): {(20,39):4, (40,49):3, (50,59):2,(60,69):1,(70,79):0},
               (5.2,6.1):{(20,39):7, (40,49):5, (50,59):3,(60,69):1,(70,79):0},
               (6.2,7.2):{(20,39):9, (40,49):6, (50,59):4,(60,69):2,(70,79):1},
               (7.3,10.0):{(20,39):11, (40,49):8, (50,59):5,(60,69):3,(70,79):1}}

        for (outer_start, outer_end), inner_dict in TC_dict.items():
            if outer_start <= TC <= outer_end:
                for (inner_start,inner_end), value in inner_dict.items():
                    if inner_start <= age <= inner_end:
                        TC_points = value
                        return TC_points
            if TC > 10.0:
                TC = 10.0
                for (outer_start, outer_end), inner_dict in TC_dict.items():
                    if outer_start <= TC <= outer_end:
                        for (inner_start,inner_end), value in inner_dict.items():
                            if inner_start <= age <= inner_end:
                                TC_points = value
                                return TC_points


def cal_TC_points_F(TC,age):
    TC_points =0
    if TC < 4.1:
        return TC_points

    else:
        TC_dict = {(4.1,5.1): {(20,39):4, (40,49):3, (50,59):2,(60,69):1,(70,79):1},
               (5.2,6.1):{(20,39):8, (40,49):6, (50,59):4,(60,69):2,(70,79):1},
               (6.2,7.2):{(20,39):11, (40,49):8, (50,59):5,(60,69):3,(70,79):2},
               (7.3,10.0):{(20,39):13, (40,49):10, (50,59):7,(60,69):4,(70,79):2}}

        for (outer_start, outer_end), inner_dict in TC_dict.items():
            if outer_start <= TC <= outer_end:
                for (inner_start,inner_end), value in inner_dict.items():
                    if inner_start <= age <= inner_end:
                        TC_points = value
                        return TC_points
            if TC > 10.0:
                TC = 10.0
                for (outer_start, outer_end), inner_dict in TC_dict.items():
                    if outer_start <= TC <= outer_end:
                        for (inner_start,inner_end), value in inner_dict.items():
                            if inner_start <= age <= inner_end:
                                TC_points = value
                                return TC_points


def cal_HDL_points(HDL):
    HDL_points = 0
    HDL_dict = {(1.3, 1.5):0,(1.0, 1.2):1}
    for (start, end), value in HDL_dict.items():
        if start <= HDL <= end:
            HDL_points = value
        if HDL < 1.0:
            HDL_points = 2
        if HDL >= 1.6:
            HDL_points = -1
    return HDL_points


def cal_ASCVDRiskScore_M(total_points,race):
    lowest_risk = "<1%"
    if total_points <= 0:
        return lowest_risk

    else:
        if race.upper() == "C":
            ASCVD_dict_C = {(1,3):"<1",
                        (4,7):1,
                        (8,9):2,
                        (10,11):3,
                        (12,12):4,
                        (13,13):5,
                        (14,14):7,
                        (15,15):9,
                        (16,16):11,
                        (17,17):14,
                        (18,18):18,
                        (19,19):23,
                        (20,20):28}
            for (start, end), value in ASCVD_dict_C.items():
                if start <= total_points <= end:
                    risk_percentage = value
                if total_points > 20:
                    risk_percentage = 28
            return f"{risk_percentage}%"

        if race.upper() == "M":
            ASCVD_dict_M = {(1,1):"<1",
                        (2,5):1,
                        (6,7):2,
                        (8,9):3,
                        (10,10):4,
                        (11,11):5,
                        (12,12):7,
                        (13,13):9,
                        (14,14):11,
                        (15,15):14,
                        (16,16):18,
                        (17,17):22,
                        (18,18):28,
                        (19,19):34,
                        (20,20):42}
            for (start, end), value in ASCVD_dict_M.items():
                if start <= total_points <= end:
                    risk_percentage = value
                if total_points > 20:
                    risk_percentage = 42
            return f"{risk_percentage}%"

        if race.upper() == "I":
            ASCVD_dict_I = {(1,4):1,
                        (5,6):2,
                        (7,7):3,
                        (8,8):4,
                        (9,9):5,
                        (10,10):6,
                        (11,11):7,
                        (12,12):10,
                        (13,13):12,
                        (14,14):15,
                        (15,15):19,
                        (16,16):24,
                        (17,17):30,
                        (18,18):37,
                        (19,19):45,
                        (20,20):54}
            for (start, end), value in ASCVD_dict_I.items():
                if start <= total_points <= end:
                    risk_percentage = value
                if total_points > 20:
                    risk_percentage = 54
            return f"{risk_percentage}%"


def cal_ASCVDRiskScore_F(total_points,race):
    lowest_risk = "<1%"
    if total_points <= 8:
        return lowest_risk

    else:
        if race.upper() == "C":
            ASCVD_dict_C = {(9,12):"<1",
                        (13,16):1,
                        (17,18):2,
                        (19,19):3,
                        (20,20):4,
                        (21,21):5,
                        (22,22):7,
                        (23,23):8,
                        (24,24):11,
                        (25,25):14,
                        (26,26):18,
                        (27,27):22}
            for (start, end), value in ASCVD_dict_C.items():
                if start <= total_points <= end:
                    risk_percentage = value
                if total_points > 27:
                    risk_percentage = 22
            return f"{risk_percentage}%"

        if race.upper() == "M":
            ASCVD_dict_M = {(9,9):"<1",
                        (10,14):1,
                        (15,16):2,
                        (17,17):3,
                        (18,18):4,
                        (19,19):5,
                        (20,20):7,
                        (21,21):9,
                        (22,22):11,
                        (23,23):14,
                        (24,24):18,
                        (25,25):23,
                        (26,26):29,
                        (27,27):36}
            for (start, end), value in ASCVD_dict_M.items():
                if start <= total_points <= end:
                    risk_percentage = value
                if total_points > 27:
                    risk_percentage = 36
            return f"{risk_percentage}%"

        if race.upper() == "I":
            ASCVD_dict_I = {(9,12):1,
                        (13,14):2,
                        (15,16):3,
                        (17,17):4,
                        (18,18):6,
                        (19,19):7,
                        (20,20):10,
                        (21,21):12,
                        (22,22):16,
                        (23,23):20,
                        (24,24):25,
                        (25,25):31,
                        (26,26):39,
                        (27,27):47}
            for (start, end), value in ASCVD_dict_I.items():
                if start <= total_points <= end:
                    risk_percentage = value
                if total_points > 27:
                    risk_percentage = 47
            return f"{risk_percentage}%"



if __name__ == "__main__":
    main()


