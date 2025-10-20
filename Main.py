# ProjectName: Rigid Body Rotational Inertia Experiment Calculation
# Author: QZoooM
from math import *

# Var
class Var():
    K = None
    I0 = None
    I1 = None
    I2 = I2_ = None
    I3 = I3_ = None
    I4 = I4_ = None
    I5 = I5_ = None
    I = I_ = None
    Iz = 0.152
    Ij = 0.211
    SerIndex = 0
    LastPage = 0 # For Utility and VarCheck use
    HelpContent = "Help Page\n\nThis is a calculation program for Rigid Body Rotational Inertia Experiment.\nPlease refer to the lab manual for detailed instructions on how to use each function.\n\nThis program can automatically Calculate and Store various parameters related to rigid body rotation.\nMake sure to input the correct values when prompted to ensure accurate calculations.\n\nIf you input invalid data or make a mistake, You can enter the Var Check Page to review and modify variables.\nIf you forget to write down the calculated value, You can return to the Main Menu and Check Variables to see all variables.\n\nFor any questions, please contact the author: QZoooM.\n"

# Check
def Ck_Var():
    print("Var.K: ", Var.K, "\nVar.I0: ", Var.I0, "\nVar.I1': ", Var.I1, "\nVar.I2: ", Var.I2, "\nVar.I2': ", Var.I2_, "\nVar.I3: ", Var.I3, "\nVar.I3': ", Var.I3_, "\nVar.I4: ", Var.I4, "\nVar.I4': ", Var.I4_, "\nVar.I5: ", Var.I5, "\nVar.I5': ", Var.I5_, "\nVar.I: ", Var.I, "\nVar.I': ", Var.I_)

def Ck_I0K():
    if (Var.I0 is None):
        print("set I0 & K manually in the Var class\n")
        Var.I0 = float(input("Input I0: "))
        Var.K = float(input("Input K: "))
        print("I0 & K set successfully.\n")

def Ck_I4_I5_():
    if (Var.I4_ is None):
        print("set I4' manually in the Var class\n")
        Var.I4_ = float(input("Input I4': "))
        print("I4' set successfully.\n")
    if (Var.I5_ is None):
        print("set I5' manually in the Var class\n")
        Var.I5_ = float(input("Input I5': "))
        print("I5' set successfully.\n")

# Func
def Avg3X(x1, x2, x3):
    return (x1+x2+x3) / 3

def Avg15T(t1, t2, t3):
    return Avg3X(t1, t2, t3) / 5

def Avg30T(t1, t2, t3):
    return Avg3X(t1, t2, t3) / 10

# ITheory
def I_md2_SolidZhu(m, D):
    return m * D**2 / 2

def I_mDoDi_EptZhu(m, Do, Di):
    return m * (Do**2 +Di**2) / 8

def I_md2_solidBall(m, D):
    return m * D**2 / 10

def I_mL_Stick(m, L):
    return m * L**2 / 12

def I_T0T1(I_1, T0, T1):
    midVar = I_1 / (T1**2 - T0**2)
    rs_I = midVar * T0**2
    rs_K = midVar * 4 * pi**2
    return [rs_I, rs_K]

def I_mDiDo_Stuck(m, Do, Di):
    return 2 * I_mDoDi_EptZhu(m, Do, Di)

# IExp
def I_KT(T, I):
    rs = Var.K * T**2 / (4 * pi**2) - I
    return rs

def I_KT_Stuck(T, I):
    return 2 * I_KT(T, I)

def I_I4I5mx2(I1, I2, m2, x):
    return I1 + I2 + 2 * m2 * x**2

# Error
def E0(X1, X0):
    return (X1 - X0) / X1

# Server
def Cal_I0K():
    print("[1]: Cal I1'\n[2]: Cal I0 & K\n[3]: Utility\n[4]: Var Check\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 0
    elif (c == '1'):
        print("Input m1 & D1 (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        m1 = float(arr[0])
        D1 = float(arr[1])
        res = I_md2_SolidZhu(m1, D1)
        Var.I1 = res
        print("I1': ", Var.I1)
    elif (c == '2'):
        print("Input T0 & T1 (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        T0 = float(arr[0])
        T1 = float(arr[1])
        if (Var.I1 is None):
            print("I1' is not set yet. Please set I1' first.\n")
            Var.I1 = float(input("Input I1': "))
            print("I1' set successfully.\n")
        I1 = float(Var.I1)
        res = I_T0T1(I1, T0, T1)
        Var.I0 = res[0]
        Var.K = res[1]
        print("I0: ", Var.I0)
        print("K: ", Var.K)
        print("I0 & K calculation completed and updated.\n")
    elif (c == '3'):
        GoUtility()
    elif (c == '4'):
        GoVarCheck()

def Cal_3Obj():
    print("[1]: Cal EptZhu\n[2]: Cal solidBall\n[3]: Cal stick\n[4]: Utility\n[5]: Var Check\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 0
    elif (c == '1'):
        Var.SerIndex = 21
    elif (c == '2'):
        Var.SerIndex = 22
    elif (c == '3'):
        Var.SerIndex = 23
    elif (c == '4'):
        GoUtility()
    elif (c == '5'):
        GoVarCheck()

def Cal_EptZhu():
    print("[1]: Cal Theory I2'\n[2]: Cal Exp I2\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 2
    elif (c == '1'):
        print("Input m & Do & Di (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        m = float(arr[0])
        Do = float(arr[1])
        Di = float(arr[2])
        res = I_mDoDi_EptZhu(m, Do, Di)
        print("Theory I2': ", res)
        Var.I2_ = res
    elif (c == '2'):
        print("Input T: ")
        inp = input("[?]: ")
        T = float(inp)
        Ck_I0K()
        I0 = float(Var.I0)
        res = I_KT(T, I0)
        print("Exp I2: ", res)
        Var.I2 = res

def Cal_solidBall():
    print("[1]: Cal Theory I3'\n[2]: Cal Exp I3\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 2
    elif (c == '1'):
        print("Input m & D (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        m = float(arr[0])
        D = float(arr[1])
        res = I_md2_solidBall(m, D)
        print("Theory I3': ", res)
        Var.I3_ = res
    elif (c == '2'):
        print("Input T: ")
        inp = input("[?]: ")
        T = float(inp)
        I0 = float(Var.Iz)
        res = I_KT(T, I0)
        print("Exp I3: ", res)
        Var.I3 = res

def Cal_stick():
    print("[1]: Cal Theory I4'\n[2]: Cal Exp I4\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 2
    elif (c == '1'):
        print("Input m & L (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        m = float(arr[0])
        L = float(arr[1])
        res = I_mL_Stick(m, L)
        print("Theory I4': ", res)
        Var.I4_ = res
    elif (c == '2'):
        print("Input T(split by space): ")
        inp = input("[?]: ")
        T = float(inp)
        I0 = float(Var.Ij)
        res = I_KT(T, I0)
        print("Exp I4: ", res)
        Var.I4 = res

def Cal_prove():
    print("[1]: Cal Theo & Exp I5\n[2]: CalProve Theo & Exp I\n[3]: Utility\n[4]: Var Check\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 0
    elif (c == '1'):
        Var.SerIndex = 31
    elif (c == '2'):
        Var.SerIndex = 32
    elif (c == '3'):
        GoUtility()
    elif (c == '4'):
        GoVarCheck()

def Cal_I5I5():
    print("[1]: Cal Theory I5'\n[2]: Cal Exp I5\n[3]: Utility\n[4]: Var Check\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 3
    elif (c == '1'):
        print("Input m5 & Do & Di (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        m5 = float(arr[0])
        Do = float(arr[1])
        Di = float(arr[2])
        res = I_mDiDo_Stuck(m5, Do, Di)
        print("Theory I5': ", res)
        Var.I5_ = res
    elif (c == '2'):
        print("Input T5: ")
        inp = input("[?]: ")
        Ck_I0K()
        T = float(inp)
        I0 = float(Var.I0)
        res = I_KT_Stuck(T, I0)
        print("Exp I5: ", res)
        Var.I5 = res
    elif (c == '3'):
        GoUtility()
    elif (c == '4'):
        GoVarCheck()

def Cal_I_I():
    print("[1]: Cal Theory I'\n[2]: Cal Exp I\n[3]: Utility\n[4]: Var Check\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = 3
    elif (c == '1'):
        print("Input T: ")
        inp = input("[?]: ")
        T = float(inp)
        Ck_I4_I5_()
        I4_ = float(Var.I4_)
        I5_ = float(Var.I5_)
        Ck_I0K()
        I0 = float(Var.I0)
        res = I_KT(T, I0)
        print("Theory I': ", res)
        Var.I_ = res
    elif (c == '2'):
        print("Input m5 & x (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        m5 = float(arr[0])
        x = float(arr[1])
        Ck_I4_I5_()
        I4_ = float(Var.I4_)
        I5_ = float(Var.I5_)
        res = I_I4I5mx2(I4_, I5_, m5, x)
        print("Theory I': ", res)
        Var.I_ = res
    elif (c == '3'):
        GoUtility()
    elif (c == '4'):
        GoVarCheck()

def Utility():
    print("Utility Page\n")
    print("[1]: Cal OtherAvg\n[2]: Cal 5TAvg\n[3]: Cal 10TAvg\n[4]: Cal E0\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = Var.LastPage
    elif (c == '1'):
        print("Input x1, x2, x3 (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        x1 = float(arr[0])
        x2 = float(arr[1])
        x3 = float(arr[2])
        res = Avg3X(x1, x2, x3)
        print("Avg3X: ", res)
    elif (c == '2'):
        print("(5T)Input t1, t2, t3 (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        t1 = float(arr[0])
        t2 = float(arr[1])
        t3 = float(arr[2])
        res = Avg15T(t1, t2, t3)
        print("Avg15T: ", res)
    elif (c == '3'):
        print("(10T)Input t1, t2, t3 (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        t1 = float(arr[0])
        t2 = float(arr[1])
        t3 = float(arr[2])
        res = Avg30T(t1, t2, t3)
        print("Avg30T: ", res)
    elif (c == '4'):
        print("(E0)Input Theory X1 & Exp X0 (split by space): ")
        inp = input("[?]: ")
        arr = inp.split(" ")
        X1 = float(arr[0])
        X0 = float(arr[1])
        res = E0(X1, X0)
        print("E0: ", res * 100, "%")

# VarCheck
def VarCheck():
    print("Var Check & Set Page\n")
    print("[1]: Check Variables\n[2]: Set I0 & K\n[3]: Set I1\n[4]: Set I4' & I5'\n[0]: <--Back\n")
    c = input("[?]: ")
    if (c == '0'):
        Var.SerIndex = Var.LastPage
    elif (c == '1'):
        Ck_Var()
    elif (c == '2'):
        print("set I0 & K manually in the Var class\n")
        Var.I0 = float(input("Input I0: "))
        Var.K = float(input("Input K: "))
        print("I0 & K set successfully.\n")
    elif (c == '3'):
        print("set I1' manually in the Var class\n")
        Var.I1 = float(input("Input I1': "))
        print("I1' set successfully.\n")
    elif (c == '4'):
        print("set I4' & I5' manually in the Var class\n")
        Var.I4_ = float(input("Input I4': "))
        Var.I5_ = float(input("Input I5': "))
        print("I4' & I5' set successfully.\n")

def Help():
    print(Var.HelpContent)
    input("Press Enter to continue...\n")

def GoUtility():
    Var.LastPage = Var.SerIndex
    Var.SerIndex = 6

def GoVarCheck():
    Var.LastPage = Var.SerIndex
    Var.SerIndex = 7

def mainServer():
    print("Main Menu\n")
    print("[1][2]: Cal I0 & K\n[3]: Cal 3 type of OBJ\n[4]: prove\n[5]: Check Variables\n[6]: Utility\n[7]: Var Check\n[8]: Get Help\n[0]: []<--Exit\n")
    c = input("[?]: ")
    if (c == '1' or c == '2'):
        Var.SerIndex = 1
    elif (c == '0'):
        exit()
    elif (c == '3'):
        Var.SerIndex = 2
    elif (c == '4'):
        Var.SerIndex = 3
    elif (c == '5'):
        Ck_Var()
    elif (c == '6'):
        GoUtility()
    elif (c == '7'):
        GoVarCheck()
    elif (c == '8'):
        Help()
    else:
        print("See those options?\nFind your target and input its correct number.\n")
        input("Press Enter to continue...\n")


# MainPart
print("Rigid Body Rotational Inertia Experiment Calculation Program\nAuthor: QZoooM")
while (True):
    if (Var.SerIndex == -1):
        exit()
    if (Var.SerIndex == 0):
        mainServer()
    if (Var.SerIndex == 1):
        Cal_I0K()
    if (Var.SerIndex == 2):
        Cal_3Obj()
    if (Var.SerIndex == 21):
        Cal_EptZhu()
    if (Var.SerIndex == 22):
        Cal_solidBall()
    if (Var.SerIndex == 23):
        Cal_stick()
    if (Var.SerIndex == 3):
        Cal_prove()
    if (Var.SerIndex == 31):
        Cal_I5I5()
    if (Var.SerIndex == 32):
        Cal_I_I()
    if (Var.SerIndex == 6):
        Utility()
    if (Var.SerIndex == 7):
        VarCheck()

        