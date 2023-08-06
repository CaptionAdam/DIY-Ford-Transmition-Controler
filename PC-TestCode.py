CurentGear = 0
PRNDL = 'P'
Solenoids = False
SS1= False #Forward Clutch
SS2 = False #Direct Drum
SS3 = False #Intermediate Band
SS4 = False #Overdrive Band
TCC = False #Torque Converter Lockup

def ShiftState():
    #Reverse Gears
    if CurentGear == -5:
        print('Gear = R-OD')
    elif CurentGear == -4:
        print('Gear = R-4')
    elif CurentGear == -3:
        print('Gear = R-3')
    elif CurentGear == -2:
        print('Gear = R-2')
    elif CurentGear == -1:
        print('Gear = R-1')
    #Neuteral
    elif CurentGear == 0:
        print('Gear = Neutral')
    #Forward Gears
    elif CurentGear == 1:
        print('Gear = 1st')
    elif CurentGear == 2:
        print('Gear = 2nd')

    elif CurentGear == 3:
        print('Gear = 3rd')

    elif CurentGear == 4:
        print('Gear = 4th')

    elif CurentGear == 5:
        print('OverDrive')

    

def ShiftSolenoid():
    global SS1
    global SS2
    global SS3
    global SS4
    if PRNDL == 'P':
        SS1 = True
        SS2 = False
        SS3 = False
        SS4 = False
    elif PRNDL == 'N':
        SS1 = False
        SS2 = False
        SS3 = False
        SS4 = False
    elif CurentGear == 1:
        SS1 = True
        SS2 = False
        SS3 = False
        SS4 = False
    elif CurentGear == 2:
        SS1= True
        SS2 = False
        SS3 = True
        SS4 = False
    elif CurentGear == 3:
        SS1= True
        SS2 = True
        SS3 = False
        SS4 = False
    elif CurentGear == 4:
        SS1 = False
        SS2 = False
        SS3 = False
        SS4 = False
    elif CurentGear == 5:
        SS1 = False
        SS2 = False
        SS3 = True
        SS4 = False

def ActiveSolenoid():
    if Solenoids == True:
        print('Shift Solenoid 1 = ', SS1)
        print('Shift Solenoid 2 = ', SS2)
        print('Shift Solenoid 3 = ', SS3)
        print('Shift Solenoid 4 = ', SS4)
        print('Torque Converter Lockup = ', TCC)

def UserInput(): #Handle Input For System
    global CurentGear
    global shiftType
    global Solenoids
    global TCC
    global PRNDL
    while True:
        ShiftState()
        ActiveSolenoid()
        print('Shift (UP/DOWN)')
        shiftType = input()

        #UP/DOWN SHIFT CODE
        if (shiftType == 'UP') and (PRNDL == 'D'):
                CurentGear = CurentGear + 1
                break
        elif (shiftType == 'DOWN') and (PRNDL == 'D'):
                CurentGear = CurentGear - 1
                break
        if (shiftType == 'UP') and (PRNDL == 'R'):
                CurentGear = CurentGear - 1
                break
        elif (shiftType == 'DOWN') and (PRNDL == 'R'):
                CurentGear = CurentGear + 1
                break
        
        #Shift Solinoid Indicator
        elif shiftType == 'ON':
            Solenoids = True
        elif shiftType == 'OFF':
            Solenoids = False

        #LOCKUP
        elif (shiftType == 'LOCK') and (TCC == False):
            TCC = True
        elif (shiftType == 'LOCK') and (TCC == True):
            TCC = False

        #PRNDL
        elif shiftType == 'P':
            PRNDL = 'P'
            break
        elif shiftType == 'R':
            PRNDL = 'R'
            break
        elif shiftType == 'N':
            PRNDL = 'N'
            break
        elif shiftType == 'D':
            PRNDL = 'D'
            break

        #DIRECT GEAR SELECTION & WRONG VALUE CRASH PREVENTION
        else: 
            try:
                int(shiftType)
                Flag = True
            except ValueError:
                Flag = False
            if Flag == True:
                CurentGear = int(shiftType)
                if PRNDL == 'D':
                    if CurentGear > 5:
                        CurentGear = 5
                    elif CurentGear < 1:
                        CurentGear = 1
                elif PRNDL == 'R':
                    if CurentGear > -1:
                        CurentGear = -1
                    elif CurentGear < -5:
                        CurentGear = -5
                continue
            else:
                continue

def ShifterLocation():
    global PRNDL
    if PRNDL == 'P':
        print('Park')
    elif PRNDL == 'R':
        print('Peverse')
    elif PRNDL == 'N':
        print('Neutral')
    elif PRNDL == 'D':
        print('Drive')
    print('Select P R N D')

def Drive():
    global shiftType
    global CurentGear
    global PRNDL
    CurentGear = 1
    while True:
        if PRNDL != 'D':
            break
        #CurentGear = int(CurentGear)
        UserInput()
        #print(Solenoids) #Testing Shift Solinoid Identification
        ShiftSolenoid()
        
def Reverse():
    global shiftType
    global CurentGear
    global PRNDL
    CurentGear = -1
    while True:
        if PRNDL != 'R':
            break
        UserInput()
        #print(Solenoids) #Testing Shift Solinoid Identification
        ShiftSolenoid()


while True:
    ShifterLocation()
    PRNDL = input()
    if PRNDL == 'P':
        continue
    elif PRNDL == 'R':
        Reverse()
        continue
    elif PRNDL == 'N':
        continue
    elif PRNDL == 'D':
        Drive()
        continue