from datetime import datetime
import pandas as pd
# The head and tail time stamps were used to calculate the total duration of 
# the experiment to check the amount of data.


# Define a function to compute the time period
def caltime (lins, cat):
    # pick the Start & End time
    t1 = lins.iloc[0, 0]
    t2 = lins.iloc[-1, 0]

    if cat==1:
        # convert str to datetime
        t11 = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
        t22 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
    elif cat==2:
        t11 = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S.%f")
        t22 = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S.%f")
    else:
        pass

    # cal the time
    t3 = t22 - t11
    nu = len(lins)
    return t1, t2, t3, nu


# Define different types of data
# Calculate hr time ========================================
hrd = pd.read_csv("hr_data.csv", header=None)
t1, t2, t3, nu = caltime(hrd, 2)
print("Start at:", t1, "\tEnd at:", t2, "\nHR Whole Time:", t3)
print("Avr Time:", t3/nu)

# Calculate prt time =======================================
prtd = pd.read_csv("prt_data.csv", header=None)
t1, t2, t3, nu = caltime(prtd, 2)
print("Start at:", t1, "\tEnd at:", t2, "\nPRT Whole Time:", t3)
print("Avr Time:", t3/nu)

# Calculate rsp time =======================================
rspd = pd.read_csv("rsp_data.csv", header=None)
t1, t2, t3, nu = caltime(rspd, 2)
print("Start at:", t1, "\tEnd at:", t2, "\nRSP Whole Time:", t3)
print("Avr Time:", t3/nu)

# Calculate spo time =======================================
spod = pd.read_csv("spo_data.csv", header=None)
t1, t2, t3, nu = caltime(spod, 2)
print("Start at:", t1, "\tEnd at:", t2, "\nSPO Whole Time:", t3)
print("Avr Time:", t3/nu)

# Calculate spv time =======================================
spvd = pd.read_csv("spv_data.csv", header=None)
t1, t2, t3, nu = caltime(spvd, 2)
print("Start at:", t1, "\tEnd at:", t2, "\nSPV Whole Time:", t3)
print("Avr Time:", t3/nu)
